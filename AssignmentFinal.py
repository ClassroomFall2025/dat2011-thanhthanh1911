import os

class NV:
    def __init__(self, ma, ho_ten, luong_co_ban):
        self.__ma_nv = ma
        self.__ho_ten = ho_ten
        self.__luong_co_ban = luong_co_ban

    def get_ma_nv(self):
        return self.__ma_nv
    def get_ho_ten(self):
        return self.__ho_ten
    def get_luong_co_ban(self):
        return self.__luong_co_ban
    
    def get_thu_nhap(self):
        return self.__luong_co_ban
    def get_thue_thu_nhap(self):
        thu_nhap = self.get_thu_nhap()
        if thu_nhap < 9000000:
            return 0
        elif thu_nhap <= 15000000:
            return thu_nhap * 0.10
        else:
            return thu_nhap * 0.12
    def xuat(self):
        print(f"NV,{self.get_ma_nv()},{self.get_ho_ten()},{self.get_luong_co_ban()},{self.get_thu_nhap()}")

class TT(NV):
    def __init__(self, ma, ho_ten, luong_co_ban, hoa_hong, doanh_so):
        super().__init__(ma, ho_ten, luong_co_ban)
        self.__hoa_hong = hoa_hong
        self.__doanh_so = doanh_so
    def get_thu_nhap(self):
        return self.get_luong_co_ban() + self.__hoa_hong * self.__doanh_so
    def xuat(self):
        print(f"TT,{self.get_ma_nv()},{self.get_ho_ten()},{self.get_luong_co_ban()},{self.__hoa_hong},{self.__doanh_so},{self.get_thu_nhap()}")

class TP(NV):
    def __init__(self, ma, ho_ten, luong_co_ban, luong_trach_nhiem):
        super().__init__(ma, ho_ten, luong_co_ban)
        self.__luong_trach_nhiem = luong_trach_nhiem
    def get_thu_nhap(self):
        return self.get_luong_co_ban() + self.__luong_trach_nhiem
    def xuat(self):
        print(f"TP,{self.get_ma_nv()},{self.get_ho_ten()},{self.get_luong_co_ban()},{self.__luong_trach_nhiem},{self.get_thu_nhap()}")

# Danh sách nhân viên
danh_sach_nv = []

# === CHỨC NĂNG 1: Nhập và Lưu TXT ===
def cn1():
    print("Chức năng 1: Nhập danh sách nhân viên từ bàn phím. Lưu thông tin nhân viên vào file.")
    so_luong_nv = int(input("Nhập số lượng nhân viên cần lưu:"))
    for i in range(so_luong_nv):
        print(f"Nhập thông tin nhân viên thứ {i+1}:")
        vitri = input("Vị trí nhân viên (NV/TT/TP):").upper()
        ma = input("Mã nhân viên: ")
        ho_ten = input("Họ tên nhân viên: ")
        luong_co_ban = float(input("Lương cơ bản: "))

        if vitri == "NV":
            nv = NV(ma, ho_ten, luong_co_ban)
            line = f"NV,{ma},{ho_ten},{luong_co_ban}\n"
        elif vitri == "TT":
            doanh_so = float(input("Doanh số bán hàng: "))
            hoa_hong = float(input("Tỉ lệ hoa hồng (%): ")) / 100
            nv = TT(ma, ho_ten, luong_co_ban, hoa_hong, doanh_so)
            line = f"TT,{ma},{ho_ten},{luong_co_ban},{hoa_hong},{doanh_so}\n"
        elif vitri == "TP":
            luong_trach_nhiem = float(input("Phụ cấp trách nhiệm: "))
            nv = TP(ma, ho_ten, luong_co_ban, luong_trach_nhiem)
            line = f"TP,{ma},{ho_ten},{luong_co_ban},{luong_trach_nhiem}\n"
        else:
            print("Vị trí nhân viên không hợp lệ. Vui lòng nhập lại.")
            continue

        danh_sach_nv.append(nv)

        with open("nhanvien.txt", "a", encoding="utf-8") as f:
            f.write(line)

    print(f"Đã lưu {so_luong_nv} nhân viên vào file nhanvien.txt.")

# === CHỨC NĂNG 2: Đọc file TXT và hiển thị ===
def cn2():
    print("Chức năng 2: Đọc thông tin nhân viên từ file và xuất danh sách nhân viên")
    if not os.path.exists("nhanvien.txt"):
        print("Chưa có file dữ liệu.")
        return
    
    danh_sach_nv.clear()
    with open("nhanvien.txt", "r", encoding="utf-8") as f:
        for line in f:
            data = line.strip().split(",")
            loai = data[0]
            if loai == "NV":
                nv = NV(data[1], data[2], float(data[3]))
            elif loai == "TT":
                nv = TT(data[1], data[2], float(data[3]), float(data[4]), float(data[5]))
            elif loai == "TP":
                nv = TP(data[1], data[2], float(data[3]), float(data[4]))
            else:
                continue
            danh_sach_nv.append(nv)
    
    print("Danh sách nhân viên trong file:")
    for nv in danh_sach_nv:
        nv.xuat()

# === CÁC HÀM KHÁC GIỮ NGUYÊN ===
def cn3():
    print("Chức năng 3: Tìm và hiển thị nhân viên theo mã nhập từ bàn phím.")
    ma = input("Nhập mã nhân viên cần tìm:")
    for nv in danh_sach_nv:
        if nv.get_ma_nv() == ma:
            print("Thông tin nhân viên:")
            nv.xuat()
            return
    print("Không tìm thấy nhân viên với mã đã nhập.")

def cn4():
    print("Chức năng 4: Xóa nhân viên theo mã nhập từ bàn phím. Cập nhật file dữ liệu.")
    pass

def cn5():
    print("Chức năng 5: Cập nhật thông tin nhân viên theo mã nhập từ bàn phím và ghi thay đổi vào file.")
    pass

def cn6():
    print("Chức năng 6: Tìm các nhân viên theo khoảng lương nhập từ bàn phím.")
    luong_min = float(input("Nhập mức lương tối thiểu: "))
    luong_max = float(input("Nhập mức lương tối đa: "))
    print(f"Các nhân viên có khoảng lương: {luong_min} - {luong_max}")
    for nv in danh_sach_nv:
        if luong_min <= nv.get_thu_nhap() <= luong_max:
            nv.xuat()

def cn7():
    print("Chức năng 7: Sắp xếp nhân viên theo họ và tên.")
    danh_sach_nv.sort(key=lambda nv: nv.get_ho_ten())
    for nv in danh_sach_nv:
        nv.xuat()

def cn8():
    print("Chức năng 8: Sắp xếp nhân viên theo thu nhập.")
    danh_sach_nv.sort(key=lambda nv: nv.get_thu_nhap(), reverse=True)
    for nv in danh_sach_nv:
        nv.xuat()

def cn9():
    print("Chức năng 9: Xuất 5 nhân viên có thu nhập cao nhất.")
    danh_sach_nv.sort(key=lambda nv: nv.get_thu_nhap(), reverse=True)
    so_luong = min(5, len(danh_sach_nv))
    for i in range(so_luong):
        danh_sach_nv[i].xuat()

def cn10():
    print("Chức năng 10: Thoát chương trình.")
    print("Kết thúc chương trình.")