#-*-coding:utf-8-*-
'''
Coding Just for Fun
Created by burness on 16/3/19.
'''
import pandas as pd
from env_variable import *

train_log_file_pd = pd.read_csv(second_test_log_info_name, encoding='gb18030')
test_log_file_pd = pd.read_csv(second_test_log_info_name, encoding='gb18030')
all_log_info_pd = train_log_file_pd.append(test_log_file_pd)
# # all_log_info_name = '../dat a/all/log_info.csv'
# print all_log_info_pd.shape
#
# all_log_info_pd = pd.read_csv(all_log_info_name, encoding='gb18030')
all_log_info_pd['diff_days'] = all_log_info_pd['Listinginfo1'].astype('datetime64') - all_log_info_pd['LogInfo3'].astype('datetime64')
all_log_info_pd['diff_days'] = all_log_info_pd['diff_days'].astype(str).str.replace(' days 00:00:00.000000000','').astype(int)


all_log_info_pd['LogInfo1'] = all_log_info_pd['LogInfo1'].astype(str)
all_log_info_pd['LogInfo2'] = all_log_info_pd['LogInfo2'].astype(str)
all_log_info_pd['LogInfo1_2'] = all_log_info_pd[['LogInfo1','LogInfo2']].apply(lambda x: ','.join(x),axis=1)
# groupby Idx LogInfo1_2
all_log_info_final_pd = pd.DataFrame()

a= all_log_info_pd.groupby('Idx')['LogInfo1_2'].count()
diff_min = all_log_info_pd.groupby('Idx')['diff_days'].min()
diff_max = all_log_info_pd.groupby('Idx')['diff_days'].max()


freq = a/(1.0+diff_max-diff_min)

all_log_info_final_pd['count'] = a
all_log_info_final_pd['freq'] = freq
all_log_info_final_pd['diff_min'] = diff_min
all_log_info_final_pd['diff_max'] = diff_max
all_log_info_final_pd['period'] = diff_max-diff_min

# print all_log_info_final_pd.reset_index().head()
all_log_info_final_pd = all_log_info_final_pd.reset_index()
# print all_log_info_final_pd.reset_index().head()
all_log_info_final_pd.to_csv(second_all_log_info_file,index=None, encoding='gb18030')




user_update_info_train_pd = pd.read_csv(second_train_update_log_file_name,encoding='gb18030')
user_update_info_test_pd = pd.read_csv(second_test_update_log_file_name, encoding='gb18030')
# user_update_info_train_pd['tag'] = 1
# user_update_info_test_pd['tag'] = 0
user_update_info_all_pd = user_update_info_train_pd.append(user_update_info_test_pd)
user_update_info_all_pd['UserupdateInfo1'] = user_update_info_all_pd['UserupdateInfo1'].str.lower()
user_update_info_all_pd['UserupdateInfo1'] = pd.factorize(user_update_info_all_pd['UserupdateInfo1'])[0]
# print user_update_info_all_pd.head()
update_count = user_update_info_all_pd.groupby('Idx')['UserupdateInfo1'].count()
# print update_count.head()
user_update_info_all_pd['update_diff_days'] = user_update_info_all_pd['ListingInfo1'].astype('datetime64')-user_update_info_all_pd['UserupdateInfo2'].astype('datetime64')
user_update_info_all_pd['update_diff_days'] = user_update_info_all_pd['update_diff_days'].astype(str).str.replace(' days 00:00:00.000000000','').astype(int)
# print user_update_info_all_pd.head()
update_diff_min = user_update_info_all_pd.groupby('Idx')['update_diff_days'].min()
update_diff_max = user_update_info_all_pd.groupby('Idx')['update_diff_days'].max()
update_freq = freq = update_count/(1.0+update_diff_max-update_diff_min)

all_update_info_final_pd = pd.DataFrame()
all_update_info_final_pd['update_count'] = update_count
all_update_info_final_pd['update_idff_min'] = update_diff_min
all_update_info_final_pd['update_idff_max'] = update_diff_max
all_update_info_final_pd['update_freq'] = freq
all_update_info_final_pd['update_period'] = update_diff_max-update_diff_min
all_update_info_final_pd = all_update_info_final_pd.reset_index()
# 增加那些字段信息有更改
# update_info_list = user_update_info_all_pd['UserupdateInfo1'].unique()
print user_update_info_all_pd.shape
Idx_userupdateInfo1 = user_update_info_all_pd[['Idx','UserupdateInfo1']].drop_duplicates()
print Idx_userupdateInfo1.shape
Idx_userupdateInfo1_pd = Idx_userupdateInfo1.assign(c = 1).set_index(["Idx", "UserupdateInfo1"]).unstack("UserupdateInfo1").fillna(0)
Idx_userupdateInfo1_pd = Idx_userupdateInfo1_pd.reset_index()
# print len(update_info_list)
print Idx_userupdateInfo1_pd.shape
print Idx_userupdateInfo1_pd.head(5)
Idx_userupdateInfo1_pd.to_csv(second_userupdate_file,index=False)
# do some process in the file
Idx_userupdateInfo1_pd = pd.read_csv(second_userupdate_file,header=None)
columns_list = ['Idx']
for i in range(55):
    temp_str = 'user_update_'+str(i)
    columns_list.append(temp_str)
Idx_userupdateInfo1_pd.columns = columns_list

print all_update_info_final_pd.shape
all_update_info_final_pd.to_csv(all_update_info_file,index=None, encoding='gb18030')
#
#
# # merge the log info and update info to the save_master_factorizeV2_file_nan
all_master_facotrizeV2_file_nan = pd.read_csv(second_save_master_factorizeV2_file_nan, encoding='gb18030')
print all_master_facotrizeV2_file_nan.shape
all_master_facotrizeV2_file_nan_log = all_master_facotrizeV2_file_nan.merge(all_log_info_final_pd, on='Idx',how='left')
all_master_facotrizeV2_file_nan_log_update = all_master_facotrizeV2_file_nan_log.merge(all_update_info_final_pd, on='Idx', how='left')
print all_master_facotrizeV2_file_nan_log_update.shape

# merge the userupdateinfor1_pd
all_master_facotrizeV2_file_nan_log_update = all_master_facotrizeV2_file_nan_log_update.merge(Idx_userupdateInfo1_pd,on='Idx',how='left')
print all_master_facotrizeV2_file_nan_log_update.shape
all_master_facotrizeV2_file_nan_log_update.to_csv(second_save_master_factorizeV2_file_nan_log_updateV2,index=None)