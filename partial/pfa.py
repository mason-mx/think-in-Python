import functools

def say(man, words):
     print 'say', words, 'to', man

say('boss', 'hello')
say2boss = functools.partial(say, 'boss')
say2boss('good morning!')
