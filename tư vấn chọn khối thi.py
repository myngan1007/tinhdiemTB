mon = ["Toan", "Lý", "Hoa", "Sinh", "Su", "Dia", "Van", "Anh"]
ds = []
dsdiem = []
#nhapdiem
for i in range(len(mon)):
    nhapdiem=float(input("Diem mon "+mon[i] + ":" + " "))
    if nhapdiem <= 10:
        ds.append(nhapdiem)
    else:
        nhapdiem = float(input("Nhap sai! Hay nhap lai!" + "Diem mon"+" " + mon[i] + ":" + " "))
        print(ds)


#diemTBtungkhoi
def khoi(a, b, c):
    tong = a+b+c
    return tong
A = khoi(ds[0], ds[1], ds[2])
B = khoi(ds[0], ds[2], ds[3])
C = khoi(ds[6], ds[5], ds[4])
D = khoi(ds[0], ds[6], ds[7])
tohop=[["A", A], ["B", B],["C", C], ["D", D]]
for i in (tohop):
    print("Diem khoi", i[0], ":",  i[1])


#chon to hop co diem cao nhat
max = 0
n = -1
for i in (tohop):
    if i[1] > max:
        max = i[1]
        n += 1
print("Ban nen thi khoi", tohop[n])










