def computepay(h,r):
    if h>40:
        rp=h*r
        op=1.5*r*(h-40)
        calculated=rp+op
        return calculated
    else:
        calculated=h*r
        return calculated



hrs = input("Enter Hours:")
h=float(hrs)
rt= input('enter rate per hour')
r=float(r)

p= computepay(h,r)
print("Pay",p)
print('yo')
