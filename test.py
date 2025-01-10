import re

def promo(n):
    print('zzzz')
    return('****', n, '****')

t = """aaaaa{{promo('aaa')}} sddsdsdsdsd"""

pattern = re.compile("""\\{\\{([a-zA-Z0-9_'\\(\\)]*)\\}\\}[.]*""")

for match in pattern.findall(t):
    print()
    print(exec(match))