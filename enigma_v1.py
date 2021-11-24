from reflector import *
from rotor import *

def enigma(text, ref, rot1, rot2, rot3):
    l = ''
    txt = ''.join([c for c in text.upper() if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'])
    for c in txt:
        l = l + rotor(rotor(rotor(reflector(rotor(rotor(rotor(c, rot3), rot2), rot1), ref), rot1, True), rot2, True), rot3, True)
    return l