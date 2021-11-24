def sh(c, shift):
    a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return a[(a.index(c)+shift) % len(a)]