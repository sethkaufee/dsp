# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0

from numpy import ceil as ceil


def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >> donuts(4)
    'Number of donuts: 4'
    >> donuts(9)
    'Number of donuts: 9'
    >> donuts(10)
    'Number of donuts: many'
    >> donuts(99)
    'Number of donuts: many'
    """

    if count < 10:
        return 'Number of donuts: %s' % count
    else:
        return 'Number of donuts: many'

for i in [4,9,10,99]:
    print (donuts(i))

def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    if len(s)>2:
        return s[:2]+s[-2:]
    else:
        return ''
        
for i in ['spring','Hello','a','xyz']:
    print (both_ends(i))

def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """

    return s[0] + s[1:].replace(s[0], '*')
    
for i in ['babble','aardvark','google','donut']:
    print (fix_start(i))


def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    return b[0:2]+a[2:]+' '+a[0:2]+b[2:]

for i,j in [('mix', 'pod'),('dog','dinner'),('gnash','sport'),('pezzy', 'firm')]:
    print (mix_up(i,j))



def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    if len(s) > 2:
        if s[-3:] =='ing':
            return s+'ly'
        else:
            return s+'ing'
    else:
        return s
        
for i in ['hail','swiming','do']:
    print(verbing(i))



def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    
    not_find = s.find('not')    
    bad_find = s.find('bad')
    
    if not_bad == -1 and not_bad == -1:
        return s
    elif not_find < bad_find:
        s = s.replace(s[not_find:bad_find+3],'good')
        return s
    else:
        return s

for i in ['This movie is not so bad','This dinner is not that bad!','This tea is not hot','It\'s bad yet not']:
    print (not_bad(i))

    



def front_back(a, b):
    dontenut_ = """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """

    a_half = int(ceil(len(a)/2))
    b_half = int(ceil(len(b)/2))
    
    return a[:a_half]+b[:b_half]+a[a_half:]+b[b_half:]

for i,j,k in [('abcd','xy','abxcdy'),('abcde','xyz','abcxydez'),('Kitten','Donut','KitDontenut')]:
    print(front_back(i,j),k)