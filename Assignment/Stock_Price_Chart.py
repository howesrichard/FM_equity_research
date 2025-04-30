
# Stock Price Chart for Bendigo Bank (BEN.AX) from 2020-04-27 to 2025-04-27

import yfinance as yf
Bendigo = yf.download(
    tickers = 'BEN.AX', 
    start='2020-04-27', 
    end='2025-04-27'
    )
Bendigo
Bendigo['Close'].plot()






#history of ASX from 2020-04-27 to 2025-04-27

ASX200 = yf.download(
    tickers = '^AXJO', 
    start='2020-04-27', 
    end='2025-04-27'
    )
ASX200
ASX200['Close'].plot()








