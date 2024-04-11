import pandas as pd

# Paths to the datasets
trips_by_distance_path = "Trips_by_Distance.csv"
trips_full_data_path = "Trips_Full_Data.csv"

# Reading the datasets into DataFrames
trips_by_distance_df = pd.read_csv(trips_by_distance_path)
trips_full_data_df = pd.read_csv(trips_full_data_path)
# Filling missing values for numeric columns with their mean values
numeric_columns = [
    'Population Staying at Home', 'Population Not Staying at Home', 'Number of Trips',
    'Number of Trips <1', 'Number of Trips 1-3', 'Number of Trips 3-5', 'Number of Trips 5-10',
    'Number of Trips 10-25', 'Number of Trips 25-50', 'Number of Trips 50-100', 'Number of Trips 100-250',
    'Number of Trips 250-500', 'Number of Trips >=500'
]
trips_by_distance_df[numeric_columns] = trips_by_distance_df[numeric_columns].fillna(trips_by_distance_df[numeric_columns].mean())

# Filling missing values for categorical columns with their mode
categorical_columns = ['State FIPS', 'State Postal Code', 'County FIPS', 'County Name']
trips_by_distance_df[categorical_columns] = trips_by_distance_df[categorical_columns].fillna(trips_by_distance_df[categorical_columns].mode().iloc[0])
# Dropping rows with more than 2 missing values
trips_by_distance_df = trips_by_distance_df.dropna(thresh=len(trips_by_distance_df.columns) - 2)
