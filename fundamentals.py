import yfinance as yf
import pandas as pd
import matplotlib.pyplot as pt
from matplotlib import style
style.use('ggplot')

import os ,sys
current_dir = os.path.dirname(os.path.abspath(__file__))
path = '/home/geo/Downloads/code/geo'
path = r'C:\Users\boonh\Downloads\code\geo'
sys.path.append(path)

# # 获取股票数据
# stock = yf.Ticker("AAPL")

# # 获取基本面数据
# fundamentals = stock.info
# print(result := pd.DataFrame(fundamentals))

# result.to_csv(f'{current_dir}/fundamentals.csv',index=False)

# 获取苹果公司的数据
apple = yf.Ticker("AAPL")

# 获取财务报表
balance_sheet = apple.balance_sheet
income_statement = apple.financials
cash_flow = apple.cashflow

# 计算总资产周转率
total_assets = balance_sheet.loc['Total Assets']
total_revenue = income_statement.loc['Total Revenue']
asset_turnover_ratio = total_revenue / total_assets
print("总资产周转率:", asset_turnover_ratio)

# 绘制总资产周转率趋势图
asset_turnover_ratio.plot()
pt.title('Total Asset Turnover Ratio Over Time')
pt.xlabel('Year')
pt.ylabel('Ratio')
pt.show()