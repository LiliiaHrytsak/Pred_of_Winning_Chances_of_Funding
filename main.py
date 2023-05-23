import Encode_labels
from PreliminaryCleaningClass import PreliminaryCleaning
from Encode_labels import novalide_date_flags
from Encode_labels import novalide_date_flags
from DeleteHiddenDataClass import DeleteHiddenClass
from FinalWorkingwithAtributesClass import FinalWorkingwithAtributesClass
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.max_columns', None)

raw_data = pd.read_csv('C:/Users/38097/Desktop/Робота з ментором/Дані для прооекту/main_data/ASECB2016.SE1600CSCB10-Data.csv',
                       sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
flags = novalide_date_flags

preliminary_cleaning = PreliminaryCleaning()
update_dataset = preliminary_cleaning.clean(raw_data)
print(update_dataset.shape)

DeleteHiddenClass.delete_hidden_columns(update_dataset, flags)
DeleteHiddenClass.delete_noval_rows(update_dataset, flags)
print(update_dataset.shape)

FinalWorkingwithAtributesClass.exchange_number_to_category(update_dataset, 'EMP', 'EMP_F')
print(update_dataset.shape)

for i in update_dataset.columns:
    if i in Encode_labels.useless_atr_list:
        update_dataset.drop(i, axis=1, inplace=True)
print(update_dataset.shape)
print(update_dataset.sample(20))
# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
