import sys
largest = -sys.maxsize
smallest = sys.maxsize
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        t=int(num)
        if t>largest:
            largest=t
        if t<smallest:
            smallest=t
       # print(num)
       
    except:
        print("Invalid input")
        continue
        
        
print("Maximum is", largest)
print("Minimum is", smallest)