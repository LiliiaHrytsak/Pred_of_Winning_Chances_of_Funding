from PreliminaryCleaningClass import PreliminaryCleaning
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.max_columns', None)

raw_data = pd.read_csv('C:/Users/38097/Desktop/Робота з ментором/Дані для прооекту/main_data/ASECB2016.SE1600CSCB10-Data.csv',
                       sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
update_data1 = PreliminaryCleaning()
update_data2 = update_data1.clean(raw_data)
print(update_data2.head(5))
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
