fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    
     lx=line.rstrip()
     wds=lx.split()
     

     for wd in wds:

            
        if wd in lst:
             continue
         
        lst.append(wd)
    
lst.sort()
print(lst)