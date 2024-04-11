import csv
from statistics import mean
import time
import matplotlib.pyplot as plt

# Function to read CSV file and return a list of dictionaries
def read_csv(filepath):
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        data = [dict(row) for row in reader]
    return data

# Function to clean and convert numeric columns
def clean_numeric_columns(data, numeric_columns):
    for row in data:
        for column in numeric_columns:
            try:
                # Convert to float if possible
                row[column] = float(row[column]) if row[column] != '' else 0.0
            except ValueError:
                # If conversion fails, set to 0.0 or another default value
                row[column] = 0.0

# Function to calculate the average of a column grouped by week
def calculate_average_by_week(data, column):
    week_sums = {}
    week_counts = {}
    for row in data:
        week = row['Week']
        value = row[column]
        if week in week_sums:
            week_sums[week] += value
            week_counts[week] += 1
        else:
            week_sums[week] = value
            week_counts[week] = 1
    # Avoid division by zero by ensuring week_counts[week] > 0
    return {week: week_sums[week] / week_counts[week] for week in week_sums if week_counts[week] > 0}

trips_by_distance_path = r"Trips_by_Distance (1).csv"
trips_by_distance_data = read_csv(trips_by_distance_path)
trips_full_data_path = r"Trips_Full Data (1).csv"
trips_full_data = read_csv(trips_full_data_path)

start_time = time.time()

# List of numeric columns to clean
numeric_columns = [
    'Population Staying at Home', 'Population Not Staying at Home', 'Number of Trips',
    'Number of Trips <1', 'Number of Trips 1-3', 'Number of Trips 3-5', 'Number of Trips 5-10',
    'Number of Trips 10-25', 'Number of Trips 25-50', 'Number of Trips 50-100', 'Number of Trips 100-250',
    'Number of Trips 250-500', 'Number of Trips >=500'
]

# Clean the numeric columns
clean_numeric_columns(trips_by_distance_data, numeric_columns)

# Calculate averages
average_home_stays = calculate_average_by_week(trips_by_distance_data, 'Population Staying at Home')
distance_range_columns = ['Number of Trips 10-25', 'Number of Trips 50-100']
average_trips_by_distance = {}
for column in distance_range_columns:
    average_trips_by_distance[column] = calculate_average_by_week(trips_by_distance_data, column)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

# Plotting
plt.figure(figsize=(12, 6))
weeks = sorted(average_home_stays.keys())
plt.plot(weeks, [average_home_stays[week] for week in weeks], label='Average Home Stays', marker='o')

for column in distance_range_columns:
    plt.plot(weeks, [average_trips_by_distance[column].get(week, 0) for week in weeks], label=column)

plt.xlabel('Week')
plt.ylabel('Average Count')
plt.title('Average Home Stays vs. Average Trips by Distance over Time')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
