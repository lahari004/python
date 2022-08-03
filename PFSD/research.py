import re
txt = "Use of python in mechine Learning"
x = re.search("^Use.*Learning$", txt)
if (x) :
    print("YES! We have a match!")
else:
    print("No Match")