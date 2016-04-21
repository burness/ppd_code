'''
Coding Just for Fun
Created by burness on 16/3/27.
'''
#-*-coding:utf-8-*-
'''
Coding Just for Fun
Created by burness on 16/3/18.
'''
import pandas as pd
import xgboost as xgb
from env_variable import *
import datetime

def xgb_model_submission(all_file, num=200, debug=True):
    if debug:
        all_data = pd.read_csv(all_file,nrows=500, encoding='gb18030')
    else:
        all_data = pd.read_csv(all_file, encoding='gb18030')
    train_data = all_data[all_data['tag'] == 1]

    feature_data = train_data.drop(['Idx', 'ListingInfo', 'target','tag'],axis=1)
    feature_data.fillna(-1, inplace=True)
    print feature_data.shape
    # labels = train_data['target']
    test_data = all_data[all_data['tag'] == 0]
    test_feature_data = test_data.drop(['Idx', 'ListingInfo', 'target','tag'],axis=1)
    test_feature_data.fillna(-1,inplace=True)


    final_train_data = feature_data
    final_test_data = test_feature_data
    labels = train_data['target']
    test_labels = test_data['target']
    dtrain = xgb.DMatrix(final_train_data, label=labels, missing=-1)
    dtest = xgb.DMatrix(final_test_data, label=test_labels, missing=-1)
    # xgb_params_list = [{'num_round': 2000, 'colsample_bytree': 0.6, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3, 'min_child_weight': 10, 'subsample': 0.5, 'eta': 0.004, 'fit_const': 0.6, 'objective': 'binary:logistic', 'max_depth': 9, 'gamma': 1},
    #                    {'num_round': 2000, 'colsample_bytree': 0.5, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3, 'min_child_weight': 10, 'subsample': 0.5, 'eta': 0.004, 'fit_const': 0.5, 'objective': 'binary:logistic', 'max_depth': 10, 'gamma': 0},
    #                    {'num_round': 2000, 'colsample_bytree': 0.5, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3, 'min_child_weight': 1, 'subsample': 0.75, 'eta': 0.01, 'fit_const': 0.6, 'objective': 'binary:logistic', 'max_depth': 9, 'gamma': 5},
    #                    {'num_round': 2000, 'colsample_bytree': 0.7, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3, 'min_child_weight': 1, 'subsample': 0.8, 'eta': 0.014, 'fit_const': 0.4, 'objective': 'binary:logistic', 'max_depth': 7, 'gamma': 10},
    #                    {'num_round': 2000, 'colsample_bytree': 0.7, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3, 'min_child_weight': 10, 'subsample': 0.8, 'eta': 0.004, 'fit_const': 0.5, 'objective': 'binary:logistic', 'max_depth': 10, 'gamma': 10},
    #                    {'num_round': 2000, 'colsample_bytree': 0.7, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3, 'min_child_weight': 3, 'subsample': 0.5, 'eta': 0.008, 'fit_const': 0.5, 'objective': 'binary:logistic', 'max_depth': 7, 'gamma': 1},
    #                    {'num_round': 2000, 'colsample_bytree': 0.5, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3, 'min_child_weight': 1, 'subsample': 0.66, 'eta': 0.014, 'fit_const': 0.5, 'objective': 'binary:logistic', 'max_depth': 8, 'gamma': 10},
    # {'num_round': 2000, 'colsample_bytree': 0.7, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3, 'min_child_weight': 6, 'subsample': 0.8, 'eta': 0.008, 'fit_const': 0.7, 'objective': 'binary:logistic', 'max_depth': 7, 'gamma': 0},
    # {'num_round': 2000, 'colsample_bytree': 0.6, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3, 'min_child_weight': 1, 'subsample': 0.66, 'eta': 0.01, 'fit_const': 0.6, 'objective': 'binary:logistic', 'max_depth': 6, 'gamma': 5},
    # {'num_round': 2000, 'colsample_bytree': 0.5, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3, 'min_child_weight': 1, 'subsample': 0.8, 'eta': 0.01, 'fit_const': 0.6, 'objective': 'binary:logistic', 'max_depth': 6, 'gamma': 1},
    # {'num_round': 2000, 'colsample_bytree': 0.4, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3, 'min_child_weight': 1, 'subsample': 0.66, 'eta': 0.006, 'fit_const': 0.6, 'objective': 'binary:logistic', 'max_depth': 6, 'gamma': 0},
    # ]
    # xgb_params_list = [
    #     {'num_round': 1200, 'colsample_bytree': 0.7, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3, 'min_child_weight': 10, 'subsample': 0.66, 'eta': 0.009000000000000001, 'fit_const': 0.7, 'objective': 'binary:logistic', 'max_depth': 8, 'gamma': 1},
    #     {'num_round': 900, 'colsample_bytree': 0.8, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3, 'min_child_weight': 1, 'subsample': 0.9, 'eta': 0.015, 'fit_const': 0.4, 'objective': 'binary:logistic', 'max_depth': 7, 'gamma': 10},
    #     {'num_round': 1200, 'colsample_bytree': 0.8, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3, 'min_child_weight': 6, 'subsample': 0.5, 'eta': 0.01, 'fit_const': 0.5, 'objective': 'binary:logistic', 'max_depth': 5, 'gamma': 10},
    #     {'num_round': 1000, 'colsample_bytree': 0.6, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3, 'min_child_weight': 1, 'subsample': 0.66, 'eta': 0.016, 'fit_const': 0.4, 'objective': 'binary:logistic', 'max_depth': 7, 'gamma': 10},
    #     {'num_round': 900, 'colsample_bytree': 0.6, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3, 'min_child_weight': 6, 'subsample': 0.75, 'eta': 0.018000000000000002, 'fit_const': 0.4, 'objective': 'binary:logistic', 'max_depth': 6, 'gamma': 10},
    #     {'num_round': 1800, 'colsample_bytree': 0.4, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3, 'min_child_weight': 10, 'subsample': 0.75, 'eta': 0.008, 'fit_const': 0.5, 'objective': 'binary:logistic', 'max_depth': 7, 'gamma': 1},
    #     {'num_round': 1000, 'colsample_bytree': 0.6, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3, 'min_child_weight': 3, 'subsample': 0.5, 'eta': 0.007, 'fit_const': 0.6, 'objective': 'binary:logistic', 'max_depth': 5, 'gamma': 1},
    #     {'num_round': 1000, 'colsample_bytree': 0.6, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3, 'min_child_weight': 3, 'subsample': 0.8, 'eta': 0.01, 'fit_const': 0.5, 'objective': 'binary:logistic', 'max_depth': 6, 'gamma': 5},
    #     {'num_round': 1400, 'colsample_bytree': 0.7, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3, 'min_child_weight': 3, 'subsample': 0.8, 'eta': 0.013000000000000001, 'fit_const': 0.5, 'objective': 'binary:logistic', 'max_depth': 5, 'gamma': 1}
    # ]
    xgb_params_list = [
        {'num_round': 2400, 'colsample_bytree': 0.5, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3, 'min_child_weight': 6, 'subsample': 0.8, 'eta': 0.016, 'fit_const': 0.4, 'objective': 'binary:logistic', 'max_depth': 10, 'gamma': 1},
        {'num_round': 1400, 'colsample_bytree': 0.7, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3, 'min_child_weight': 10, 'subsample': 0.9, 'eta': 0.008, 'fit_const': 0.5, 'objective': 'binary:logistic', 'max_depth': 6, 'gamma': 5},
        {'num_round': 1800, 'colsample_bytree': 0.4, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3, 'min_child_weight': 10, 'subsample': 0.8, 'eta': 0.01, 'fit_const': 0.4, 'objective': 'binary:logistic', 'max_depth': 7, 'gamma': 0},
        {'num_round': 2200, 'colsample_bytree': 0.7, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3, 'min_child_weight': 1, 'subsample': 0.8, 'eta': 0.014, 'fit_const': 0.7, 'objective': 'binary:logistic', 'max_depth': 7, 'gamma': 5},
        {'num_round': 2200, 'colsample_bytree': 0.6, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3, 'min_child_weight': 1, 'subsample': 0.75, 'eta': 0.02, 'fit_const': 0.4, 'objective': 'binary:logistic', 'max_depth': 6, 'gamma': 5},
        {'num_round': 1200, 'colsample_bytree': 0.6, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3, 'min_child_weight': 6, 'subsample': 0.5, 'eta': 0.02, 'fit_const': 0.4, 'objective': 'binary:logistic', 'max_depth': 10, 'gamma': 10},
        {'num_round': 1200, 'colsample_bytree': 0.7, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3, 'min_child_weight': 6, 'subsample': 0.75, 'eta': 0.01, 'fit_const': 0.4, 'objective': 'binary:logistic', 'max_depth': 5, 'gamma': 1},
        {'num_round': 2400, 'colsample_bytree': 0.6, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3, 'min_child_weight': 10, 'subsample': 0.66, 'eta': 0.012, 'fit_const': 0.6, 'objective': 'binary:logistic', 'max_depth': 6, 'gamma': 1},
        {'num_round': 1200, 'colsample_bytree': 0.6, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3, 'min_child_weight': 1, 'subsample': 0.8, 'eta': 0.02, 'fit_const': 0.6, 'objective': 'binary:logistic', 'max_depth': 6, 'gamma': 5},
        {'num_round': 1000, 'colsample_bytree': 0.6, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3, 'min_child_weight': 10, 'subsample': 0.8, 'eta': 0.02, 'fit_const': 0.6, 'objective': 'binary:logistic', 'max_depth': 5, 'gamma': 5},
        {'num_round': 1200, 'colsample_bytree': 0.7, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3, 'min_child_weight': 3, 'subsample': 0.5, 'eta': 0.01, 'fit_const': 0.5, 'objective': 'binary:logistic', 'max_depth': 6, 'gamma': 1},
        {'num_round': 1400, 'colsample_bytree': 0.7, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3, 'min_child_weight': 1, 'subsample': 0.66, 'eta': 0.016, 'fit_const': 0.7, 'objective': 'binary:logistic', 'max_depth': 7, 'gamma': 5},
        {'num_round': 1800, 'colsample_bytree': 0.7, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3, 'min_child_weight': 6, 'subsample': 0.66, 'eta': 0.014, 'fit_const': 0.5, 'objective': 'binary:logistic', 'max_depth': 6, 'gamma': 10},
        {'num_round': 1400, 'colsample_bytree': 0.4, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3, 'min_child_weight': 3, 'subsample': 0.9, 'eta': 0.012, 'fit_const': 0.4, 'objective': 'binary:logistic', 'max_depth': 6, 'gamma': 0},
        {'num_round': 1200, 'colsample_bytree': 0.5, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3, 'min_child_weight': 6, 'subsample': 0.75, 'eta': 0.014, 'fit_const': 0.4, 'objective': 'binary:logistic', 'max_depth': 5, 'gamma': 10},
        {'num_round': 1400, 'colsample_bytree': 0.7, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3, 'min_child_weight': 1, 'subsample': 0.9, 'eta': 0.01, 'fit_const': 0.6, 'objective': 'binary:logistic', 'max_depth': 7, 'gamma': 10}
    ]
    for i,xgb_params in enumerate(xgb_params_list):
        print 'processing the %dth xgb model'%i
        num_boost_round = xgb_params['num_round']
        xgbr = xgb.train(xgb_params, dtrain,num_boost_round=num_boost_round)
        y_pred = xgbr.predict(dtest, ntree_limit=xgbr.best_iteration)
        sub_file = voting_folder_path+'single_'+datetime.datetime.now().strftime("%m%d")+'_'+str(i)+'.csv'
        pd.DataFrame({'Idx': test_data['Idx'].values, 'score': y_pred}).to_csv(sub_file, index=False)
    print 'finished'

if __name__ == '__main__':
    # xgb_model(all_file=save_master_factorizeV2_file_nan_log_update, num = -1, debug = False)
    xgb_model_submission(all_file=second_save_master_factorizeV2_file_nan_log_updateV2,num=-1, debug=False)
    # xgb_model(save_master_factorizeV2_file_nan_log_update_ensemble, num=-1, debug=False)

