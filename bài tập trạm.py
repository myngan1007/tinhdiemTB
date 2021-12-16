A = []

row = int(input("So tram ma ban muon nhap la: "))
colum = row

for i in range(0, row):
	new = []
	for j in range(0, colum):
		if i==j:
			new.append(0)
		elif i >= 1 and j < i:
			new.append(A[j][i])
		else:
			print("Tram", i+1, "va", j+1, "la: ", end='')
			value = int(input())
			new.append(value)
	A.append(new)

for i in A:
	print(i)

n = int(input("So tram ma ban muon xuat du lieu la: "))
for i in range(n):
	print(A[i])
    