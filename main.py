import pandas as pd
from pathlib import Path
import time
import data.data_collector as data_coll

# Define the symbol and intervals DATA COLLECTOR
symbol = "BTCUSDT"
interval = "5m"
limit = 1000
file_name = 'BTCUSDT_5m_20230101.csv'
date_start = '2023-01-01 03:00:00'
file_path = Path('data', file_name)

# Check if the file exists, otherwise call data_collector to fetch and save the data
if Path.is_file(file_path):
    print(f"{file_name} already exists.")
else:
    while not data_coll.save_historical_data(symbol, interval, limit, date_start, file_name):
        print(f"Waiting for {file_name} to be saved...")
        time.sleep(10)
        break

# # Set input parameters
# balance = 1000
# position_rate = 0.02
# ema_period = 200
# rsi_period = 14
#
# # Set initial parameters
# position_size = balance * position_rate
# open_position = None
# win_trades = 0
# loss_trades = 0
# profit = 0

# Load the data
df = pd.read_csv(f'data/{file_name}')

# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

print(df)