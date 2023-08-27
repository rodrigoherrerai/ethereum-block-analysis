import pandas as pd
import matplotlib.pyplot as plt

from eth_gas_used import return_eth_gas_used_per_block
from eth_gas_price import return_eth_gas_price
from eth_blocks_per_day import return_eth_blocks_per_day


def return_eth_price_per_year():
    eth_price_df = pd.read_csv("data/eth_price.csv")
    eth_price_df["Date(UTC)"] = pd.to_datetime(eth_price_df["Date(UTC)"])
    eth_price_df["Year"] = eth_price_df["Date(UTC)"].dt.year
    average_per_year = eth_price_df.groupby("Year")["Value"].mean()
    return average_per_year.to_dict()




# This is the average block value in ETH, excluding MEV. 
def average_block_value_in_eth():
    # average gas used per year. 
    gas_per_block = return_eth_gas_used_per_block()

    # average gas price per year.
    gas_price = return_eth_gas_price()

    result = {}

    for year in gas_per_block:
        result[year] = gas_per_block[year] * gas_price[year] / 1_000_000_000
    
    return result

# This is the average block value in USD, excluding MEV.
def average_block_value_in_usd():
    block_eth = average_block_value_in_eth()
    average_eth_price = return_eth_price_per_year()
    
    result = {}
    
    for year in block_eth:
        result[year] = block_eth[year] * average_eth_price[year]
    
    return result


# plots the average eth block value in eth per year.
def plot_eth_block_value_eth():
    data = average_block_value_in_eth()

    years = list(data.keys())
    values = list(data.values())

    plt.figure(figsize=(10, 6))
    plt.plot(years, values, marker='o')
    plt.title('Average Block Value in ETH (excluding MEV)')
    plt.xlabel('Year')
    plt.ylabel('ETH')
    plt.grid(True)
    plt.show()


# plots the average eth block value in eth per year.
def plot_eth_block_value_in_usd():
    data = average_block_value_in_usd()

    years = list(data.keys())
    values = list(data.values())

    plt.figure(figsize=(10, 6))
    plt.plot(years, values, marker='o')
    plt.title('Average Block Value in USD (excluding MEV)')
    plt.xlabel('Year')
    plt.ylabel('USD')
    plt.grid(True)
    plt.show()



# daily block revenue.
def plot_eth_daily_block_revenue_usd():
    block_value = average_block_value_in_usd()
    blocks_per_day = return_eth_blocks_per_day()

    result = {}

    
    for year in block_value:
        result[year] = (block_value[year] * blocks_per_day[year]) / 1_000_000
    
    years = list(result.keys())
    values = list(result.values())

    plt.figure(figsize=(10, 6))
    plt.plot(years, values, marker='o')
    plt.title('Average Daily Block Revenue (M USD)')
    plt.xlabel('Year')
    plt.ylabel('Units in Millions $USD')
    plt.grid(True)
    plt.show()



# yearly block revenue.
def plot_eth_yearly_block_revenue_usd():
    block_value = average_block_value_in_usd()
    blocks_per_day = return_eth_blocks_per_day()

    result = {}

    
    for year in block_value:
        result[year] = ((block_value[year] * blocks_per_day[year]) / 1_000_000) * 365
    
    years = list(result.keys())
    values = list(result.values())

    plt.figure(figsize=(10, 6))
    plt.plot(years, values, marker='o')
    plt.title('Yearly Block Revenue (M USD)')
    plt.xlabel('Year')
    plt.ylabel('Units in Millions $USD')
    plt.grid(True)
    plt.show()


