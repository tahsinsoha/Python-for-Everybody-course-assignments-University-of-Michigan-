name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
di=dict()

for line in handle:
    if  line.startswith("From:"):
        continue
    if  line.startswith("From"):
        wds=line.split()
        wds=wds[5].split(':')
        #print(wds[0])
        di[wds[0]]=di.get(wds[0],0)+1
        
ymp=list()

for k,v in di.items():
    
     t=(k,v)
     ymp.append(t)
ymp=sorted(ymp)
        
for k,v in ymp:
    print(k,v)

