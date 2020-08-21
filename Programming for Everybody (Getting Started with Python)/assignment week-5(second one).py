score = input("Enter Score: ")
p = float(score)

if p>1.0:
    print("ERROR")
    
elif p>=.9:
    print("A")
elif p>=.8:
    print("B")
elif p>=.7:
    print("C")
elif p>=.6:
    print("D")
else:
    print("F")