#To calculate the pay based on the input hours and rate using conditional if else.
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if h>40 :
   pay4up = (h - 40)*r*1.5
   pay40 = 40*r
   gross_pay = pay4up+pay40
   print(gross_pay)
else :
   pay4und = h*r
   print(pay4und)