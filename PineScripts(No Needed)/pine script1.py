# the implementation of the MACD indicator in Pine:

pip install pyplot

import matplotlib

fast = 12, 
slow = 26
fastMA = ema(close, fast)
slowMA = ema(close, slow)
macd = fastMA - slowMA
signal = sma(macd, 9)
plot(macd, color=color.blue)
plot(signal, color=color.orange)

