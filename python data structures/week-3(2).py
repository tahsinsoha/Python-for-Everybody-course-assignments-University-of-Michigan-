fname = input("Enter file name: ")
fh = open(fname)
cnt=0
sm=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    cnt+=1
    t= line.find(":")
    p= line[t+2:]
    f=float(p)
    sm+=f
        
print("Average spam confidence:",sm/cnt)