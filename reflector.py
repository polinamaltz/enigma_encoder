def reflector(symbol, n):
    if not n:
        return symbol
    refl = {1 : ('AY', 'BR', 'CU', 'DH', 'EQ', 'FS', 'GL', 'IP', 'JX', 'KN', 'MO', 'TZ', 'VW')}
    for c in refl[n]:
            if symbol in c:
                return c[(c.index(symbol)+1)%len(c)]