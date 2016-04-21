'''
Coding Just for Fun
Created by burness on 16/3/19.
'''
import pandas as pd
from env_variable import *

master_train = pd.read_csv(second_save_master_factorizeV2_file_nan, encoding='gb18030')

a = master_train[['UserInfo_2','target']]
a_all = a.groupby('UserInfo_2').agg('count')
a_0 = a[a['target'] == 0].groupby('UserInfo_2').agg('count')
a_1 = a[a['target'] == 1].groupby('UserInfo_2').agg('count')
a_0_pd = a_0.reset_index()
a_1_pd = a_1.reset_index()
a_all_pd = a_all.reset_index()
print a_all_pd.head()
a_0_all = a_0_pd.merge(a_all_pd,on='UserInfo_2')
print a_0_all.head()
a_0_all['UserInfo_2_ratio'] = a_0_all['target_x']/a_0_all['target_y']
print a_0_all.head(40)
a_0_all.columns = ['UserInfo_2','UserInfo_2_0_count','UserInfo_2_all_count','UserInfo_2_0_ration']
print a_0_all.head(20)

b = master_train[['UserInfo_4','target']]
b_all = b.groupby('UserInfo_4').agg('count')
b_0 = b[b['target'] == 0].groupby('UserInfo_4').agg('count')
b_1 = b[b['target'] == 1].groupby('UserInfo_4').agg('count')
b_0_pd = b_0.reset_index()
b_1_pd = b_1.reset_index()
b_all_pd = b_all.reset_index()
print a_all_pd.head()
b_0_all = b_0_pd.merge(b_all_pd, on='UserInfo_4')
print b_0_all.head()
b_0_all['UserInfo_4_ratio'] = b_0_all['target_x']/b_0_all['target_y']
print b_0_all.head(40)
b_0_all.columns = ['UserInfo_4', 'UserInfo_4_0_count', 'UserInfo_4_all_count', 'UserInfo_4_0_ratio']
print b_0_all.head(20)

a_0_all.to_csv(second_userinfo_2_ratio, encoding='gb18030', index=None)
b_0_all.to_csv(second_userinfo_4_ratio, encoding='gb18030', index=None)
