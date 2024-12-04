import pandas as pd


df = pd.read_csv('Citywise_AQI.csv')

# Calculate the mean AQI
mean_aqi = df['AQI'].mean()

# Find the maximum value of PM2.5
max_pm25 = df['PM2.5'].max()

print(f'Mean AQI: {mean_aqi}')
print(f'Maximum PM2.5: {max_pm25}')

