'''
Coding Just for Fun
Created by burness on 16/3/19.
'''
import pandas as pd
from env_variable import *
import numpy as np

train_log_file_pd = pd.read_csv(train_log_info_name, encoding='gb18030')
test_log_file_pd = pd.read_csv(test_log_info_name, encoding='gb18030')
all_log_info_pd = train_log_file_pd.append(test_log_file_pd)
# # all_log_info_name = '../dat a/all/log_info.csv'
# print all_log_info_pd.shape
#
# all_log_info_pd = pd.read_csv(all_log_info_name, encoding='gb18030')
all_log_info_pd['diff_days'] = all_log_info_pd['Listinginfo1'].astype('datetime64') - all_log_info_pd['LogInfo3'].astype('datetime64')
all_log_info_pd['diff_days'] = all_log_info_pd['diff_days'].astype(str).str.replace(' days 00:00:00.000000000','').astype(int)


all_log_info_final_pd = pd.DataFrame()
all_log_info_pd['LogInfo1'] = all_log_info_pd['LogInfo1'].astype(str)
all_log_info_pd['LogInfo2'] = all_log_info_pd['LogInfo2'].astype(str)
all_log_info_pd['LogInfo1_2'] = all_log_info_pd[['LogInfo1','LogInfo2']].apply(lambda x: ','.join(x),axis=1)

a= all_log_info_pd.groupby('Idx')['LogInfo1_2'].count()
diff_min = all_log_info_pd.groupby('Idx')['diff_days'].min()
diff_max = all_log_info_pd.groupby('Idx')['diff_days'].max()


freq = a/(1.0+diff_max-diff_min)

all_log_info_final_pd['count'] = a
all_log_info_final_pd['freq'] = freq
all_log_info_final_pd['diff_min'] = diff_min
all_log_info_final_pd['diff_max'] = diff_max
all_log_info_final_pd['period'] = diff_max-diff_min
all_log_info_final_pd = all_log_info_final_pd.reset_index()
print all_log_info_final_pd.columns
all_log_info_pd['diff_days'] = all_log_info_pd['Listinginfo1'].astype('datetime64') - all_log_info_pd['LogInfo3'].astype('datetime64')
all_log_info_pd['diff_days'] = all_log_info_pd['diff_days'].astype(str).str.replace(' days 00:00:00.000000000','').astype(int)



all_log_info_pd['LogInfo1_2_fac'] = pd.factorize(all_log_info_pd['LogInfo1_2'])[0]
print all_log_info_pd.shape
temp = pd.get_dummies(all_log_info_pd['LogInfo1_2_fac'],prefix='LogInfo1_2_fac')
all_log_info_pd = pd.concat([all_log_info_pd,temp], axis=1)
log_info_list = ['Idx']
for i in range(62):
    log_info_list.append('LogInfo1_2_fac_'+str(i))
print log_info_list
# log_info_list.append
all_log_info_pd = all_log_info_pd[log_info_list]
all_log_info_pd_group = all_log_info_pd.groupby('Idx').agg(sum)
all_log_info_pd_reset = all_log_info_pd_group.reset_index()
print all_log_info_pd_reset[all_log_info_pd_reset['Idx']==10001]
print all_log_info_pd.shape
all_log_info_final_pd = all_log_info_final_pd.merge(all_log_info_pd_reset, on='Idx')
print all_log_info_final_pd.shape
all_log_info_final_pd.to_csv(all_log_info_file,index=None, encoding='gb18030')


# user_update_info_all_pd['update_diff_days'] = user_update_info_all_pd['ListingInfo1'].astype('datetime64')-user_update_info_all_pd['UserupdateInfo2'].astype('datetime64')
# user_update_info_all_pd['update_diff_days'] = user_update_info_all_pd['update_diff_days'].astype(str).str.replace(' days 00:00:00.000000000','').astype(int)
# # print user_update_info_all_pd.head()
# update_diff_min = user_update_info_all_pd.groupby('Idx')['update_diff_days'].min()
# update_diff_max = user_update_info_all_pd.groupby('Idx')['update_diff_days'].max()
# update_freq = freq = update_count/(1.0+update_diff_max-update_diff_min)
# #
# all_update_info_final_pd = pd.DataFrame()
# all_update_info_final_pd['update_count'] = update_count
# all_update_info_final_pd['update_idff_min'] = update_diff_min
# all_update_info_final_pd['update_idff_max'] = update_diff_max
# all_update_info_final_pd['update_freq'] = freq
# all_update_info_final_pd['update_period'] = update_diff_max-update_diff_min
# all_update_info_final_pd = all_update_info_final_pd.reset_index()


