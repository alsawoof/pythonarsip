fname = input("Enter file name: ")
fh = open(fname)
avcon = 0
count = 0
lfs = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    sp = line[20:]
    lf = float(sp)
    count = count+1
    #print(lf)
    lfs = lfs + lf 
#print("lf sum = ", lfs)

avcon = lfs/count
print("Average spam confidence:", avcon)
#print("Line count : ", count)
#print("Done")