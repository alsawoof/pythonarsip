#To calculate the pay based on the input hours and rate using function if else.
def computepay(h, r):
    if h>40 :
        payup40 = ((h - 40)*r*1.5)+(40*r)
        return payup40
    
    else :
        payund40 = h*r
        return payund40
    
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
p = computepay(h, r)
print("Pay", p)