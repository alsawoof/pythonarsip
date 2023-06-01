#Untuk diambil jam pada txt kemudian di print juga diurutkan dan dihitung seberapa sering disebut.
name = input("Enter file name: ")
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)
counts = dict()

for line in fh:
    line = line.rstrip()
    if not line.startswith('From ') : 
        continue
    wds = line.split()
    time = wds[5]
    hp = time.split(':')
    hour = hp[0]
    #print(hour)
    counts[hour] = counts.get(hour, 0)+1
    
for k, v in sorted(counts.items()):
    print(k, v)
