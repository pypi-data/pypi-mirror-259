from finlab import data
import finlab
import pickle
import os
import plotly.express as px
from finlab.backtest import sim
from finlab.tools.event_study import create_factor_data
import tqdm
import numpy as np 
import pandas as pd
from finlab.dataframe import FinlabDataFrame
import cufflinks as cf
from sklearn.linear_model import LinearRegression
from datetime import datetime
from IPython.display import display, HTML
# import df_type

db_path = "/home/sb0487/trade/finlab/finlab_db" #資料儲存路徑



"""
程式碼傷眼滲入


"""
#若未來相關函式增多再開發
class cofindf(FinlabDataFrame):
    @property
    def pr(self):
        # 計算每行的有效值數量
        valid_counts = self.count(axis=1)
        valid_counts = valid_counts.replace(0, np.nan)
        rank_df = self.rank(axis=1, ascending=True, na_option='keep')
        pr_df = rank_df.div(valid_counts, axis=0) * 100
        return pr_df



class Codata:


    def __init__(self,online = True, auto_update = False, df_type = "findf", db_path= db_path):
        print("初始化...")
        self.online = online
        self.auto_update = auto_update
        self.df_type = df_type
        self.db_path = db_path
        
        #finlab db有時會掛掉,因此加入下方函數
        if self.online == True: 
            try:
                self.close, self.day_update_d = self.get_update_date_d() 
                self.monthly_revenue, self.day_update_m = self.get_update_date_m()  
                self.eps, self.day_update_q = self.get_update_date_q() 
                
                print(f"連線 finlab_db,當前日資料最新日期為:{self.day_update_d}")
                print(f"連線 finlab_db,當前月資料最新日期為:{self.day_update_m}")
                print(f"連線 finlab_db,當前季資料最新日期為:{self.day_update_q}")
            except:
                print("抓取不到db資料,請檢察連線狀態,finlab資料庫是否正常")
                pass
        else:
            print("離線模式,auto_update關閉")
            self.auto_update = False
#載入區----------------------------------------------------------------------------------------------------------------
    def get_update_date_d(self):
        close = data.get("price:收盤價")
        day_update_d = close.index[-1]
        
        return close,day_update_d
        
    def get_update_date_m(self):
        monthly_revenue = data.get("monthly_revenue:當月營收")
        day_update_m = monthly_revenue.index[-1]
        return monthly_revenue,day_update_m
        
    def get_update_date_q(self):
        eps = data.get("financial_statement:每股盈餘")
        day_update_q = eps.index[-1]
        return eps,day_update_q
        
    def get_file_path(self,file_name): 
        return os.path.join(self.db_path, file_name.replace(":", "_") + ".pickle")

    def save_file(self,file_df,file_name) :
        file_df.to_pickle(self.get_file_path(file_name))
    
    def load_local(self,file_name): #從地端讀取檔案
        #不把df型態判別寫在這邊理由是:不同df種類自動更新日期判別語法不同,且pickle只有pd能讀,其他也是要轉換
        with open(self.get_file_path(file_name), 'rb') as file:
            file_df = cofindf(pickle.load(file))
        return file_df
    def ouput_type_df(self,file_df):
        if self.df_type == "findf":
            type_df = file_df
        elif self.df_type == "cudf":
            import cudf
            type_df = df_type.DataFrame(file_df)
        elif self.df_type == "sparkdf":
            from pyspark.sql import SparkSession
            spark = SparkSession.builder.appName("Pandas to Spark DataFrame").getOrCreate()
            type_df = spark.createDataFrame(file_df)
        return type_df


    # @classmethod
    def get(self, file_name):
        if not os.path.isdir(self.db_path):
            raise OSError("資料夾路徑錯誤")
        try:
            file_df = self.load_local(file_name)
            print(f"從地端載入: \"{file_name}\"")
            if self.auto_update:
                file_df = self.check_update(file_df,file_name)
            #選擇df輸出型態
            type_df = self.ouput_type_df(file_df)
            return type_df
            
        except FileNotFoundError as e:
            print(f"地端資料庫未發現資料: \"{file_name}\", 改為從finlab下載...")
            # print(f"錯誤訊息: {e}")
            file_df = data.get(file_name)
            self.save_file(file_df,file_name)
            file_df = self.load_local(file_name)
            
            #選擇df輸出型態
            type_df = self.ouput_type_df(file_df)
            return type_df

    
    #需在online = True條件下執行
    def check_update(self,file_df,file_name): #檢查更新日期
        if type(file_df.index[-1]) == int:
            print("自動更新只支援日,月,季資料")
            file_update_df = file_df
        elif file_df.index[-1] == self.day_update_d or file_df.index[-1] ==  self.day_update_q:
            print(f"目前資料已是最新:{file_df.index[-1]}")
            file_update_df = file_df

        elif file_df.index[-1] == self.day_update_m and ((file_df.index[-1]-file_df.index[1]).days)/len(file_df)>3:
            print(f"目前資料已是最新:{file_df.index[-1]}")
            file_update_df = file_df
        else :
            file_df = data.get(file_name)
            self.save_file(file_df,file_name)
            file_update_df = self.load_local(file_name)
            print(f"資料更新至{file_update_df.index[-1]}")
        return file_update_df
    
