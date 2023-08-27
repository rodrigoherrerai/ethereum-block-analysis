import pandas as pd
import matplotlib.pyplot as plt


# Load data from CSV file
block_time_df = pd.read_csv('data/eth_block_time.csv')


# Convert Date(UTC) to datetime
block_time_df['Date(UTC)'] = pd.to_datetime(block_time_df['Date(UTC)'])

# Calculate the number of blocks per day
block_time_df['Blocks per Day'] = 86400 / block_time_df['Value']

# Group data by year and calculate the average number of blocks per day
average_blocks_per_day_per_year = block_time_df.groupby(block_time_df['Date(UTC)'].dt.year)['Blocks per Day'].mean()

def return_eth_blocks_per_day():
    return average_blocks_per_day_per_year.to_dict()

# plots the average number of blocks per day per year.
def plot_eth_blocks_per_day():
    plt.figure(figsize=(10, 6))
    plt.plot(average_blocks_per_day_per_year, marker='o', color='b')
    plt.title('Average Number of Blocks Per Day')
    plt.xlabel('Year')
    plt.ylabel('BLOCKS')
    plt.grid(True)
    plt.show()

