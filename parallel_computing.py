import dask.dataframe as dd
import matplotlib.pyplot as plt
import time

# Path to the dataset
trips_by_distance_path = r"C:\Users\DELL\Desktop\Trips_by_Distance (1).csv"

# Define dtype specification
dtype_spec = {
    'County Name': 'object',
    'Number of Trips': 'float64',
    'Number of Trips 1-3': 'float64',
    'Number of Trips 10-25': 'float64',
    'Number of Trips 100-250': 'float64',
    'Number of Trips 25-50': 'float64',
    'Number of Trips 250-500': 'float64',
    'Number of Trips 3-5': 'float64',
    'Number of Trips 5-10': 'float64',
    'Number of Trips 50-100': 'float64',
    'Number of Trips <1': 'float64',
    'Number of Trips >=500': 'float64',
    'Population Not Staying at Home': 'float64',
    'Population Staying at Home': 'float64',
    'State Postal Code': 'object'
}

# Load the dataset with Dask and specify dtypes
trips_by_distance_ddf = dd.read_csv(trips_by_distance_path, dtype=dtype_spec)

start_time = time.time()  # Capture start time

# Fill missing values with mean for numeric columns
numeric_columns = ['Population Staying at Home', 'Population Not Staying at Home',
                   'Number of Trips', 'Number of Trips <1', 'Number of Trips 1-3',
                   'Number of Trips 3-5', 'Number of Trips 5-10', 'Number of Trips 10-25',
                   'Number of Trips 25-50', 'Number of Trips 50-100', 'Number of Trips 100-250',
                   'Number of Trips 250-500', 'Number of Trips >=500']

for col in numeric_columns:
    trips_by_distance_ddf[col] = trips_by_distance_ddf[col].fillna(trips_by_distance_ddf[col].mean())

# Fill missing values with mode for categorical columns
categorical_columns = ['State FIPS', 'State Postal Code', 'County FIPS', 'County Name']

for col in categorical_columns:
    mode_value = trips_by_distance_ddf[col].value_counts().idxmax()
    trips_by_distance_ddf[col] = trips_by_distance_ddf[col].fillna(mode_value)

# Drop rows with more than 2 missing values
trips_by_distance_ddf = trips_by_distance_ddf.dropna(thresh=len(trips_by_distance_ddf.columns) - 2)

# Define function to calculate average trips by distance
def calculate_average_trips_by_distance(column):
    return trips_by_distance_ddf.groupby('Week')[column].mean().compute()

# Define number of processors
n_processors = [10, 20]
n_processors_time = {}  # Define n_processors_time dictionary

for processor in n_processors:
    start_time = time.time()

    # Calculate average trips by distance
    average_trips_by_distance = [calculate_average_trips_by_distance(col) for col in ['Number of Trips 10-25', 'Number of Trips 50-100']]

    end_time = time.time()  # Capture end time

    # Calculate execution time
    execution_time = end_time - start_time  # In seconds
    n_processors_time[processor] = execution_time

# Print execution times for different numbers of processors
print("Execution times for different numbers of processors:")
for processor, time_taken in n_processors_time.items():
    print(f"{processor} processors: {time_taken} seconds")
