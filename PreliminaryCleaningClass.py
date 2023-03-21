class PreliminaryCleaning(object):
    def __init__(self):
        pass

    def count_entrances(self, data):
        """ Return  number entrances of identical values

        Parameters:
            data (dataframe): Input dataframe in which we want to  count number entrances of identical values in column
        Returns:
            result_dict (dict): Dictionary which contains number of  entrances of identical values in each column
        """
        result_dict = {}
        for i in data.columns:
            temp_value = data[i].value_counts()
            result_dict[i] = len(temp_value)
        return result_dict

    def count_null_values(self, data):
        """ Return  percent value of null values in each column

        Parameters:
            data (dataframe): Input dataframe in which we want to count percent value
                                of null values in each column
        Returns:
            data_null_counts (float64): Percent number of  null values in each column
        """
        data_null_counts = data.isnull().sum()/data.shape[0]*100
        return data_null_counts

    def get_clean_list(self, data, uniq_values=2, null_perc=90):
        """ Return a list of column names that we want to delete. It's columns in
                which amount of unique values in a column is less than the specific
                value and the percent missing values is more than the specific value

                Parameters:
                    data (dataframe): Input dataframe
                    uniq_values (int): The number of unique values which is not enough
                                        to leave the column for further work
                    null_perc (int): The percentage of missing values in the column
                                        above which the column should be deleted
                Returns:
                    final_list (list[str]): a list of column names for deleting
                """
        one_value_columns = [name for name, value in self.count_entrances(data).items() if value <= uniq_values]
        columns_more_90nulls = list(self.count_null_values(data)[self.count_null_values(data) > null_perc].index)
        final_list = list(set().union(one_value_columns, columns_more_90nulls))
        return final_list

    def clean(self, data):
        """ Return  new dataframe in which we deleted useless columns

                Parameters:
                    data (dataframe): Input dataframe in which we want to delete useless columns
                Returns:
                    new_data (dataframe): Updated dataframe without useless columns
                """
        new_data = data.copy()
        new_data.drop(columns=self.get_clean_list(data), inplace=True)
        return new_data


