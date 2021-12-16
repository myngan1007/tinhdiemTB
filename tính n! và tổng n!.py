s=0
gt=1
#tinhgiaithua
n=int(input("Nhap so can tinh giai thua:" + " "))
for i in range(1,n+1):
    gt=gt*i
print (n,"!", "=", gt)
#tinhtonggiaithua
def giaithua(i):
    if i==0:
        return 1
    else:
        return i*giaithua(i-1)
s=0
n=int(input("Nhap n:" +" "))
for i in range (1,n+1):
    j=giaithua(i)
    s+=j
print ("Tong n giai thua la:" +" " , s)