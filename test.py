from time import gmtime, strftime, time
from rotor import *
from reflector import *
from enigma import *

with open("pairs", "r") as f:
	pairs = f.read()
with open("text.txt", "r") as f:
	text = f.read()
encoded_text = enigma(text, 1, 1, 0, 2, 0, 3, 0, pairs)
path = "enigma_result_" + strftime("%Y-%m-%d_%H-%M-%S", gmtime()) + ".txt"
f = open(path, "w")
f.write(encoded_text)
f.close()