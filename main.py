from eth_gas_used import plot_eth_gas_used_per_block
from eth_gas_price import plot_eth_gas_price
from eth_blocks_per_day import plot_eth_blocks_per_day
from eth_block_value import plot_eth_block_value_in_usd, plot_eth_block_value_eth, plot_eth_daily_block_revenue_usd, plot_eth_yearly_block_revenue_usd


def main():
    plot_eth_yearly_block_revenue_usd()
    plot_eth_daily_block_revenue_usd()
    plot_eth_block_value_eth()
    plot_eth_block_value_in_usd()
    plot_eth_blocks_per_day()
    plot_eth_gas_used_per_block()
    plot_eth_gas_price()



if __name__ == "__main__":
    main()