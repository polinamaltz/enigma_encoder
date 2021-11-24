from time import gmtime, strftime, time
from rotor import *
from reflector import *
from enigma import *

encoded_text = enigma("Attitude is a little thing that makes a BIG difference.", 1, 1, 2, 3)
path = "enigma_result_" + strftime("%Y-%m-%d_%H-%M-%S", gmtime()) + ".txt"
f = open(path, "w")
f.write(encoded_text)
f.close()