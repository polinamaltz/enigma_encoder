def rotor(symbol, n, reverse=False):
    sign = -1 if reverse else 1
    rotors = {1: ('AELTPHQXRU', 'BKNW', 'CMOY', 'DFG', 'IV', 'JZ', 'S'),
             2: ('FIXVYOMW', 'CDKLHUP', 'ESZ', 'BJ', 'GR', 'NT', 'A', 'Q'),
             3: ('ABDHPEJT', 'CFLVMZOYQIRWUKXSG', 'N')
             }
    if not n:
        return symbol
    for c in rotors[n]:
            if symbol in c:
                return c[(c.index(symbol)+sign)%len(c)]