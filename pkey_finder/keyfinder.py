import math
import numpy as np
import pandas as pd
import sys

from datetime import datetime
import itertools

def findkey(file_name,key_len):
    column_to_exclud = ['ID'] ## add columns which should be part of the key
    file_name = file_name
    cols_len_in_key = key_len
    df = pd.read_csv(file_name, sep=',')
    print(df.head())
    colmns = ['column_name', 'count']
    table_row_count = len(df)
    list_of_keys = []
    data = []
    key_found = ''
    for cols in df.columns:
        if cols not in column_to_exclud:
            data.append((cols, len(df[cols].unique())))
            ## Create a seperate logic to just find the primary key using only 1 column - can check this inside this for loop
            if (len(df) == len(df[cols].unique())):
                # print('found the key ->' + cols)
                list_of_keys.append((cols, 1, len(df[cols].unique()), table_row_count))
                key_found = 'yesssssss'
                break

    if (key_found != 'yes'):
        uniq_vals_count = pd.DataFrame(data, columns=colmns)
        uniq_vals_count = uniq_vals_count.sort_values(by='count', ascending=False)
        columns_list = list(uniq_vals_count[0:cols_len_in_key - 1]['column_name'])
        # print(list_of_keys)

        ## only creating combination of maximum 5 columns. The combination length will start from 2, bascially a search for composite key
        column_list = []
        for i in range(2, cols_len_in_key):
            combin = list(itertools.combinations(columns_list, i))
            column_list.extend(combin)

        ## Iterate through below loop and do the group by on each of the combination and check if its a composite primary key or not.
        # print(column_list)

        for i in range(0, len(column_list)):
            listToStr = [x for x in column_list[i]]
            df1 = df.fillna(-1).groupby(listToStr).size().to_frame().reset_index()
            key_length = len(listToStr)
            col_list = ','.join(str(e) for e in listToStr)
            list_of_keys.append((col_list, key_length, len(df1), table_row_count))

    key_length_df = pd.DataFrame(data=list_of_keys, columns=['Cols_in_key', 'number_of_cols_in_keu', 'uniq_recs_on_key',
                                                             'file_total_rows'])
    key_length_df['is_primary'] = np.where(key_length_df['uniq_recs_on_key'] >= key_length_df['file_total_rows'], 'yes',
                                           'no')

    key_length_df = key_length_df.sort_values('uniq_recs_on_key', ascending=False)
    return key_length_df



if __name__ == '__main__':
    filename = sys.argv[1]
    key_len = int(sys.argv[2])
    key_length_df = findkey(filename,key_len)
    print(key_length_df.head())
    key_length_df.to_csv('key.csv', index=False)
