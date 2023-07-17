import pandas as pd
from datetime import datetime as date
from binance.um_futures import UMFutures
from pathlib import Path

# Define the symbol and intervals DATA COLLECTOR
symbol = "BTCUSDT"
interval = "5m"
limit = 1000
file_name = 'test1.csv'
date_start = '2023-07-10 03:00:00'

# Parcing data and collect in df
def fetch_historical_data(symbol, interval, limit, start_time, end_time):
    client = UMFutures()
    main_df = []

    while start_time < end_time:
        print(start_time)
        print(type(start_time))
        last_time = start_time + (300000 * limit)
        if last_time < end_time:
            klines = client.continuous_klines(pair=symbol,
                                              contractType='PERPETUAL',
                                              interval=interval,
                                              startTime=start_time,
                                              limit=limit)
        else:
            klines = client.continuous_klines(pair=symbol,
                                              contractType='PERPETUAL',
                                              interval=interval,
                                              startTime=start_time,
                                              endTime=end_time,
                                              limit=limit)

        df = pd.DataFrame(klines)
        start_time = df.iloc[-1, 0] + (300000)
        main_df += klines

    df = pd.DataFrame(main_df, columns=["timestamp", "open", "high", "low", "close", "volume", "close_time",
                                        "quote_asset_volume", "number_of_trades", "taker_buy_base_asset_volume",
                                        "taker_buy_quote_asset_volume", "ignore"])
    df = df.drop_duplicates()
    return df

# Save collecting data to csv fill
def save_historical_data(symbol, interval, limit, date_start, file_name):
    # Datetime object containing current date and time
    now = date.now()
    current_date = now.strftime('%Y-%m-%d %H:%M:%S')

    # Datetime to ms
    start_time = int(date.strptime(date_start, '%Y-%m-%d %H:%M:%S').timestamp() * 1000)
    end_time = int(date.strptime(current_date, '%Y-%m-%d %H:%M:%S').timestamp() * 1000)

    data = fetch_historical_data(symbol, interval, limit, start_time, end_time)
    file_path = Path('data', file_name)
    data.to_csv(file_path, index=False)
    print(f'Saved {len(data)} rows to {file_path}')
