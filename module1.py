import numpy as np
import pandas as pd


def read_csv():
    # Method to read the CSV file "Hospital_patients_datasets.csv" using pandas.
    # Returns: Pandas DataFrame containing the data from the CSV file.
    ds = pd.read_csv('./Hospital_patients_datasets.csv')
    
    return ds


def check_duplicates():
    ds = read_csv()
    # Method to check for duplicate rows in the DataFrame.
    # Returns: The number of duplicated rows found in the DataFrame.
    ds = ds.duplicated().sum()
    return ds


def check_null_values():
    ds = read_csv()
    # Method to check for null (missing) values in the DataFrame.
    # Returns: A pandas Series indicating the count of null values for each column in the DataFrame.
    ds.isna().sum()
    return ds



def converting_dtype():
    ds = read_csv()
    # Method to convert 'ScheduledDay' and 'AppointmentDay' columns to datetime objects.
    # Returns: DataFrame with 'ScheduledDay' and 'AppointmentDay' columns converted to datetime objects.
    ds['ScheduledDay'] = pd.to_datetime(ds.ScheduledDay).dt.date
    ds['AppointmentDay'] = pd.to_datetime(ds.AppointmentDay).dt.date
    return ds


def rename_columns():
    ds = converting_dtype()
    # Method to rename some columns in the DataFrame.
    # Returns: DataFrame with certain column names changed to new names.
    ds.rename(columns={'Hipertension' : 'Hypertension', 
                   'Handcap' : 'Handicap',
                   'SMS_received' : 'SMSReceived', 
                   'No-show' : 'NoShow'}, inplace=True)
    
    return ds


