#nhap phan so
n=int(input("Nhap so ps can tinh tong:"))
ps=[]
tong=[0,1]
for i in range (n):
    print ("Nhap phan so thu",i+1)
    s=input(" ")
    ps=s.split("/")
    ps.append(s)

#tinh tong
    ps[0]=int(ps[0])
    ps[1]=int(ps[1])
    tong[0]=tong[0]*ps[1] + tong[1]*ps[0]
    tong[1]=tong[1]*ps[1]
    a=int(tong[0])
    b=int(tong[1])
    while (a != b):
        if (a > b):
            a = a - b
        else:
            b = b - a
    ucln=a
    tong[0]//=ucln
    tong[1]//=ucln
print ("Tong",n,"phan so la:",tong[0],"/",tong[1])

