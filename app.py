import yfinance as yf

# Define the ticker symbols
vix_ticker = '^VIX'
shy_ticker = 'SHY'
dxy_ticker = 'DX-Y.NYB'

# Fetch the data for VIX, SHY, and DXY
vix_data = yf.Ticker(vix_ticker)
shy_data = yf.Ticker(shy_ticker)
dxy_data = yf.Ticker(dxy_ticker)

vix_hist = vix_data.history(period='5d')
shy_hist = shy_data.history(period='5d')
dxy_hist = dxy_data.history(period='5d')

# Calculate the change in VIX, SHY, and DXY
vix_change = vix_hist['Close'].iloc[-1] - vix_hist['Close'].iloc[-2]
print(vix_change)

shy_change = shy_hist['Close'].iloc[-1] - shy_hist['Close'].iloc[-2]
print(shy_change)

try:
    dxy_change = dxy_hist['Close'].iloc[-1] - dxy_hist['Close'].iloc[-2]
except IndexError:
    dxy_change = 0

print(dxy_change)

# Determine if the day is bullish or bearish based on VIX, SHY, and DXY
sentiment = 'Neutral'

if vix_change < 0 and shy_change > 0 and dxy_change < 0:
    sentiment = 'Bullish'
elif vix_change > 0 and shy_change < 0 and dxy_change > 0:
    sentiment = 'Bearish'

print(f'The market sentiment for the day is: {sentiment}')
