from binance.um_futures import UMFutures
import pandas as pd
from pathlib import Path
import time
import data.data_collector as data_coll

# Define the symbol and intervals DATA COLLECTOR
symbol = "BTCUSDT"
interval = "5m"
limit = 1000
file_name = 'BTCUSDT_5m_20230601.csv'
date_start = '2023-06-01 03:00:00'
file_path = Path('data', file_name)

# Check if the file exists, otherwise call data_collector to fetch and save the data
if Path.is_file(file_path):
    print(f"{file_name} already exists.")
else:
    while not data_coll.save_historical_data(symbol, interval, limit, date_start, file_name):
        print(f"Waiting for {file_name} to be saved...")
        time.sleep(10)
        break

