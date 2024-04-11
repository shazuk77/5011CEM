import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Load datasets
trips_by_distance = pd.read_csv(r"C:\Users\DELL\Desktop\Trips_by_Distance (1).csv")
trips_full_data = pd.read_csv(r"C:\Users\DELL\Desktop\Trips_Full Data (1).csv")

# 1. Determine the Number of People Staying at Home and Their Travel Distances

# Calculate average number of people staying at home per week
avg_people_at_home = trips_by_distance.groupby('Week')['Population Staying at Home'].mean()

# Calculate average distance people travel when not at home
# Adjust column name for average travel distances calculation
avg_travel_distances = trips_by_distance.groupby('Week')['Number of Trips 10-25'].mean()

# Visualize using histograms
plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1)
avg_people_at_home.plot(kind='bar', color='blue')
plt.title('Average People Staying at Home per Week')
plt.xlabel('Week')
plt.ylabel('Average People')

plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 2)
avg_travel_distances.plot(kind='bar', color='green')
plt.title('Average Travel Distance when Not at Home per Week')
plt.xlabel('Week')
plt.ylabel('Average Distance (miles)')
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))  # Set x-axis ticks to integers

plt.tight_layout()
plt.show()

# 2. Identify Dates with Specific Trip Counts and Compare Trip Ranges

# Filter data for > 10,000,000 people conducting 10-25 trips
df_10_25_trips = trips_by_distance[(trips_by_distance['Number of Trips 10-25'] > 10000000)]

# Filter data for > 10,000,000 people conducting 50-100 trips
df_50_100_trips = trips_by_distance[(trips_by_distance['Number of Trips 50-100'] > 10000000)]

# Visualize using scatter plots
plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1)
plt.scatter(range(len(df_10_25_trips)), df_10_25_trips['Number of Trips 10-25'], color='red')
plt.title('Dates with >10,000,000 People Conducting 10-25 Trips')
plt.xlabel('Distance')
plt.ylabel('Number of Trips')

plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 2)
plt.scatter(range(len(df_50_100_trips)), df_50_100_trips['Number of Trips 50-100'], color='blue')
plt.title('Dates with >10,000,000 People Conducting 50-100 Trips')
plt.xlabel('Distance')
plt.ylabel('Number of Trips')

plt.tight_layout()
plt.show()
