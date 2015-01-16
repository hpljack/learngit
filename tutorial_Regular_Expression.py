__author__ = 'liuhuiping'

#Regular Expression study

import re

if __name__ == '__main__':
    p = re.compile('[a-z]+')
    m = p.match('tempo')
    print(m.group())
    print(m.span())
    print(m.start(),m.end(),sep=',')

    # test match and search
    m = p.match(':::message')
    print(m)
    m = p.search(':::message')
    print(m.group(),m.span())

    #match example
    p1 = re.compile('...')
    m1 = p1.match('string goes here')
    if m1:
        print('Match found: ',m1.group())
    else:
        print('No match')

    p = re.compile('\d+')
    ls =p.findall('12 drummers druming, 11 pipers piping, 10 lords a leaping')
    print(ls)

    iterator = p.finditer('12 drummers druming, 11 pipers piping, 10 lords a leaping')
    for m in iterator:
        print(m.span())

    print(re.match(r'Form\s+','Formage amk'))
    print(re.match(r'Form\s+','Formage amk Thu May 12 19:12:10 1998'))