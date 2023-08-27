import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV files
gas_used_df = pd.read_csv('data/eth_gas_used.csv')
block_time_df = pd.read_csv('data/eth_block_time.csv')

# Convert Date(UTC) to datetime
gas_used_df['Date(UTC)'] = pd.to_datetime(gas_used_df['Date(UTC)'])
block_time_df['Date(UTC)'] = pd.to_datetime(block_time_df['Date(UTC)'])

# Group data by year and calculate the average gas usage values per second
average_gas_per_year = gas_used_df.groupby(gas_used_df['Date(UTC)'].dt.year)['Value'].mean()
average_gas_per_second_per_year = average_gas_per_year / 86400  # Divide by 86,400 seconds

# Group data by year and calculate the average eth_block_time
average_block_time_per_year = block_time_df.groupby(block_time_df['Date(UTC)'].dt.year)['Value'].mean()

# Calculate the product of average gas per second and seconds per block
results = average_gas_per_second_per_year * average_block_time_per_year

def return_eth_gas_used_per_block():
    return results.to_dict()


# gas used per block. 
def plot_eth_gas_used_per_block():
    plt.figure(figsize=(10, 6))
    plt.plot(results, marker='o', color='b')
    plt.title('Average Gas Used Per Block')
    plt.xlabel('Year')
    plt.ylabel('GAS')
    plt.grid(True)
    
    # Format y-axis labels without scientific notation
    plt.ticklabel_format(style='plain', axis='y')
    
    plt.show()


