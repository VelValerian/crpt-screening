from binance.um_futures import UMFutures
import pandas as pd
import os
import time
import data.data_collector as data_coll

# Define the symbol and intervals DATA COLLECTOR
symbol = "BTCUSDT"
interval = "5m"
limit = 1000
file_name = 'BTCUSDT_5m_20230710.csv'
date_start = '2023-07-10 03:00:00'

# Check if the file exists, otherwise call data_collector to fetch and save the data
if os.path.isfile(file_name):
    print(f"{file_name} already exists. Proceeding with the analysis...")
else:
    while not data_coll.save_historical_data(symbol, interval, limit, date_start, file_name):
        print(f"Waiting for {file_name} to be saved...")
        time.sleep(10)

