import pandas as pd
import matplotlib.pyplot as plt

# files
df = pd.read_csv("data/eth_gas_price.csv")


# sanitization
df["Date(UTC)"] = pd.to_datetime(df["Date(UTC)"])
df["Year"] = df["Date(UTC)"].dt.year
average_per_year_wei = df.groupby("Year")["Value (Wei)"].mean()
average_per_year_gwei = average_per_year_wei / 1_000_000_000

def return_eth_gas_price():
    return average_per_year_gwei.to_dict()

# plots the average gas price per year in GWEI since the genesis data.
def plot_eth_gas_price():
    plt.figure(figsize=(10, 6))
    plt.plot(average_per_year_gwei, marker='o', color='b')
    plt.title('Average gas price (GWEI)')
    plt.xlabel('Year')
    plt.ylabel('GWEI')
    plt.grid(True)
    plt.show()

