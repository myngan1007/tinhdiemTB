dsmon = ["GTN", "TCC", "TDLT", "TTHCM"]
sotinchi=[2,3,3,3]

ten = []
xhb=[]
diemtb=[]
sohocsinh = int(input("Nhap so sinh vien: "))
hb=int(input("Nhap so sinh vien duoc xet hoc bong: "))

def diemTB(ten, mon, tinchi):
	#Tính điểm trung bình của hs x với số môn và tín chỉ dựa vào công thức đã cho
	x = len(mon)
	tong = 0
	diem_ren_luyen = float(input("Nhap diem ren luyen: "))
	for i in range(x):
		diemtp = "Nhap diem mon " + mon[i] + ": "
		y = float(input(diemtp))
		tong += y*tinchi[i]

	diem = tong / sum(tinchi) + 0.2*diem_ren_luyen

	return diem



def sapxep(a, b):
	#Sắp xếp theo thứ tự từ lớn xuống bé của danh sách a và b là tên của sinh viên cũng được thay đổi theo thứ tự như a
	sx = len(a)
	for i in range(0, sx):
		for j in range(i+1, sx):
			if a[j] > a[i]:
				a[i], a[j] = a[j], a[i]
				b[i], b[j] = b[j], b[i]

	return a, b

for i in range(sohocsinh):
	#Nhập điểm của sinh viên x và đưa điểm và tên của sinh viên đó vào các list tương ứng, làm tròn điểm của học sinh bằng 2 sau chữ số thâp phân
	sinhvien_x = str(input("Nhap ten sinh vien: "))
	ten.append(sinhvien_x)
	dtb = diemTB(sinhvien_x, dsmon, sotinchi)
	dtb = round(dtb, 2)
	print ('Diem trung binh cua '+' '+str(ten[i])+ ' la: ',dtb)
	diemtb.append(dtb)

sapxep(diemtb,ten) # sắp xếp điểm và tên

for i in range(sohocsinh):
	#In ra tên và điểm của sinh viên đó theo thứ tự tương ứng
	print("Thu tu cac sinh vien tu cao den thap la: ", ten[i], ": ", diemtb[i])

print("Cac em duoc hoc bong la: ", ten[0:hb]) #In ra những sinh viên được nhận học bổng
