import pandas as pd
import numpy as np
import yfinance as yf
from matplotlib import style
style.use('ggplot')

import os ,sys
current_dir = os.path.dirname(os.path.abspath(__file__))
path = '/home/geo/Downloads/code/geo'
path = r'C:\Users\boonh\Downloads\code\geo'
sys.path.append(path)

from notification_bot.loguru_notification import loguru_notf
logger = loguru_notf(current_dir)
logger.add('download_stock_data')

if __name__ == '__main__':

    nyse = pd.read_csv(f'{current_dir}/NYSE.csv')
    amex = pd.read_csv(f'{current_dir}/AMEX.csv')
    nasdaq = pd.read_csv(f'{current_dir}/NASDAQ.csv')

    end_date = pd.Timestamp.today()  # 今天的日期
    start_date = end_date - pd.DateOffset(years=2)  # 两年前的日期

    symbols = []
    for symbol in nyse.Symbol : 
        symbols.append(symbol)
    
    for symbol in amex.Symbol : 
        symbols.append(symbol)
    
    for symbol in nasdaq.Symbol : 
        symbols.append(symbol)
    
    data = {}
    for stock in symbols :
        path = os.path.join(current_dir,f'data/{stock}.csv')
        df = yf.download(stock,start=start_date,end=end_date)
        data[f'{stock}'] = df.Close
        df.to_csv(path,index=False)
        logger.info(f'{stock} downloaded.')
    
    pd.DataFrame(data).to_csv(f'{current_dir}/data.csv',index=False)

    stock = '^GSPC'
    path = os.path.join(current_dir,f'data/{stock}.csv')
    df = yf.download(stock,start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))
    df.to_csv(path,index=False)
    logger.info(f'{stock} SP500.')

    # path = os.path.join(current_dir,'data/TWII.csv')
    # df = yf.download('^TWII',start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))
    # df.to_csv(path,index=False)