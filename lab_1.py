import pandas as pd
import numpy as np
# reading the csv file for operations:
df = pd.read_csv('AQI_Data.csv') 

# a) Displaying the first 8 rows :
print("First 8 rows of the AQI Data:")
print(df.head(8))

# b) Displaying the last 5 rows : 
print("Last 5 rows of the AQI Data:")
print(df.tail(5))

# show dtype and number of nopn null values in each column :
print("showing the Data Type of and number of not null rows:")
print(df.info())

# Compute mean of AQI : 
AQI_mean = np.mean(df['AQI'])

# Compute max of PM2.5 : 
PM25_maximum = np.max(df['PM2.5'])

# Compute min of PM10 : 
PM10_minimum = np.min(df['PM10'])

#printing the values :
print("Mean of AQI:", AQI_mean)
print("Max of PM2.5:", PM25_maximum)
print("Min of PM10:", PM10_minimum)