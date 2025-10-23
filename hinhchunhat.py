class ChuNhat:
    def __init__(self, chieudai, chieurong):
        self.chieudai = chieudai
        self.chieurong = chieurong

    def tinh_chuvi(self):
        return 2 * (self.chieudai + self.chieurong)
    def tinh_dientich(self):
        return self.chieudai * self.chieurong

    def xuat(self):
        print(f"Chiều dài hình chữ nhật:{self.chieudai}")
        print(f"Chiều rộng hình chữ nhật:{self.chieurong}")
        print(f"Diện tích hình chữ nhật:{self.tinh_dientich()}")

    # def __str__(self):
    #     return f"Chiều dài: {self.chieudai}, Chiều rộng: {self.chieurong}, Diện tích: {self.tinh_dientich()}, Chu vi: {self.tinh_chuvi()}"
class HinhVuong(ChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)
        self.canh = canh

    def xuat(self):
        print(f"Cạnh hình vuông:{self.canh}")
        print(f"Diện tích hình vuông:{self.tinh_dientich()}")

    # def __str__(self):
    #     return f"Cạnh: {self.canh}, Diện tích: {self.tinh_dientich()}, Chu vi: {self.tinh_chuvi()}"