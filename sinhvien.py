class SinhVien:
    # Các thuộc tính
    # ten_sinh_vien = ""
    # năm_sinh = ""
    # diem = ""
    
    # Các phương thức
    def _init_(self, ten_sv, nam_sinh, diem):
        self.ten_sinh_vien = ten_sv
        self.năm_sinh = nam_sinh
        self.diem = diem
    
    def xuat_thong_tin_sv(self):
        print(f"Tên sinh viên: {self.ten_sinh_vien}, Năm sinh: {self.năm_sinh} có điểm: {self.diem}")
        
# sv1 = SinhVien()
# sv1.them_sinh_vien("ThanhThanh", 2004, 9)
# sv1.xuat_thong_tin_sv()

class SinhVienXLDL(SinhVien):
    def __init__(self, ten_sv, nam_sinh, diem, lap_trinh):
        super._init_(ten_sv, nam_sinh, diem)
        self.lap_trinh = lap_trinh

    def xuat_thong_tin_sv(self):
        # print(f"Tên sinh viên: {self.ten_sinh_vien}, Năm sinh: {self.năm_sinh} và học lập trình")
        # print(f"{SinhVien.__str__()} và học lập trình {self.lap_trinh}")
        def __str__(self):
            return f"{super().__str__()} và học lập trình {self.lap_trinh}"

    # def xuat_thong_tin_sv(self):
    #     super().xuat_thong_tin_sv()
    #     print(f"Học lập trình: {self.lap_trinh}")

sv1 = SinhVien("ThanhThanh", 2004, 9, "Python")
# sv1.xuat_thong_tin_sv()
print(sv1)