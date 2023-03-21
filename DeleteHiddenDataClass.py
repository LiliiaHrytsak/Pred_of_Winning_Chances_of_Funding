import numpy as np


class DeleteHiddenClass(object):
    def __init__(self):
        pass

    def delete_hidden_columns(self, data, flags):
        list_del_columns = []
        for i in data.columns:
            if ((data[i].isin(flags)).sum() / len(data[i])) > 0.5:
                list_del_columns.append(i)
        data.drop(list_del_columns, axis=1, inplace=True)
        return data

    def delete_novalid_rows(self, data, flags):
        list_del_rows = []
        for i in data.columns:
            if data[i][data[i].isin(flags)].index.size > 0:
                list_del_rows.extend(list(data[i][data[i].isin(flags)].index))
        data.drop(np.unique(list_del_rows), axis=0, inplace=True)
        return data

    