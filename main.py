a=input()
b=input()
c=a
d=b
f=[]
while True:
    if d in a:
        print(a+"".join(f),sep="")
        break
    else:
        f.insert(0,d[len(d)-1])
        d=d.replace(d[len(d)-1],"")
