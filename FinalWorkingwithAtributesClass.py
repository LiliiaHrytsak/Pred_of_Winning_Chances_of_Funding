import numpy as np
import pandas as pd
import Encode_labels

class FinalWorkingwithAtributesClass(object):
    def __init__(self):
        pass

    @staticmethod
    def exchange_number_to_category(data, certain_column, certain_flag_column):
        data[certain_column] = np.where(data[certain_column].str.isnumeric() == True, data[certain_column], -999)
        data[certain_column] = pd.to_numeric(data[certain_column])
        dict_mask = Encode_labels.make_mask(data)
        for k, v in dict_mask.items():
            data[certain_flag_column][v] = k


    @staticmethod
    def replace_error_value_in_column(self, certain_column, error_value, correct_value):
        certain_column = certain_column.str.replace(" ", "")
        certain_column = certain_column.str.replace(error_value, correct_value)
        return print(certain_column.value_counts())






