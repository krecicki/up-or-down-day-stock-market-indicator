# up-or-down-day-stock-market-indicator
Will SPY end higher or lower? The script is 93.33% (14/15) accurate on bearish and bullish days. On neutral days, 13 times it ended Lower and only 7 times did it end Higher.
For access to the spread sheet from our testing visit https://file.io/ZluAkbpjiUA6 to download it.

# Accuracy
2024-03-07: Sentiment Bullish, SPY_End Higher - Accurate 
2024-03-11: Sentiment Bearish, SPY_End Lower - Accurate 
2024-05-23: Sentiment Bearish, SPY_End Lower - Accurate 
2024-05-24: Sentiment Bullish, SPY_End Higher - Accurate 
2024-05-29: Sentiment Bearish, SPY_End Lower - Accurate 
2024-05-09: Sentiment Bullish, SPY_End Higher - Accurate 
2024-05-14: Sentiment Bullish, SPY_End Higher - Accurate 
2024-05-15: Sentiment Bullish, SPY_End Higher - Accurate 
2024-05-20: Sentiment Bearish, SPY_End Higher - Inaccurate
2024-04-29: Sentiment Bullish, SPY_End Higher - Accurate 
2024-04-30: Sentiment Bearish, SPY_End Lower - Accurate 
2024-05-02: Sentiment Bullish, SPY_End Higher - Accurate 
2024-05-03: Sentiment Bullish, SPY_End Higher - Accurate 
2024-03-14: Sentiment Bearish, SPY_End Lower - Accurate 
2024-03-15: Sentiment Bearish, SPY_End Lower - Accurate 


# This script now considers the following
If the change in VIX (^VIX) is negative, the change in SHY (1-3 Year Treasury Bond ETF) is positive, and the change in DXY (U.S. Dollar Currency Index) is negative, the sentiment is considered "Bullish".

If the change in VIX is positive, the change in SHY is negative, and the change in DXY is positive, the sentiment is considered "Bearish".
If neither of the above conditions is met, the sentiment is considered "Neutral".

### VIX (CBOE Volatility Index)

The VIX is a measure of expected volatility in the S&P 500 index.
A lower VIX typically indicates lower expected volatility and is considered a bullish signal for the stock market.


### SHY (iShares 1-3 Year Treasury Bond ETF)

SHY tracks the performance of short-term U.S. Treasury bonds.
When SHY rises, it implies that investors are demanding higher prices for short-term bonds, which generally happens when interest rates are expected to decrease.
Lower interest rates are typically seen as bullish for the stock market.


### DXY (U.S. Dollar Index)

The DXY measures the value of the U.S. dollar against a basket of major currencies.
A declining DXY indicates a weakening U.S. dollar, which can be bullish for U.S. multinational companies and the stock market in general, as it makes their products and services more competitive in international markets.

# Google Colab 
[https://colab.research.google.com/drive/1MhtzibjBbJEnDPQGPxY3vYT9hL9sb-LW?usp=sharing](https://colab.research.google.com/drive/1MhtzibjBbJEnDPQGPxY3vYT9hL9sb-LW?usp=sharing)
