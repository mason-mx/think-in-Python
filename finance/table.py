from time import ctime
from urllib2 import urlopen

col_width = []

def columnar_display(list, list_examples, pagewidth=200) :
    maxlen = 0
    '''for item in list :
        l = len(str(item))
        if l > maxlen :
            maxlen = l
    #maxlen += 1   # space it out a little more
    #print maxlen
    numcol = int(pagewidth / maxlen)'''

    i = 0
    for item in list :
        maxlen = len(str(item))
        if len(str(list_examples[i])) > maxlen:
             maxlen = len(str(list_examples[i]))
        maxlen += 1
        col_width.append(maxlen)
        print '{0:{1}}'.format(item, maxlen),
        i += 1
        if i % len(list) == 0 :
            print '\n',

list = [ 'Python Core', 'Python VTE', 'Regular Expression', 'socket',
         'tarfile', 'Testing', 'threading', 'twitter', 'unittest',
         'Upstart', 'Webkit', 'Zeitgeist' ]


columns = ['TICKER', 'CAPITAL', 'EARING/SHARE', 'PRICE/EARING', 'PRICE', 'DATE', 'CHANGE', '%AGE', 'HIGH', 'LOW', 'YEAR RANGE', 'COMPANY']
columns_examples = ['COST', '1000.00B', '100.00', '100.00', '100.00', '12/12/2017', '+100.00', '+100.00%', '1000.00', '1000.00', '1000.00 - 1000.00', 'Costco Wholesale Corporation']

columnar_display(columns, columns_examples)

TICKs = ('yhoo', 'cost', 'adbe', 'intc', 'fb', 'disca', 'kb', 'kbh', 'med', 'cavm', 'tsm', 'amat', 'goog', 'aapl')
URL = 'http://quote.yahoo.com/d/quotes.csv?s=%s&f=sj1erl1d1c1p2hgw'

u = urlopen(URL % ','.join(TICKs))

for row in u:
    #print row
    quotes = row.split(',')
    for i in range(0, len(columns)-1) :
        print '{0:{1}}'.format(quotes[i], col_width[i]),
    print '\r',

u.close()
