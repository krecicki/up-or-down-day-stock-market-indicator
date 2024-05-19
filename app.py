'''
This script now considers the following:
If the VIX is down and SHY is up (implying lower interest rates) and DXY is down, it suggests a bullish sentiment.
Conversely, if the VIX is up and SHY is down and DXY is up, it indicates a bearish sentiment.
The script will print the market sentiment for the day as “Bullish,” “Bearish,” or “Neutral” if the conditions do not match either bullish or bearish criteria. 
'''
import yfinance as yf
from datetime import datetime, timedelta

# Define the ticker symbols
vix_ticker = '^VIX'
shy_ticker = 'SHY'
dxy_ticker = 'DX-Y.NYB'

# Fetch the data for VIX and SHY
vix_data = yf.Ticker(vix_ticker)
shy_data = yf.Ticker(shy_ticker)

vix_hist = vix_data.history(period='2d')
shy_hist = shy_data.history(period='2d')

# Calculate the change in VIX and SHY
vix_change = vix_hist['Close'].iloc[-1] - vix_hist['Close'].iloc[-2]
shy_change = shy_hist['Close'].iloc[-1] - shy_hist['Close'].iloc[-2]

# Fetch the data for DXY and handle errors
try:
    dxy_data = yf.Ticker(dxy_ticker)
    dxy_hist = dxy_data.history(period='7d')

    # Get the current weekday
    today = datetime.today().weekday()

    # Find the index of the last Friday's data
    last_friday = (datetime.today() - timedelta(days=today + 3)).date()
    last_friday_index = dxy_hist.index.get_loc(last_friday, method='ffill')

    # Calculate the change in DXY
    if today == 0:  # Monday
        dxy_change = dxy_hist['Close'].iloc[-1] - dxy_hist['Close'].iloc[last_friday_index]
    else:
        dxy_hist = dxy_data.history(period='2d')
        dxy_change = dxy_hist['Close'].iloc[-1] - dxy_hist['Close'].iloc[-2]
except:
    dxy_change = 0  # Set dxy_change to 0 if an error occurs

# Determine if the day is bullish or bearish based on VIX, SHY, and DXY
sentiment = 'Neutral'
if vix_change < 0 and shy_change > 0 and dxy_change < 0:
    sentiment = 'Bullish'
elif vix_change > 0 and shy_change < 0 and dxy_change > 0:
    sentiment = 'Bearish'

print(f'The market sentiment for the day is: {sentiment}')
