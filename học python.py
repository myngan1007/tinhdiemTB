
dsmon = ["GTN", "TCC", "TDLT", "TTHCM"]
sotinchi=[2,3,3,2]

ten = []
sohocsinh = int(input("Nhap so luong sinh vien: "))
xhb=int(input("Nhap so sinh vien duoc xet hoc bong: "))

def diemTB(ten, mon, tinchi):
	x = len(mon)
	tong = 0
	diem_ren_luyen = float(input("Nhap diem ren luyen: "))
	for i in range(x):
		diemtp = "Nhap diem mon " + mon[i] + ": "
		y = float(input(diemtp))
		tong += y*tinchi[i]

	diem = tong / sum(tinchi) + 0.2*diem_ren_luyen
	format(diem, '.2f')
	return diem

dsdtb=[]
diem_va_sv = {}
for i in range(sohocsinh):
	hocsinh_x = input("Nhap ten sv: ")
	ten.append(hocsinh_x)
	dtb = diemTB(hocsinh_x, dsmon, sotinchi)
	print("Diem trung binh la: ",dtb)
