import pandas as pd
import pickle

from sklearn import tree
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

class DecisionTreeModel:
    def __init__(self):
        pass


    @staticmethod
    def model_validation( X_train, y_train, X_test, y_test, parameters_dict={}, cv=4):
        model = tree.DecisionTreeClassifier()
        clf = GridSearchCV(model, parameters_dict, cv=cv, scoring='neg_root_mean_squared_error')
        validated_model = clf.fit(X_train, y_train)
        y_pred = validated_model.predict(X_test)
        rmse = mean_squared_error(y_test, y_pred, squared=False)
        print(f'Best parameters of {model}:{clf.best_params_} \n'
            f'RMSE of {model}: {rmse}')
        return validated_model.best_estimator_, rmse, y_pred

    @staticmethod
    def train_model(best_estimator, X_train, X_test, y_train, y_test,num_columns):
            full_X = pd.concat([X_train, X_test], axis=0)
            full_Y = pd.concat([y_train, y_test], axis=0)
            Scaler = StandardScaler()
            Scaler.fit_transform(full_X[num_columns])
            resulted_model = best_estimator.fit(full_X, full_Y)
            finale_model = 'finalized_model.sav'
            pickle.dump(resulted_model, open(finale_model, 'wb'))
            return finale_model, Scaler
