import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder

class SplitAndScale:
    def __init__(self):
        pass

    def split_data(data, train_size, name_target_column):
        X = data.drop(columns=[name_target_column]).copy()
        y = data[name_target_column]
        X_train_valid, X_test_main, y_train_valid, y_test_main = \
            train_test_split(X, y, train_size=train_size)
        return X_train_valid, X_test_main, y_train_valid, y_test_main


    def scale_data(data, not_numerical_columns, X_train, X_test,y_train_valid):
        numerical_columns = data.columns.drop(not_numerical_columns)
        scaler_num = StandardScaler()
        scaler_num.fit_transform(X_train[numerical_columns])
        scaler_num.transform(X_test[numerical_columns])
        scaler_cat = OneHotEncoder()
        scaler_cat.fit_transform(X_train[not_numerical_columns])
        scaler_cat.transform(X_test[not_numerical_columns])
        scaler_cat.transform(y_train_valid)
        return X_train, X_test, numerical_columns
