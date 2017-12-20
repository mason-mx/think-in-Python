#coding=utf-8
'''
import matplotlib.pyplot as plt
import matplotlib.finance as mpf
import numpy as np

ticker = ('AAPL')
start = (2016, 1, 1)
end = (2016, 2, 12)

#quotes = [2.0, 2.3, 2.6, 2.5, 2.2, 2.1, 1.8, 1.9, 2.2, 2.5, 3.7, 3.8, 3.4]

quotes = np.array(mpf.quotes_historical_yahoo_ohlc(ticker, start, end))

y = np.linspace(90, 105, len(quotes))
fig, (ax1, ax2) = plt.subplots(2, sharex=True, figsize=(8, 6))
mpf.candlestick_ohlc(ax1, quotes, width=0.6, colorup='g', colordown='r')
ax1.set_title('aapl')
ax1.set_ylabel('index level')
ax1.grid(True)
ax1.xaxis_date()
plt.bar(quotes[:, 0] - 0.25, quotes[:, 5], width=0.5)
ax2.set_ylabel('volume')
ax2.grid(True)
ax2.autoscale_view()
plt.setp(plt.gca().get_xticklabels(), rotation=30)


from matplotlib.pylab import date2num
import datetime
 
data_list = []
for dates,row in hist_data.iterrows():
    date_time = datetime.datetime.strptime(dates,'%Y-%m-%d')
    t = date2num(date_time)
    open,high,low,close = row[:4]
    datas = (t,open,high,low,close)
    data_list.append(datas)
 
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)
ax.xaxis_date()
plt.xticks(rotation=45)
plt.yticks()
plt.title("股票代码：601558两年K线图")
plt.xlabel("时间")
plt.ylabel("股价（元）")
mpf.candlestick_ohlc(ax,data_list,width=1.5,colorup='r',colordown='green')
plt.grid()
'''
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.finance as mpf

start = (2014, 5, 1)
end = (2014, 6, 30)
quotes = mpf.quotes_historical_yahoo_ohlc('^GDAXI', start, end)
#quotes = mpf.quotes_historical_yahoo(‘^GDAXI’, start, end)
quotes[:2]

fig, ax = plt.subplots(figsize=(8, 5))
fig.subplots_adjust(bottom=0.2)

print "Hello"
#use Line2d
#mpf.plot_day_summary_oclh(ax, quotes, ticksize=3, colorup=’k’, colordown=’r’)#
mpf.candlestick_ohlc(ax, quotes, width=0.6, colorup='b', colordown='r')
#mpf.candlestick(ax, quotes, width=0.6, colorup=’b’, colordown=’r’)
plt.grid(True)
ax.xaxis_date()
# dates on the x-axis
ax.autoscale_view()

plt.setp(plt.gca().get_xticklabels(), rotation=30)
#raw_input(“Press Enter to continue…”)
print "bye"
