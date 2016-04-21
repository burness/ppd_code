#-*-coding:utf-8-*-
'''
Coding Just for Fun
Created by burness on 16/3/26.
'''
from env_variable import *
import pandas as pd
import xgboost as xgb
import itertools
def feature_ensemble(all_file,out_file):
    all_data = pd.read_csv(all_file, encoding='gb18030')
    third_list = []
    # 找出final_train_data中以ThirdParty_Info_Period打头的特征
    feature_importance = pd.read_csv(features_importance_file)
    feature_importance_columns = feature_importance['feature'].tolist()
    for f in feature_importance_columns[:20]:
        if f.find("ThirdParty_Info_Period") !=-1:
            third_list.append(f)
    print third_list
    third_combination_list  = list(itertools.combinations(third_list,2))
    print len(third_combination_list)
    for (first,second) in third_combination_list:
        all_data[first+"_*_"+second] = all_data[first] * all_data[second]
    print all_data.shape
    print all_data.head(2)
    # remove corr

    for (first,second) in third_combination_list:
        all_data[first+"_+_"+second] = all_data[first] + all_data[second]
    print all_data.shape
    print all_data.head(2)

    for (first,second) in third_combination_list:
        all_data[first+"_-_"+second] = all_data[first] - all_data[second]
    print all_data.shape
    print all_data.head(2)


    for (first,second) in third_combination_list:
        all_data[first+"_/_"+second] = all_data[first]*1.0 / all_data[second]
    print all_data.shape
    print all_data.head(2)
    # remove corr
    print "start computing corr"
    feature_corr = all_data.corr()
    print "compute corr done"
    corr_columns_list = []
    for c1_num, column_1 in enumerate(third_list):
        for c2_num, column_2 in enumerate(third_list):
            if column_1 == column_2 or c1_num>c2_num:
                continue
            elif feature_corr[column_1][column_2] > 0.98:
                corr_columns_list.append(column_2)
    print corr_columns_list
    all_data_corr = all_data.drop(corr_columns_list,axis=1)
    print all_data_corr.shape
    all_data_corr.to_csv(out_file)


if __name__ == '__main__':
    feature_ensemble(second_save_master_factorizeV2_file_nan_log_update, second_save_master_factorizeV2_file_nan_log_update_ensemble)
