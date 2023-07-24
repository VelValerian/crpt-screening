import pandas as pd
import ta as ta
from main import ema_period, rsi_period, df


def calculate_rsi(df: pd.DataFrame, period: int = rsi_period) -> pd.Series:
    """
    Calculates the RSI (Relative Strength Index) of a given DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame with the OHLC data.
    period (int): The period to use for the RSI calculation.

    Returns:
    pd.Series: The RSI values.
    """
    delta = df["close"].diff()
    up = delta.clip(lower=0)
    down = -delta.clip(upper=0)
    avg_gain = up.rolling(period).mean()
    avg_loss = down.rolling(period).mean().abs()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi


def calculate_ema(df: pd.DataFrame, period: int = ema_period) -> pd.Series:
    """
    Calculates the EMA (Exponential Moving Average) of a given DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame with the OHLC data.
    period (int): The period to use for the EMA calculation.

    Returns:
    pd.Series: The EMA values.
    """
    ema = df["close"].ewm(span=period, adjust=False).mean()
    return ema


def calculate_psar(df: pd.DataFrame) -> pd.Series:
    """
    Calculates the PSAR (Parabolic SAR) of a given DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame with the OHLC data.

    Returns:
    pd.Series: The PSAR values.
    """
    psar_indicator = ta.trend.PSARIndicator(high=df["high"], low=df["low"], close=df["close"])
    psar = psar_indicator.psar()
    return psar

def calculate_obv(df: pd.DataFrame) -> pd.Series:
    obv_indicator = ta.volume.OnBalanceVolumeIndicator(close=df['close'], volume=df['volume'])
    obv = obv_indicator.on_balance_volume()
    return obv

def calculate_ad_line(df: pd.DataFrame) -> pd.Series:
    acc_dis_indicator = ta.volume.AccDistIndexIndicator(high=df["high"], low=df["low"],
                                                        close=df['close'], volume=df['volume'])
    ad_line = acc_dis_indicator.acc_dist_index()
    return ad_line

def calculate_aroon_up(df: pd.DataFrame) -> pd.Series:
    aroon_indicator = ta.trend.AroonIndicator(high=df["high"], low=df["low"])
    dataroon_up = aroon_indicator.aroon_up()
    return dataroon_up

def calculate_aroon_down(df: pd.DataFrame) -> pd.Series:
    aroon_indicator = ta.trend.AroonIndicator(high=df["high"], low=df["low"])
    aroon_down = aroon_indicator.aroon_down()
    return aroon_down

# calculate indicators
df["ema"] = calculate_ema(df)
df["rsi"] = calculate_rsi(df)
df["sar"] = calculate_psar(df)
df["obv"] = calculate_obv(df)
df["ad_line"] = calculate_ad_line(df)
df["dataroon_up"] = calculate_aroon_up(df)
df["aroon_down"] = calculate_aroon_down(df)