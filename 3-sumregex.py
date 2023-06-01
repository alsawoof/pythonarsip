import re
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "realdata3.txt"
fh = open(fname)
fr = fh.read()
ns = 0
lst = list()
numtxt = re.findall('[0-9]+',fr)
#print(numtxt)

for item in numtxt :
    #untuk mengubah list string menjadi integer
    nt = int(item)
    ns = ns+nt
print(ns)