'''
Coding Just for Fun
Created by burness on 16/3/15.
'''
import pandas as pd
submission = pd.read_csv('voting_0417.csv')
submission.columns = ['Idx','score']
submission['score'] = submission['score'].map(lambda  x : '%.4f'%x)
submission.to_csv('voting_0417_final.csv',index=None)