user_update_info_train_pd = pd.read_csv(train_update_log_file_name,encoding='gb18030')
user_update_info_test_pd = pd.read_csv(test_update_log_file_name, encoding='gb18030')
user_update_info_train_pd['tag'] = 1
user_update_info_test_pd['tag'] = 0
user_update_info_all_pd = user_update_info_train_pd.append(user_update_info_test_pd)
user_update_info_all_pd['update_diff_days'] = user_update_info_all_pd['ListingInfo1'].astype('datetime64')-user_update_info_all_pd['UserupdateInfo2'].astype('datetime64')
user_update_info_all_pd['update_diff_days'] = user_update_info_all_pd['update_diff_days'].astype(str).str.replace(' days 00:00:00.000000000','').astype(int)
# print user_update_info_all_pd.head()
update_count = user_update_info_all_pd.groupby('Idx')['UserupdateInfo1'].count()
update_diff_min = user_update_info_all_pd.groupby('Idx')['update_diff_days'].min()
update_diff_max = user_update_info_all_pd.groupby('Idx')['update_diff_days'].max()
update_freq = freq = update_count/(1.0+update_diff_max-update_diff_min)
#
all_update_info_final_pd = pd.DataFrame()
all_update_info_final_pd['update_count'] = update_count
all_update_info_final_pd['update_idff_min'] = update_diff_min
all_update_info_final_pd['update_idff_max'] = update_diff_max
all_update_info_final_pd['update_freq'] = freq
all_update_info_final_pd['update_period'] = update_diff_max-update_diff_min
all_update_info_final_pd = all_update_info_final_pd.reset_index()
user_update_info_all_pd['UserupdateInfo1_frac'] = pd.factorize(user_update_info_all_pd['UserupdateInfo1'])[0]
temp = pd.get_dummies(user_update_info_all_pd['UserupdateInfo1_frac'],prefix='UserupdateInfo1_frac')
user_update_info_all_pd = pd.concat([user_update_info_all_pd,temp], axis=1)
userupdate_info_list = ['Idx']
for i in range(87):
    userupdate_info_list.append('UserupdateInfo1_frac_'+str(i))
print userupdate_info_list
# log_info_list.append
user_update_info_all_pd = user_update_info_all_pd[userupdate_info_list]
user_update_info_all_pd_group = user_update_info_all_pd.groupby('Idx').agg(sum)
user_update_info_all_pd_reset = user_update_info_all_pd_group.reset_index()
print user_update_info_all_pd_reset[user_update_info_all_pd_reset['Idx']==10001]
user_update_info_all_pd_reset = user_update_info_all_pd_reset.merge(all_update_info_final_pd, on='Idx')
print user_update_info_all_pd_reset.head()
print user_update_info_all_pd_reset.shape
user_update_info_all_pd_reset.to_csv(all_update_info_file, index=None,encoding='gb18030')

all_master_facotrizeV2_file_nan = pd.read_csv(save_master_factorizeV2_file_nan, encoding='gb18030')
print all_master_facotrizeV2_file_nan.shape
all_master_facotrizeV2_file_nan_log = all_master_facotrizeV2_file_nan.merge(all_log_info_final_pd, on='Idx',how='left')
all_master_facotrizeV2_file_nan_log_update = all_master_facotrizeV2_file_nan_log.merge(user_update_info_all_pd_reset, on='Idx', how='left')
print all_master_facotrizeV2_file_nan_log_update.shape
all_master_facotrizeV2_file_nan_log_update.to_csv(save_master_factorizeV2_file_nan_log_update,index=None)
# print user_update_info_all_pd.head()
# user_update_info_all_pd['UserupdateInfo1'] = user_update_info_all_pd['UserupdateInfo1'].str.lower()
# user_update_info_all_pd['UserupdateInfo1'] = pd.factorize(user_update_info_all_pd['UserupdateInfo1'])[0]
# # print user_update_info_all_pd.head()
# update_count = user_update_info_all_pd.groupby('Idx')['UserupdateInfo1'].count()
# # print update_count.head()
# user_update_info_all_pd['update_diff_days'] = user_update_info_all_pd['ListingInfo1'].astype('datetime64')-user_update_info_all_pd['UserupdateInfo2'].astype('datetime64')
# user_update_info_all_pd['update_diff_days'] = user_update_info_all_pd['update_diff_days'].astype(str).str.replace(' days 00:00:00.000000000','').astype(int)
# # print user_update_info_all_pd.head()
# update_diff_min = user_update_info_all_pd.groupby('Idx')['update_diff_days'].min()
# update_diff_max = user_update_info_all_pd.groupby('Idx')['update_diff_days'].max()
# update_freq = freq = update_count/(1.0+update_diff_max-update_diff_min)
# #
# all_update_info_final_pd = pd.DataFrame()
# all_update_info_final_pd['update_count'] = update_count
# all_update_info_final_pd['update_idff_min'] = update_diff_min
# all_update_info_final_pd['update_idff_max'] = update_diff_max
# all_update_info_final_pd['update_freq'] = freq
# all_update_info_final_pd['update_period'] = update_diff_max-update_diff_min
# all_update_info_final_pd = all_update_info_final_pd.reset_index()
# #
# # # print all_update_info_final_pd.head()
# all_update_info_final_pd.to_csv(all_update_info_file, encoding='gb18030')

#
#
# # merge the log info and update info to the save_master_factorizeV2_file_nan
# all_master_facotrizeV2_file_nan = pd.read_csv(save_master_factorizeV2_file_nan, encoding='gb18030')
# print all_master_facotrizeV2_file_nan.shape
# all_master_facotrizeV2_file_nan_log = all_master_facotrizeV2_file_nan.merge(all_log_info_final_pd, on='Idx',how='left')
# all_master_facotrizeV2_file_nan_log_update = all_master_facotrizeV2_file_nan_log.merge(all_log_info_final_pd, on='Idx', how='left')
# print all_master_facotrizeV2_file_nan_log_update.shape
# all_master_facotrizeV2_file_nan_log_update.to_csv(save_master_factorizeV2_file_nan_log_update,index=None)