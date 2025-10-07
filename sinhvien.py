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
        print(f"Tên sinh viên: {self.ten_sinh_vien}, Năm sinh: {self.năm_sinh}")
        print(f"Điểm: {self.diem}")
        
# sv1 = SinhVien()
# sv1.them_sinh_vien("ThanhThanh", 2004, 9)
# sv1.xuat_thong_tin_sv()
