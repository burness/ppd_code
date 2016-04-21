#-*-coding:utf-8-*-
'''
Coding Just for Fun
Created by burness on 16/3/18.
'''
import pandas as pd
import xgboost as xgb
import operator
from env_variable import *

def feature_importance(all_file,debug,feature_importance_file,xgb_fmap):
    if debug:
        all_data = pd.read_csv(all_file,nrows=500, encoding='gb18030')
    else:
        all_data = pd.read_csv(all_file, encoding='gb18030')
    train_data = all_data[all_data['tag'] ==1]
    feature_data = train_data.drop(['Idx', 'ListingInfo', 'target','tag'],axis=1)
    feature_data.fillna(-1, inplace=True)
    labels = train_data['target']
    xgb_fmap = './save_data/xgb_fmap.csv'
    # print xgb_fmap
    def create_feature_map(features):
        outfile = open(xgb_fmap,'w')
        for i, feat in enumerate(feature_data.columns):
            outfile.write('{0}\t{1}\tq\n'.format(i,feat))
        outfile.close()
    # gen xgb.map
    create_feature_map(train_data.columns)

    dtrain = xgb.DMatrix(feature_data, label=labels, missing=-1)

    xgb_params = {'subsample':0.7, 'min_child_weight': 1, 'eval_metric': 'auc', 'fit_const': 0.5,
                  'nthread': 3, 'num_round': 1400, 'gamma': 5, 'max_depth': 6, 'eta': 0.03,
                  'colsample_bytree': 0.6, 'silent': 1, 'objective': 'binary:logistic'}
    gbdt = xgb.train(xgb_params, dtrain, num_boost_round=1400)
    importance = gbdt.get_fscore(fmap=xgb_fmap)
    importance = sorted(importance.items(), key=operator.itemgetter(1),reverse=True)
    df = pd.DataFrame(importance, columns=['feature', 'fscore'])
    df.to_csv(feature_importance_file,index=None)

if __name__ == '__main__':
    # feature_importance(all_file=save_master_factorize_file_nan, debug=False,
    #                    feature_importance_file = features_importance_file, xgb_fmap = xgb_fmap)
    feature_importance(all_file=second_save_master_factorizeV2_file_nan_log_update, debug=False,feature_importance_file = features_importance_file,
                       xgb_fmap = xgb_fmap)
