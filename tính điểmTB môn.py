
mon = ["Tieng anh","Lap trinh", "Toan cao cap", "Kinh te vi mo"]
tc = [5, 3, 3, 3]
dsdiem = dssv = dsdiemTB = []
TB = 0
#nhập tên
def nhapten():
    ten = input("Ten sinh vien: ")
    dssv.append(ten)

#tính điểm trung bình
def tinhdiemTB(mon,tc):
    tongdiem = 0
    drl = int(input("Diem ren luyen: "))
    for i in range(len(mon)):
        diem = float(input("Diem " + mon[i] + ": "))
        dsdiem.append(diem)
        tongdiem += diem*tc[i]
    diemTB = round(tongdiem/sum(tc) + 0.2*drl, 2)
    dsdiemTB.append(diemTB)
    return (diemTB)

n = int(input("So sinh vien: "))
m = int(input("So sinh vien nhan hoc bong: "))

for i in range (n):
    print (i+1, end=".")
    nhapten()
    TB = tinhdiemTB(mon,tc)
    print ("Diem trung binh: ", TB)
    print("-"*100)


#tìm những bạn nhận học bổng




















