import akshare as ak

stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20150301", end_date='20260118', adjust="")
print(stock_zh_a_hist_df)
