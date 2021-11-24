def comm(l, pairs):
    if not pairs:
        return l
    dc = {}
    pairs = pairs.upper().split(' ')
    for c in pairs:
        if c[0] in dc.keys() or c[1] in dc.values() or c[1] in dc.keys() or c[0] in dc.values():
            return ""
        else:
            dc[c[0]] = c[1]
    ll = ""
    for c in l:
        if c in dc.keys():
            ll += dc[c]
        elif c in dc.values():
            ll += list(dc.keys())[list(dc.values()).index(c)]
        else:
            ll += c
    return ll