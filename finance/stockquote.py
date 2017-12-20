from urllib2 import urlopen
url = 'http://quote.yahoo.com/d/quotes.csv?s=googl&f=sl1d1c1p2hgwvj1ern'
u = urlopen(url, 'r')
for row in u:
    print row
u.close()
