'''
Coding Just for Fun
Created by burness on 16/3/21.
'''
from sklearn.base import BaseEstimator, TransformerMixin
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.embeddings import Embedding
from keras.layers.normalization import BatchNormalization
from keras.layers.recurrent import LSTM
class Lstm_burness(BaseEstimator, TransformerMixin):
    '''
    neurons_list include the input, output, each hidden layers neurons num
    '''
    # def __init__(self,neurons_list, batch_size, nb_epoch,params):
    def __init__(self,**params):
        self.model = None
        # print 'init',params
        self.params = params
        # print 'init2' , self.params

    def build_model(self, feature_size,neurons_list,dropout = [0.5,0.5],activation = 'tanh', init = 'uniform', loss = 'rmse', optimizer = 'adadelta'):
        print neurons_list
        model = Sequential()
        # model.add(Embedding(feature_size,neurons_list[0]))
        for i in range(len(neurons_list)):
            if i == 0:
                print ("Input shape: " + str(neurons_list))
                print ("Adding Layer " + str(i) + ": " + str(neurons_list[i]))
                print 'input_dim ',feature_size
                model.add(Dense(neurons_list[i], input_dim = feature_size, init = init))
            else:
                print ("Adding Layer " + str(i) + ": " + str(neurons_list[i]))
                model.add(Dense(neurons_list[i], init = init))
            print ("Adding " + activation + " layer")
            model.add(Activation(activation))
            model.add(BatchNormalization())
            if len(dropout) > i:
                print ("Adding " + str(dropout[i]) + " dropout")
                model.add(Dropout(dropout[i]))
        model.add(Dense(1, init = init))
        model.compile(loss='mean_squared_error', optimizer='rmsprop')
        return model

    def fit(self, X, y):
        # print 'fit',self.params
        # print self.params['neurons_list']
        neurons_list = self.params['neurons_list']
        # print 'fit ',neurons_list
        # print X.shape[0]
        # neurons_list.insert(0,X.shape[1])
        print neurons_list
        X_feature_size = X.shape[1]
        model = self.build_model(X_feature_size,neurons_list)
        print 'tag'
        # print len(X)
        # print len(X)
        # print len(y.values)
        # print X.shape
        # print y.shape
        model.fit(X.toarray(),y,batch_size=400, nb_epoch=10, validation_split=0.05)
        self.model = model

    def predict(self, X):
        y = self.model.predict(X.toarray())
        return y

    def set_params(self, **params):
        self.params.update(params)
        return self

    def get_params(self, deep = False):
        params = self.params
        print '1',params
        return params