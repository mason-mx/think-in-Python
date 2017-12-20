#!/usr/bin/env python

from time import ctime
from urllib2 import urlopen

TICKs = ('yhoo', 'cost', 'adbe', 'intc', 'fb', 'disca', 'kb', 'kbh', 'med', 'cavm', 'tsm', 'amat', 'goog', 'aapl')
#URL = 'http://quote.yahoo.com/d/quotes.csv?s=%s&f=nsj1erl1d1c1p2hgw'
URL2 = 'http://ichart.yahoo.com/table.csv?s=GOOG&a=06&b=12&c=2016&d=10&e=2&f=2017&g=d&ignore=.csv'
http://ichart.yahoo.com/table.csv?s=GE&a={date.addMonths(-2).format('MM')}&b={date.today.format('dd')}&c={date.today.format('yyyy')}&d={date.addMonths(-1).format('MM')}&e={date.today.format('dd')}&f={date.today.format('yyyy')}&g=d&ignore=.csv
#URL2 = 'https://chart.yahoo.com/c/bb/m/goog'

print '\nPrices quoted as of:%s PDT\n' % ctime()
print 'COMPANY', 'TICKER', 'CAPITAL', 'EARING PER SHARE', 'PRICE/EARING', 'PRICE', 'DATE', 'CHANGE', '%AGE', 'HIGH', 'LOW', 'YEAR RANGE'
print '-------', '------', '-------', '----------------', '------------', '-----', '----', '------', '----', '----', '---', '----------'
#u = urlopen(URL % ','.join(TICKs))
u = urlopen(URL2)

for row in u:
    print row
    #company, tick, capital, earn, ratio, price, date, chg, per, high, low, range52 = row.split(',')
    #print company, tick, capital, '%.2f' % float(earn), ratio, '%.2f' % float(price), date, chg, per, '%.2f' % float(high), '%.2f' % float(low), range52

u.close()
