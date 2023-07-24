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


# calculate indicators
df["ema"] = calculate_ema(df)
df["rsi"] = calculate_rsi(df)
df["sar"] = calculate_psar(df)
