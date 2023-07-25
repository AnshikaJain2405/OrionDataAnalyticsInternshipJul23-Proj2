import pandas as pd

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
    if '-' in value:
        x, y = map(float, value.strip().split('-'))
        return (x + y) / 2
    return value

