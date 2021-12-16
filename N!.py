n = int(input("mèo méo meo mèo meo, nhập n hoặc bị hun = "))
giai_thua= 1
s=0
for i in range(n):
   giai_thua = giai_thua * (i+1)
   s= s+giai_thua
print("Giai thừa của", n, "là", giai_thua)
print("Tổng của giai thừa các giai thừa là ", s)