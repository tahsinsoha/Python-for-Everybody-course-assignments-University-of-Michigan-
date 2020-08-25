text = "X-DSPAM-Confidence:    0.8475"
t= text.find(":")
p= text[t+2:]
f=float(p)
print(f)