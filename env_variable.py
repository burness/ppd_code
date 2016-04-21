#-*-coding: utf-8-*-
'''
Coding Just for Fun
Created by burness on 16/3/18.
'''
data_path = '/Users/burness/datahack/拍拍贷分控比赛/data/PPD-First-Round-Data-Update_2/'
# data_path = '/home/burness/datahack/拍拍贷分控比赛/data/PPD-First-Round-Data-Update_2/'
train_path = data_path + 'train/'
test_path = data_path + 'test/'

train_master_file = train_path + 'PPD_Training_Master_GBK_3_1_Training_Set.csv'
test_master_file = test_path + 'PPD_Master_GBK_2_Test_Set.csv'

train_log_file = train_path + 'PPD_LogInfo_3_1_Training_Set.csv'
test_log_file = test_path + 'PPD_LogInfo_2_Test_Set.csv'

train_userupdate_file = train_path + 'PPD_Userupdate_Info_3_1_Training_Set.csv'
test_userupdate_file = test_path + 'PPD_Userupdate_Info_2_Test_Set.csv'

save_data_path = '/Users/burness/datahack/拍拍贷分控比赛/script/ver2/save_data/'
# save_data_path = '/home/burness/datahack/拍拍贷分控比赛/script/ver2/save_data/'
save_master_factorize_file = save_data_path+'all_master_info_factorize.csv'
# -1 to nan
save_master_factorize_file_nan = save_data_path + 'all_master_inf_factorize_nan.csv'
save_master_factorizeV2_file_nan = save_data_path + 'all_master_info_factorizeV2_nan.csv'
# category to dummies
save_master_factorize_file_nan_dummies = save_data_path + 'all_master_inf_factorize_nan_dummies.csv'
save_master_factorizeV2_file_nan_dummies = save_data_path + 'all_master_inf_factorizeV2_nan_dummies.csv'
# feature importance file
features_importance_file = save_data_path+'features_importance_file.csv'
features_importance_ensemble_file = save_data_path + 'features_importance_ensemble_file.csv'

xgb_fmap = save_data_path + 'xgb_fmap.csv'

submission_file = save_data_path+'single_0319_1.csv'
submission_no_feature_importance_file = save_data_path + 'single_0321_1.csv'

userinfo_2_ratio = save_data_path + 'userinfo_2_ratio.csv'
userinfo_4_ratio = save_data_path + 'userinfo_4_ratio.csv'


# log file
train_log_info_name = train_path + 'PPD_LogInfo_3_1_Training_Set.csv'
test_log_info_name = test_path + 'PPD_LogInfo_2_Test_Set.csv'

all_log_info_file = save_data_path + 'all_log_info_features.csv'

# user update log file
train_update_log_file_name = train_path + 'PPD_Userupdate_Info_3_1_Training_set.csv'
test_update_log_file_name = test_path + 'PPD_Userupdate_Info_2_Test_set.csv'

all_update_info_file = save_data_path + 'all_update_info_features.csv'


save_master_factorizeV2_file_nan_log_update = save_data_path+ 'save_master_factorizeV2_file_nan_log_update.csv'
save_master_factorizeV2_file_nan_log_update_ensemble = save_data_path + 'save_master_factorizeV2_file_nan_log_update_ensemble.csv'


city_geo_info_file = save_data_path+'city_gb180_geocode.csv'

voting_folder_path = save_data_path+'voting_folder5/'

second_train_master_file = train_path + 'train_master.csv'
second_test_master_file = test_path + 'test_master.csv'
second_save_master_factorizeV2_file_nan = save_data_path+ 'second_save_master_factorizeV2_file_nan_log_update.csv'
second_userinfo_2_ratio = save_data_path + 'second_userinfo_2_ratio.csv'
second_userinfo_4_ratio = save_data_path + 'second_userinfo_4_ratio.csv'
second_save_master_factorize_file = save_data_path+'second_all_master_info_factorize.csv'

second_save_master_factorizeV2_file_nan_log_update = save_data_path+ 'second_save_master_factorizeV2_file_nan_log_update.csv'


second_train_log_info_name = train_path + 'train_log.csv'
second_test_log_info_name = test_path + 'test_log.csv'

second_all_log_info_file = save_data_path + 'second_all_log_info_features.csv'


second_userupdate_file = save_data_path+'second_userupdate_info.csv'
second_train_update_log_file_name = train_path + 'train_userupdate.csv'
second_test_update_log_file_name =test_path +'test_userupdate.csv'
second_save_master_factorizeV2_file_nan_log_update_ensemble = save_data_path + 'second_save_master_factorizeV2_file_nan_log_update_ensemble.csv'
second_save_master_factorizeV2_file_nan_log_updateV2 = save_data_path+ 'second_save_master_factorizeV2_file_nan_log_updateV2.csv'