def computepay(h,r):
    if h>40:
        reg=h*r
        otp=(h-40.0)*(r*0.5)
        xp=reg+otp
    else:
        xp=h*r
    return xp

hrs = input("Enter Hours:")
rt = input("Enter rate:")
h= float(hrs)
r=float(rt)
p = computepay(h,r)
print("Pay",p)