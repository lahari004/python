#Print a list of all matches ("in") fron a text
import re
txt = "Use of Python in Machine Learning"
x = re.findall("in", txt)
print(x)

