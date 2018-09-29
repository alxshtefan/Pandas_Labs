import pandas as pd
import numpy as np


class First:
    my_list = None
    my_tuple = None
    my_string_list = None
    my_pandas_series = None
    my_numpy_vector = None
    my_numpy_nan_vector = None
    my_numpy_array = None

    def __init__(self):
        # https://pythonworld.ru/tipy-dannyx-v-python/spiski-list-funkcii-i-metody-spiskov.html
        self.my_list = [341, 52, 3, 64, 5]
        # print(self.my_list, end='\n\n')

        # https://pythonworld.ru/tipy-dannyx-v-python/kortezhi-tuple.html
        # immutable, tuple('12345') => ('1' ... '5')
        # Pay attention to this bracket '(' , in array or list it is like this '['
        self.my_tuple = (1, 2, 3, 4, 5)
        # print(self.my_tuple, end='\n\n')

        # https://www.dotnetperls.com/string-list-python
        self.my_string_list = ['one', 'two', 'three', 'four', 'five']
        # print(self.my_string_list, end='\n\n')

        # https://khashtamov.com/ru/pandas-introduction/
        self.my_pandas_series = pd.Series([4, 3, 2, 1, 0])
        # print(self.my_pandas_series)
        # print('Indexes:', end=' '), print(self.my_pandas_series.index)
        # print('Values:', end=' '), print(self.my_pandas_series.values, end='\n\n')

        # https://docs.scipy.org/doc/numpy-1.15.1/user/quickstart.html
        self.my_numpy_vector = np.arange(5)
        # print(self.my_numpy_vector, end='\n\n')

        # https://stackoverflow.com/questions/1704823/initializing-numpy-matrix-to-something-other-than-zero-or-one
        self.my_numpy_nan_vector = np.empty(5)
        self.my_numpy_nan_vector.fill(np.nan)
        # print(self.my_numpy_nan_vector, end='\n\n')

        self.my_numpy_array = np.array([[x for x in range(0, 35)] for y in range(0, 10)])
        # print(self.my_numpy_array, end='\n\n')


# Fill collections
def task_1():
    return First()


# Create data frame & delete NaN column
def task_2(first):
    df = pd.DataFrame({
        'LIST': first.my_list,
        'TUPLE': first.my_tuple,
        'STRING LIST': first.my_string_list,
        'SERIES': first.my_pandas_series,
        'VECTOR': first.my_numpy_vector,
        'NaN_VECTOR': first.my_numpy_nan_vector,
        'ARRAY': [first.my_numpy_array[i] for i in range(0, 5)]
    })
    df = df.drop(['NaN_VECTOR'], axis='columns')
    return df


# Apply methods of analysis
def task_3(df):
    print('Median\n', df['LIST'].median())
    print('Average\n', df['LIST'].mean())
    print('Percentile\n', df['LIST'].quantile())


# Find column where max = min, print it
def task_4(df):
    for el in df:
        max_in_col = df[el].max()
        min_in_col = df[el].min()
        if max_in_col == min_in_col:
            print(df[el])


# Delete columns that are the most different by the average value among all columns
def task_5(df):
    df_average = 0
    for el in df:
        try:
            df_average += df[el].mean()
        except TypeError:
            print(end="")
    df_average /= len(df)

    max_differ = None
    min_differ = None
    for el in df:
        try:
            average = df[el].mean()

            if max_differ is None:
                max_differ = el
                continue

            if min_differ is None:
                min_differ = el
                continue

            if df[max_differ].mean() < average:
                max_differ = el

            if df[min_differ].mean() > average:
                min_differ = el
        except TypeError:
            print(end="")

    df = df.drop([max_differ], axis='columns')
    df = df.drop([min_differ], axis='columns')
    return df


# Convert MxN array to columns of the data frame
def task_6(df):
    counter = 0
    arrays = df['ARRAY']
    for el in arrays:
        df['ARRAY_' + str(counter)] = el[:5]
        counter += 1
    df.drop(['ARRAY'], axis='columns')
    return df


# Count correlation
# https://stackoverflow.com/questions/42579908/use-corr-to-get-the-correlation-between-two-columns
def task_7(df):
    print(df['LIST'].corr(df['ARRAY_2']))
    print(df.corr())


def main():
    first = task_1()
    df = task_2(first)
    task_3(df.drop(['ARRAY'], axis='columns'))
    task_4(df.drop(['ARRAY'], axis='columns'))
    df_copy = df
    df = task_5(df.drop(['ARRAY'], axis='columns'))
    df = task_6(df_copy)
    task_7(df)


if __name__ == '__main__':
    main()
