import pandas as pd
import numpy as np

def change(df, column):
    '''Removed the words bedroom, bhk and rk from the size column as we saw from above that we need 
    to do that and then created chart for better understanding of the values now.'''
    df[column] = df[column].astype(str).str.replace(' Bedroom', '').str.replace(' BHK', '').str.replace(' RK', '')
    return df[column]

def remove_null_values(df:pd.DataFrame):
    '''Removing the null values in the data using mean, median, 
    or a particular value, based on initial analysis.'''
    df['size'].fillna(df['size'].astype(float).median(), inplace=True)
    df['size'] = df['size'].astype(float)

    df['society'].fillna('others', inplace=True)

    df['bath'].fillna(df['bath'].astype(float).median(), inplace=True)

    df['balcony'].fillna(df['balcony'].astype(float).median(), inplace=True)

    df['location'].fillna(df['location'].mode()[0], inplace=True)

    return df


def Total_sqft_average(value):
    '''Some values in the total_sqft column are in the form of x-y so to use those columns 
    I have found the mean of these values x+y/2 and replaced the x-y with this mean.'''
    if isinstance(value, str): 
        if '-' in value:
            x, y = map(float, value.strip().split('-'))
            return (x + y) / 2
    return value


# def create_metric_map(metric_df:pd.DataFrame):
#     '''Certain values in the total_sqft column are not in sqft so to make that an easy transition 
#     I have made a dictionary containing some of the metrics, and this function helps it to be case 
#     insensitive'''
metric_df = {'metric': ['acres', 'sq. yards', 'sq. meter', 'perch', 'cents', 'guntha', 'ground'],
                 'value': [43560, 9, 10.76, 272, 435.56, 1089, 2400]}
metric_map = {metric.lower(): value for metric, value in zip(metric_df['metric'], metric_df['value'])}
    # return metric_map


def extract_numeric(s):
    '''After the data dictionary has been formed we create a function to extract the numeric values
      from our dataframe copy_df.'''
    try:
        return float(''.join(filter(str.isdigit, s)))
    except ValueError:
        return None
    

def Total_sqft_convert(value):
    '''Converts total_sqft values to a unified unit, based on the metric_map'''
    value = str(value)
    found_metric = False
    for metric_name in metric_map:
        if metric_name in value.lower():
            metric_value = metric_map[metric_name]
            numeric_value = extract_numeric(value)
            if numeric_value:
                found_metric = True
                return numeric_value * metric_value
    if not found_metric and not value.replace('.','', 1).isdigit():
        print("Warning: Unrecognized metric in 'total_sqft':", value)
    return value



def remove_skew(df, column):
    '''Removing skewdness of the data'''
    df[column]=np.log1p(df[column])