#Untuk melakukan slicing string (sehingga output : 0.8475)
text = "X-DSPAM-Confidence:    0.8475"
t = text.find('0')
pr = float(text[t:t+6])
print(pr)