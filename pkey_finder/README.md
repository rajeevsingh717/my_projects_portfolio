# pkey_finder
FindKey is program to find the key for any CSV data file. If there is no Primary key then It will try to find the composite key.
Couple of parameters which is important for program execution

column_to_exclud - List down the columns to not include in the primary/composite key calculation. Not supported as part of command line argument.
file_name - Name of the file which will be investigated for primary/composite key findings. Supported as part of argument
cols_len_in_key - Control the maximum number of columns in a composite Key by using this arguments. Supported as part of argument

Run Command:-
python keyfinder.py cust.csv 5


