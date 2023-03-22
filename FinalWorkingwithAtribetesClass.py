import numpy as np
import pandas as pd


class FinalWorkingwithAtribetesClass(object):
    def __init__(self):
        pass

    def exchange_number_to_category(self, certain_column, certain_flag_column,  dict_mask):
        certain_column = np.where(certain_column.str.isnumeric() == True, certain_column, -999)
        certain_column = pd.to_numeric(certain_column)
        for k, v in dict_mask.items():
            certain_flag_column[v] = k

    def replace_error_value_in_column(self, certain_column, error_value, correct_value):
        certain_column= certain_column.str.replace(" ", "")
        certain_column = certain_column.str.replace(error_value, correct_value)
        return print(certain_column.value_counts())






