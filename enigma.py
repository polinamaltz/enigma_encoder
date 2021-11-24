from reflector import *
from rotor import *
from sh import *
from comm import *

def enigma(text, ref, rot1, shift1, rot2, shift2, rot3, shift3, pairs=""):
    l = ''
    txt = ''.join([c for c in text.upper() if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'])
    txt = comm(txt, pairs)
    if not txt:
        return "Извините, невозможно произвести коммутацию"
    dc = {1 : 17, 2 : 5, 3 : 22}
    for c in txt:
        shift3 = (shift3 + 1) % 26
        if shift2 == dc[rot2] - 1: 
            shift2 = (shift2 + 1) % 26
            shift1 = (shift1 + 1) % 26
        if shift3 % 26 == dc[rot3]: 
            shift2 = (shift2 + 1) % 26
        c = sh(rotor(sh(c,shift3), rot3), -shift3)
        c = sh(rotor(sh(c,shift2), rot2), -shift2)
        c = sh(rotor(sh(c,shift1), rot1), -shift1)
        c = reflector(c, ref)
        c = sh(rotor(sh(c,shift1), rot1, True), -shift1)
        c = sh(rotor(sh(c,shift2), rot2, True), -shift2)
        c = sh(rotor(sh(c,shift3), rot3, True), -shift3)
        l = l + c
    l = comm(l, pairs)
    return l if l else "Извините, невозможно произвести коммутацию"