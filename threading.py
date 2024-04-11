import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor
import time  # Import time module

trips_by_distance_path = r"C:\Users\DELL\Desktop\Trips_by_Distance (1).csv"
trips_full_data_path = r"C:\Users\DELL\Desktop\Trips_Full Data (1).csv"

# Load the datasets
trips_by_distance_df = pd.read_csv(trips_by_distance_path)
df=trips_by_distance_df
trips_full_data_df = pd.read_csv(trips_full_data_path)

start_time = time.time()  # Capture start time

# Fill missing values with mean for numeric columns
numeric_columns = ['Population Staying at Home', 'Population Not Staying at Home',
                   'Number of Trips', 'Number of Trips <1', 'Number of Trips 1-3',
                   'Number of Trips 3-5', 'Number of Trips 5-10', 'Number of Trips 10-25',
                   'Number of Trips 25-50', 'Number of Trips 50-100', 'Number of Trips 100-250',
                   'Number of Trips 250-500', 'Number of Trips >=500']
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

# Fill missing values with mode for categorical columns
categorical_columns = ['State FIPS', 'State Postal Code', 'County FIPS', 'County Name']
df[categorical_columns] = df[categorical_columns].fillna(df[categorical_columns].mode().iloc[0])

# Drop rows with more than 2 missing values
df = df.dropna(thresh=len(df.columns) - 2)

# Step 3: Analysis and Visualization

# Average Home Stays per 'Week of Date'
average_home_stays = df.groupby('Week')['Population Staying at Home'].mean()

# Determine the average number of trips within specific distance ranges per 'Week of Date'
# Assuming the distance range columns are 'Number of Trips <1', 'Number of Trips 1-3', etc.
distance_range_columns = ['Number of Trips 10-25', 'Number of Trips 50-100']


def calculate_average_trips_by_distance(column):
    return df.groupby('Week')[column].mean()


# Specify the number of threads (change this value as needed)
num_threads = 4
# Create ThreadPoolExecutor with specified number of threads
with ThreadPoolExecutor(max_workers=num_threads) as executor:
    # Submit tasks for each distance range column
    future_results = [executor.submit(calculate_average_trips_by_distance, column) for column in distance_range_columns]

    # Get results
    average_trips_by_distance = [future.result() for future in future_results]
end_time = time.time()  # Capture end time

# Calculate execution time
execution_time = end_time - start_time  # In seconds
print(f"Execution time: {execution_time} seconds")
# Visualization
plt.figure(figsize=(12, 6))

# Plot Average Home Stays
plt.plot(average_home_stays.index, average_home_stays.values, label='Average Home Stays', marker='o')

# Plot Average Trips by Distance
for i, column in enumerate(distance_range_columns):
    plt.plot(average_trips_by_distance[i].index, average_trips_by_distance[i].values, label=column)

# Add labels and title
plt.xlabel('Week of Date')
plt.ylabel('Average Count')
plt.title('Average Home Stays vs. Average Trips by Distance over Time')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.show()


