import re

html = ''

def promo(n):
    global html
    print('zzzz')
    html += '****' + n + '****'

def other(a,b,c):
    global html
    print(a,b,c)
    html += f'@@@@{a} {b} {c} @@@####'

t = """aaaaa{{promo('aaa')}} sddsdsdsdsd {{other(12,34,4)}} XXZXXZZX"""

for start in t.split('{{'):
    stop = start.split('}}')
    print('ASASAS', stop)
    if len(stop) == 2:
        exec(stop[0])
        html += stop[1]
    else:
        html += stop[0]


print(html)