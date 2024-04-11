import pandas as pd
import matplotlib.pyplot as plt

trips_full_data = pd.read_csv(r"C:\Users\DELL\Desktop\Trips_Full Data (1).csv")

# Define the distance-trip categories
distance_trip_columns = ['Trips <1 Mile', 'Trips 1-3 Miles', 'Trips 3-5 Miles',
                         'Trips 5-10 Miles', 'Trips 10-25 Miles', 'Trips 25-50 Miles',
                         'Trips 50-100 Miles', 'Trips 100-250 Miles', 'Trips 250-500 Miles',
                         'Trips 500+ Miles']

# Sum the number of travelers for each distance-trip category
total_travelers_by_distance_trip = trips_full_data[distance_trip_columns].sum()

# Plot the data
plt.figure(figsize=(10, 6))
total_travelers_by_distance_trip.plot(kind='bar', color='skyblue')
plt.title('Number of Participants by Distance-Trips')
plt.xlabel('Distance-Trip Category')
plt.ylabel('Number of Participants')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