#產業區----------------------------------------------------------------------------------------------------------------
    
    #把category拆成主分類與細分類
    def get_industry_pro(self):
        industry = self.get('security_industry_themes').dropna()
        def extract_majcategory(category_list):
            matching_categories = set([category.split(':')[0] for category in eval(category_list) if ':' in category])
            return str(list(matching_categories))
        
        def extract_subcategory(category_list):
            matching_categories = [category.split(':')[-1] for category in eval(category_list) if ':' in category]
            return str(matching_categories)
        
        # 应用自定义函数到 DataFrame 的每一行
        industry['maj_category'] = industry['category'].apply(extract_majcategory)
        industry['sub_category'] = industry['category'].apply(extract_subcategory)
        
        return industry

    
    def show_industry(self):
        industry = self.get_industry_pro()
        sub_category_counts_df = pd.DataFrame(industry['sub_category'].apply(eval).explode('sub_category').value_counts()).reset_index()
        maj_category_counts_df = pd.DataFrame(industry['maj_category'].apply(eval).explode('maj_category').value_counts()).reset_index()
        
        industry["maj_category"] = industry["maj_category"].apply(eval)
        industry["sub_category"] = industry["sub_category"].apply(eval)
        industry_explode = industry.explode('maj_category').explode('sub_category')
        industry_explode["count"] = 1
        
        fig = px.treemap(industry_explode, path=[px.Constant("台股產業總總覽"), "maj_category", "sub_category","name"], values='count')
        fig.update_layout(
            margin=dict(t=1, l=1, r=1, b=1)
        )
        
        fig.show()
        return maj_category_counts_df,sub_category_counts_df
    
    def filter_industry(self,file_df, keyword_list, category_type = "maj_category", remove_or_add="remove", exact_or_fuzzy="fuzzy"):
        industry_pro = self.get_industry_pro()
        
        if exact_or_fuzzy == "fuzzy":
            if remove_or_add == "remove":
                
                file_filtered_df = (file_df
                    .loc[:, ~file_df.columns.isin(
                        industry_pro[industry_pro[category_type]
                        .apply(lambda x: bool(set(eval(x)) & set(keyword_list)))]['stock_id']
                        .tolist())]
                )
           
            elif remove_or_add == "add":
                file_filtered_df = (file_df
                    .loc[:, file_df.columns.isin(
                        industry_pro[industry_pro[category_type]
                        .apply(lambda x: bool(set(eval(x)) & set(keyword_list)))]['stock_id']
                        .tolist())]
                )
    
        
        if exact_or_fuzzy == "exact":
            if remove_or_add == "remove": # 完全一樣才移除
                
                file_filtered_df = (file_df
                    .loc[:, ~file_df.columns.isin(
                        industry_pro[industry_pro[category_type]
                        .apply(lambda x: bool(set(eval(x)) == set(keyword_list)))]['stock_id']
                        .tolist())]
                )
    
            elif remove_or_add == "add": # 完全一樣才加入
                file_filtered_df = (file_df
                    .loc[:, file_df.columns.isin(
                        industry_pro[industry_pro[category_type]
                        .apply(lambda x: bool(set(eval(x)) == set(keyword_list)))]['stock_id']
                        .tolist())]
                )
        
        return file_filtered_df



    
    
    #把category拆成主分類與細分類
    def get_industry_pro(self):
        industry = self.get('security_industry_themes').dropna()
        def extract_majcategory(category_list):
            matching_categories = set([category.split(':')[0] for category in eval(category_list) if ':' in category])
            return str(list(matching_categories))
        
        def extract_subcategory(category_list):
            matching_categories = [category.split(':')[-1] for category in eval(category_list) if ':' in category]
            return str(matching_categories)
        
        # 应用自定义函数到 DataFrame 的每一行
        industry['maj_category'] = industry['category'].apply(extract_majcategory)
        industry['sub_category'] = industry['category'].apply(extract_subcategory)
        
        return industry

#便利工具區----------------------------------------------------------------------------------------------------------------

    #需在online = True條件下執行
    def get_rev_date(self,forward_days = 1):
        exits_df = self.close<0
        def update_row(row):
            if row.name in self.monthly_revenue.index:
                return True
            else:
                return row
    
        rev_date = exits_df.apply(update_row, axis=1)
        rev_date_shifted = rev_date.shift(-1)
        for i in range(1,forward_days+1):
            rev_date_shifted_n = rev_date.shift(-i)
            rev_date_shifted = rev_date_shifted  | rev_date_shifted_n
            
        return rev_date_shifted
    
    #需在online = True條件下執行
    def day_to_month(self,buy_df):
        monthly_index_df = FinlabDataFrame(index=self.monthly_revenue.index)
        buy_df  = monthly_index_df.join(buy_df, how='left')
        return buy_df
        

    def get_pr(self, file_df):
        # 計算每行的有效值數量
        valid_counts = file_df.count(axis=1)
        valid_counts[valid_counts == 0] = np.nan
        rank_df = file_df.rank(axis=1, ascending=True, na_option='keep')
        pr_df = rank_df.div(valid_counts, axis=0) * 100
        
        return pr_df

    def display_report_statis(self, file_df):
        max_year_compound_ret = (1 + file_df["return"].mean()) ** (240 / file_df["period"].mean())
    
        html_content = """
        <sorry style="font-size: larger;">交易統計</sorry>
        <ul>
          <li>交易筆數: {}</li>
          <li>平均報酬率: {:.2f}</li>
          <li>平均MDD: {:.2f}</li>
          <li>報酬率標準差: {:.2f}</li>
          <li>平均持有期間(交易日): {:.2f}</li>
          <li>平均處於獲利天數: {:.2f}</li>
          <li>最大年化複利報酬: {:.2f}</li>
        </ul>
        """.format(len(file_df),
                   file_df["return"].mean(),
                   file_df["mdd"].mean(),
                   file_df["return"].std(),
                   file_df["period"].mean(),
                   file_df["pdays"].mean(),
                   max_year_compound_ret)
        
        display(HTML(html_content))
     #------------------------------------------------------------------------------------------------





