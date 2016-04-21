'''
Coding Just for Fun
Created by burness on 16/3/18.
'''
import pandas as pd
import numpy as np
from env_variable import *
def clean_data(train_master_file, test_master_file, debug, save_data, city_common):
    if debug:
        train_master_data = pd.read_csv(second_train_master_file, nrows = 500,encoding='gb18030')
        train_master_data['tag'] = 1
        test_master_data = pd.read_csv(second_test_master_file, nrows = 500,encoding='gb18030')
        test_master_data['tag'] = 0
        # target =2
        test_master_data['target'] = 2
        all_master_data = train_master_data.append(test_master_data)
    else:
        train_master_data = pd.read_csv(second_train_master_file,encoding='gb18030')
        train_master_data['tag'] = 1
        test_master_data = pd.read_csv(second_test_master_file,encoding='gb18030')
        test_master_data['tag'] = 0
        test_master_data['target'] = 2
        all_master_data = train_master_data.append(test_master_data)
    # find the category columns
    category_list = ["UserInfo_2", "UserInfo_4", "UserInfo_7", "UserInfo_8", "UserInfo_19", "UserInfo_20", "UserInfo_1", \
                     "UserInfo_3", "UserInfo_5", "UserInfo_6", "UserInfo_9", "UserInfo_2", "UserInfo_4", \
                     "UserInfo_7", "UserInfo_8", "UserInfo_19", "UserInfo_20", "UserInfo_11", "UserInfo_12", "UserInfo_13", \
                     "UserInfo_14", "UserInfo_15", "UserInfo_16", "UserInfo_18", "UserInfo_21", "UserInfo_22", "UserInfo_23", \
                     "UserInfo_24", "Education_Info1", "Education_Info2", "Education_Info3", "Education_Info4", \
                     "Education_Info5", "Education_Info6", "Education_Info7", "Education_Info8", "WeblogInfo_19", \
                     "WeblogInfo_20", "WeblogInfo_21", "SocialNetwork_1", "SocialNetwork_2", "SocialNetwork_7", \
                     "ListingInfo", "SocialNetwork_12"]
    # want to see the UserInfo_2 and UserInfo_4 add the feature whether UserInfo_2 and UserInfo_4 is equal
    city_category_list = ["UserInfo_2", "UserInfo_4"]
    user_info_2 = all_master_data['UserInfo_2'].unique()
    user_info_4 = all_master_data['UserInfo_4'].unique()
    ret_list = list(set(user_info_2).union(set(user_info_4)))
    ret_list_dict = dict(zip(ret_list,range(len(ret_list))))
    print ret_list_dict


    # print all_master_data[['UserInfo_2','UserInfo_4']].head()
    all_master_data['UserInfo_2'] = all_master_data['UserInfo_2'].map(ret_list_dict)
    all_master_data['UserInfo_4'] = all_master_data['UserInfo_4'].map(ret_list_dict)

    for col in category_list:
        if city_common:
            if col in city_category_list:
                continue
            else:
                all_master_data[col] = pd.factorize(all_master_data[col])[0]
        else:
            all_master_data[col] = pd.factorize(all_master_data[col])[0]

    print all_master_data.shape
    city_lat_pd = pd.read_csv(city_geo_info_file,encoding='gb18030')
    # print city_lat_pd.head(200)
    city_lat_pd['UserInfo_2'] = city_lat_pd['city'].map(ret_list_dict)
    city_lat_pd = city_lat_pd.drop('city',axis=1)
    all_master_data = all_master_data.merge(city_lat_pd,on='UserInfo_2',how='left')
    city_lat_pd['UserInfo_4'] = city_lat_pd['UserInfo_2']
    city_lat_pd = city_lat_pd.drop('UserInfo_2',axis=1)
    all_master_data = all_master_data.merge(city_lat_pd,on='UserInfo_4',how='left')
    print all_master_data.shape

    # add a feature whether the UserInfo_2 and UserInfo_4 are equal
    def is_equal(x):
        if x['UserInfo_2'] == x['UserInfo_4']:
            x['UserInfo_2_4_01'] = 0
        else:
            x['UserInfo_2_4_01'] = 1
        return x['UserInfo_2_4_01']

    all_master_data['UserInfo_2_4_01'] = all_master_data.apply(is_equal, axis=1)
    # print all_master_data[['UserInfo_2_4_01','UserInfo_2','UserInfo_4']].head()
    print all_master_data.shape
    # add the ratio\count\all_count of each UserInfo_2 and UserInfo_4
    userinfo_2_ratio_pd = pd.read_csv(second_userinfo_2_ratio)
    userinfo_4_ratio_pd = pd.read_csv(second_userinfo_4_ratio)
    print userinfo_2_ratio_pd.shape
    print userinfo_4_ratio_pd.shape
    # merge the userinfo_2_ratio_pd and userinfo_4_ratio_pd
    all_master_data = all_master_data.merge(userinfo_2_ratio_pd, on='UserInfo_2', how='left')
    all_master_data = all_master_data.merge(userinfo_4_ratio_pd, on='UserInfo_4', how='left')

    print all_master_data.shape


    # save the factorize
    if save_data:
        all_master_data.to_csv(second_save_master_factorize_file,index=None)
    # print all_master_data.shape
    # clean the -1
    all_master_data = all_master_data.replace(-1,np.nan)
    print all_master_data.shape
    if save_data:
        # all_master_data.to_csv(save_master_factorize_file_nan,index=None)
        all_master_data.to_csv(second_save_master_factorizeV2_file_nan,index=None)

    # # dummies
    # for col in category_list:
    #     temp = pd.get_dummies(all_master_data[col],prefix=col)
    #     all_master_data = pd.concat([all_master_data,temp], axis=1)
    # print all_master_data.shape
    # if save_data:
        # all_master_data.to_csv(save_master_factorize_file_nan_dummies,index=None)
        # all_master_data.to_csv(save_master_factorizeV2_file_nan_dummies,index=None)


if __name__ == '__main__':
    clean_data(second_train_master_file, second_test_master_file, debug = False, save_data = True, city_common = True)
    # clean_data(train_master_file,test_master_file,debug = False, save_data = True, city_common = True)



