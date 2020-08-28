name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
di=dict()

for line in handle:
    if  line.startswith("From:"):
        continue
    if  line.startswith("From"):
        wds=line.split()
        di[wds[1]]=di.get(wds[1],0)+1
        
maxx=-1
word=None

for k,v in di.items():
    if v>maxx:
        maxx=v
        word=k
        
print(word,maxx)
