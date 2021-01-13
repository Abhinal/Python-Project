from pattern import pypart, pypart2, triangle, numpat, countnum

while True:
    choice = globals()[input("Type 'pypart' or 'pypart2' or 'triangle' or 'numpat' or 'countnum': ")]
    choice(int(input('Enter number of coloumns: ')))