#Untuk menghitung banyak kata/email yang disimpan di dictionary dan dicari kata terbanyak yang dipanggil
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From ') : 
        continue
    
    words = line.split()
    mail = words[1]
#    print(mail)
#    print(mail)
    counts[mail] = counts.get(mail, 0)+1

bigcount = None
bigmail = None
for mail,count in counts.items() :
    if bigcount is None or count > bigcount:
        bigmail = mail
        bigcount = count

print(bigmail, bigcount)