#-*-coding:utf-8-*-
'''
Coding Just for Fun
Created by burness on 16/3/18.
'''
import pandas as pd
import xgboost as xgb
from env_variable import *

def xgb_model(all_file, num=200, debug=True):
    if debug:
        all_data = pd.read_csv(all_file,nrows=500, encoding='gb18030')
    else:
        all_data = pd.read_csv(all_file, encoding='gb18030')
    train_data = all_data[all_data['tag'] ==1]
    feature_data = train_data.drop(['Idx', 'ListingInfo', 'target','tag'],axis=1)
    feature_data.fillna(-1, inplace=True)
    labels = train_data['target']
    # feature_importance = pd.read_csv(features_importance_file)
    # feature_importance_columns = feature_importance['feature'].tolist()
    # feature_importance_columns = feature_importance_columns[:num]
    # final_train_data = feature_data[feature_importance_columns]
    final_train_data = feature_data
    print final_train_data.shape
    labels = train_data['target']
    dtrain = xgb.DMatrix(final_train_data, label=labels, missing=-1)
    # xgb_params = {'subsample':0.9, 'min_child_weight': 1, 'eval_metric': 'rmse', 'fit_const': 0.5,
    #               'nthread': 3, 'num_round': 700, 'gamma': 5, 'max_depth': 6, 'eta': 0.01,
    #               'colsample_bytree': 0.6, 'silent': 1, 'objective': 'binary:logistic'}
    # xgb_params = {'num_round': 2200, 'colsample_bytree': 0.4, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3,
    #               'min_child_weight': 1, 'subsample': 0.66, 'eta': 0.006, 'fit_const': 0.6, 'objective': 'binary:logistic',
    #               'max_depth': 6, 'gamma': 0}
    xgb_params = {'num_round': 2400, 'colsample_bytree': 0.5, 'silent': 1, 'eval_metric': 'auc', 'nthread': 3,
                  'min_child_weight': 6, 'subsample': 0.8, 'eta': 0.016, 'fit_const': 0.4, 'objective': 'binary:logistic',
                  'max_depth': 10, 'gamma': 1}

    xgb.cv(xgb_params, dtrain, num_boost_round=2400, nfold=5, metrics={'auc'}, show_progress=True)
    print 'finished'

def xgb_model_submission(all_file,num=200,debug=True):
    if debug:
        all_data = pd.read_csv(all_file,nrows=500, encoding='gb18030')
    else:
        all_data = pd.read_csv(all_file, encoding='gb18030')
    train_data = all_data[all_data['tag'] == 1]

    feature_data = train_data.drop(['Idx', 'ListingInfo', 'target','tag'],axis=1)
    feature_data.fillna(-1, inplace=True)
    print feature_data.shape
    labels = train_data['target']
    test_data = all_data[all_data['tag'] == 0]
    test_feature_data = test_data.drop(['Idx', 'ListingInfo', 'target','tag'],axis=1)
    test_feature_data.fillna(-1,inplace=True)

    # feature_importance = pd.read_csv(features_importance_file)
    # feature_importance_columns = feature_importance['feature'].tolist()
    # feature_importance_columns = feature_importance_columns[:num]
    # final_train_data = feature_data[feature_importance_columns]
    # print final_train_data.shape
    # final_test_data = test_feature_data[feature_importance_columns]
    final_train_data = feature_data
    final_test_data = test_feature_data
    labels = train_data['target']
    test_labels = test_data['target']
    dtrain = xgb.DMatrix(final_train_data, label=labels, missing=-1)
    dtest = xgb.DMatrix(final_test_data, label=test_labels, missing=-1)
    xgb_params = {'subsample':0.9, 'min_child_weight': 1, 'eval_metric': 'rmse', 'fit_const': 0.5,
                  'nthread': 3,  'gamma': 5, 'max_depth': 6, 'eta': 0.02,
                  'colsample_bytree': 0.6, 'silent': 1, 'objective': 'binary:logistic'}
    xgbr = xgb.train(xgb_params, dtrain, num_boost_round=1400)
    y_pred = xgbr.predict(dtest, ntree_limit=xgbr.best_iteration)
    pd.DataFrame({'Idx': test_data['Idx'].values, 'score': y_pred}).to_csv(submission_no_feature_importance_file, index=False)
    print 'finished'

if __name__ == '__main__':
    xgb_model(all_file=second_save_master_factorizeV2_file_nan_log_updateV2, num = -1, debug = False)
    # xgb_model_submission(all_file=save_master_factorizeV2_file_nan_log_update,num=-1, debug=False)
    # xgb_model(save_master_factorizeV2_file_nan_log_update_ensemble, num=-1, debug=False)

