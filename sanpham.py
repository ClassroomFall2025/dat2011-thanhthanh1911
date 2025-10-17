# Bài 1
class SanPham:
    def __init__(self, ten_sp, gia, giam_gia):
        self.ten_sp = ten_sp
        self.gia = gia
        self.__giam_gia = giam_gia

    # def doc_giam_gia(self):
    #     return self.__giam_gia
    # def cap_nhat_giam_gia(self, giam_gia_moi):
    #     self.__giam_gia = giam_gia_moi

    def thue_nhap_khau(self):
        return self.gia * 0.1
    
    def get_ten_sp(self):
        return self.__ten_sp
    def set_ten_sp(self, ten_sp):
        self.__ten_sp = ten_sp

    def get_gia(self):
        return self.__gia
    def set_gia(self, gia):
        self.__gia = gia

    def get_giam_gia(self):
        return self.__giam_gia
    def set_giam_gia(self, giam_gia):
        self.__giam_gia = giam_gia
    
    def nhap_thong_tin_sp(self):
        
        self.ten_sp = input("Nhập tên sản phẩm: ")
        self.gia = float(input("Nhập giá sản phẩm: "))
        self.__giam_gia = float(input("Nhập giảm giá sản phẩm: "))
    def xuat_thong_tin_sp(self):
        print(f"Sản Phẩm{self.ten_sp} Giá: {self.gia} Giảm giá: {self.__giam_gia} Thuế nhập khẩu: {self.thue_nhap_khau()}")
    def __str__(self):
        return f"Sản Phẩm{self.ten_sp} Giá: {self.gia} Giảm giá: {self.__giam_gia} Thuế nhập khẩu: {self.thue_nhap_khau()}"



# Bài 3
    


# sp1 = SanPham("Beer", 20000, 5000)
# print(sp1.doc_giam_gia())
# sp1.xuat_thong_tin()
# print(sp1)

# sp1.cap_nhat_giam_gia(3000)
# print(sp1)