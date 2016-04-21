'''
Coding Just for Fun
Created by burness on 16/3/22.
'''
import pandas as pd
from operator import itemgetter
from env_variable import *
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error, make_scorer, roc_auc_score
from sklearn import grid_search
import numpy as np


def fmean_squared_error(ground_truth, predictions):
    fmean_squared_error_ = mean_squared_error(ground_truth, predictions) ** 0.5
    return fmean_squared_error_


def auc_score(groud_truth, predictions):
    auc_score = roc_auc_score(groud_truth, predictions)
    return auc_score

def report(grid_scores, n_top=3):
    top_scores = sorted(grid_scores, key=itemgetter(1), reverse=True)[:n_top]
    for i, score in enumerate(top_scores):
        print("Model with rank: {0}".format(i + 1))
        print("Mean validation score: {0:.3f} (std: {1:.3f})".format(
                score.mean_validation_score,
                np.std(score.cv_validation_scores)))
        print("Parameters: {0}".format(score.parameters))
        print("")


RMSE = make_scorer(fmean_squared_error, greater_is_better=False)
AUC = make_scorer(auc_score, greater_is_better=True)

def lr_model(all_file, num=200, debug=True):
    if debug:
        all_data = pd.read_csv(all_file,nrows=500, encoding='gb18030')
    else:
        all_data = pd.read_csv(all_file, encoding='gb18030')
    train_data = all_data[all_data['tag'] ==1]
    feature_data = train_data.drop(['Idx', 'ListingInfo', 'target','tag'],axis=1)
    feature_data.fillna(-1, inplace=True)
    # labels = train_data['target']
    feature_importance = pd.read_csv(features_importance_file)
    feature_importance_columns = feature_importance['feature'].tolist()
    feature_importance_columns = feature_importance_columns[:num]
    final_train_data = feature_data[feature_importance_columns]
    # final_train_data = feature_data
    print final_train_data.shape
    labels = train_data['target']
    clf = LogisticRegression()
    param_grid = {'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000], 'penalty':['l2'],'solver':['lbfgs','liblinear']}
    model = grid_search.RandomizedSearchCV(estimator=clf, param_distributions=param_grid, n_jobs=1, cv=2, verbose=0,
                                           n_iter=5, scoring=AUC)
    model.fit(final_train_data,labels)
    report(model.grid_scores_)


if __name__ == '__main__':
    lr_model(all_file=save_master_factorizeV2_file_nan_log_update, num=-1, debug=False)