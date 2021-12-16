'''
n=int(input("Nhap so nguyen n:"))
s=0
for i in range (1,n+1):
    if (i%2!=0):
        s += i
print ("Tong",n," so nguyen le la: ",s)
'''
n = int(input('Nhap n: '))
s1=0
s2=0
i=0
for i in range(1,n+1):
    if (i%2!=0):
        s1 += i
    elif (i % 2 == 0):
       s2+=i
print ("Tong cac so nguyen le la: ",s1)
print('Tong cac so nguyen chan la: ',s2)


