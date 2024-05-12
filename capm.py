import numpy as np
import pandas as pd
import statsmodels.api as sm
import os ,sys
current_dir = os.path.dirname(os.path.abspath(__file__))
path = '/home/geo/Downloads/code/geo'
path = r'C:\Users\boonh\Downloads\code\geo'
sys.path.append(path)

if __name__ == '__main__':

    data= pd.read_csv(f'{current_dir}/data.csv')
    df = pd.DataFrame(data)
    df.dropna(axis=1,inplace=True)
    # print(df.head())

    market_returns = pd.read_csv(f'{current_dir}/data/^GSPC.csv')
    market_returns = market_returns['Close'].pct_change().dropna()
    market_returns = np.array(market_returns)
    # print(market_returns)

    for stock in df :
        asset_returns = df[stock]
        if asset_returns.isna().any() :
            continue
        
        asset_returns = asset_returns.pct_change().dropna()
        asset_returns  = np.array(asset_returns)

        # 將市場收益率作為自變量X
        X = sm.add_constant(market_returns)  # 添加常數項（截距）

        # 建立線性回歸模型
        model = sm.OLS(asset_returns, X)
        results = model.fit()

        # 輸出回歸結果
        if results.rsquared > 0.6 :
            # print(results.summary())
            print(f'stock : {stock} , alpha : {results.params[0]} , beta : {results.params[0]}')
