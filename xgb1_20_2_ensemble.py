# -*-coding:utf-8-*-
'''
Coding Just for Fun
Created by burness on 16/3/7.
'''
import pandas as pd
from xgboostClassifier import XGBoostClassifier
from sklearn import grid_search
import time
from env_variable import *
from sklearn.metrics import mean_squared_error, make_scorer, roc_auc_score


def fmean_squared_error(ground_truth, predictions):
    fmean_squared_error_ = mean_squared_error(ground_truth, predictions) ** 0.5
    return fmean_squared_error_


def auc_score(groud_truth, predictions):
    auc_score = roc_auc_score(groud_truth, predictions)
    return auc_score


RMSE = make_scorer(fmean_squared_error, greater_is_better=False)
AUC = make_scorer(auc_score, greater_is_better=True)


all_data = pd.read_csv(second_save_master_factorizeV2_file_nan_log_update, encoding='gb18030')
train_data = all_data[all_data['tag'] == 1]
# add a column in order to sampling


feature_data = train_data.drop(['Idx', 'ListingInfo', 'target','tag'],axis=1)
feature_data.fillna(-1, inplace=True)
print feature_data.shape
labels = train_data['target']
test_data = all_data[all_data['tag'] == 0]
test_feature_data = test_data.drop(['Idx', 'ListingInfo', 'target','tag'],axis=1)
test_feature_data.fillna(-1,inplace=True)

# feature_importance = pd.read_csv(features_importance_file)
# feature_importance_columns = feature_importance['feature'].tolist()
# feature_importance_columns = feature_importance_columns[:-1]
# final_train_data = feature_data[feature_importance_columns]
final_train_data = feature_data
print final_train_data.shape
# final_test_data = test_feature_data[feature_importance_columns]
final_test_data = test_feature_data
labels = train_data['target']
test_labels = test_data['target']

start_time = time.time()
clf = XGBoostClassifier()
param_grid = {'silent': [1], 'nthread': [3], 'eval_metric': ['auc'],
              'eta': [x * 0.002 for x in range(10)],
              'max_depth': [5, 6, 7, 8, 9, 10], 'num_round': [400, 600, 700, 800, 900,1000,1200,1400],
              'fit_const': [0.4, 0.5, 0.6, 0.7],
              'subsample': [0.5, 0.66, 0.75, 0.8,0.9], 'objective': ['binary:logistic'],
              'gamma': [0, 1, 5, 10, 100],
              'min_child_weight': [1, 3, 6, 10], 'colsample_bytree': [0.4, 0.5, 0.6, 0.7]}

model = grid_search.RandomizedSearchCV(estimator=clf, param_distributions=param_grid, n_jobs=-1, cv=5, verbose=0,
                                       n_iter=30, scoring=AUC)
model.fit(final_train_data, labels)

print("--- Model Finding Best Params spending %s ---" % round(((time.time() - start_time) / 60), 2))

print("Best parameters found by grid search:")
print(model.best_params_)
print("Best CV score:")
print(model.best_score_)
# print("ALL scores:")
# print(model.grid_scores_)
for i in range(len(model.grid_scores_)):
    print(model.grid_scores_[i][0], model.grid_scores_[i][1])
    print(model.grid_scores_[i][2])
    print("----------------------------------")



y_pred = model.predict(final_test_data)
print y_pred.shape

submission = pd.DataFrame({"ID": test_data['Idx'], "score": y_pred})
submission.to_csv("single_0407.csv", index=False)
