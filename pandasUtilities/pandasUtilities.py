"""
    File:           pandasUtilities.py
    Author:         Gaurav Shimpi
    Created on:     12th July, 2019
    Modified on:    15th July, 2019
    Description:    pandas Utilities contains Some extra attributes and functions which makes our work easier
                    when working with pandas and its functionality.
"""
import pandas as pd
from pandas import DataFrame


# Prints a single line, It's same as println() in other languages, by default print single empty line or "\n"
printline = lambda times=1 : print("\n" * times)

# function that counts NaN values for whole dataframe
__checkAllNaNs = lambda dataframe: dataframe.isnull().sum()
DataFrame.checkNans = __checkAllNaNs

# dropped a specific row where Total stop was NaN, Instead of doing other Logic I simply dropped 1 row
# Find row where Total_stops is NaN -> Locate index -> Drop index from Dataframe
__dropRowsWhereNone = lambda dataframe,column : dataframe.drop(dataframe[dataframe[column].isnull()].index) #, inplace= True
DataFrame.dropNans = __dropRowsWhereNone


# check total number of duplicate rows
__totalDuplicateRows = lambda dataframe : dataframe.duplicated().sum()
DataFrame.allDuplicates = __totalDuplicateRows

# From all the column names it will replace spaces to under_scores
def __remove_all_column_name_spaces(dataframe):
    dataframe.columns = dataframe.columns.str.replace(" ", "_")

DataFrame.replaceHeaderSpaces = __remove_all_column_name_spaces

# For Safely popping any column from DataFrame, If it consists that column_name
# I was facing probelm with this as running the same cell again will throw errors.
def __pop_safe(dataframe: DataFrame, column_name: str):
  try:
    return dataframe.pop(column_name)
  except:
    print("DataFrame do not consists such column : {}".format(column_name))

DataFrame.pop_safe = __pop_safe

"""
    Check all the basic information about dataset
"""
def __get_dataset_overview(dataframe):
    print("=> Shape of dataframe is\n")
    print(dataframe.shape)
    printline()

    print("=> Data types of each columns\n")
    print(dataframe.dtypes)
    printline()

    print("=> Head and tail of the dataframe is ")
    display(dataframe.head()) #https://stackoverflow.com/a/29665452 => how display works?
    display(dataframe.tail())
    printline()

    print("=> Basic statistics about this dataframe")
    display(dataframe.describe())

DataFrame.overview = __get_dataset_overview
