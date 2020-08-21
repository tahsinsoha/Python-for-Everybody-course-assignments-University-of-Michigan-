hrs = input("Enter Hours:")
h = float(hrs)
rt = input("Enter rate:")
r = float(rt)

if h>40:
    reg=h*r
    otp=(h-40.0)*(r*0.5)
    ans=reg+otp
else:
    ans=h*r
    
print(ans)