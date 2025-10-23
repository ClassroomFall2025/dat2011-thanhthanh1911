# Đọc file baitho.txt

file = open("Resource.txt", "r",encoding="utf-8")
noidung = file.read()
print(noidung)

# Đọc từng dòng
file = open("Resource.txt","r",encoding="utf-8")
dong = file.readline()
print(dong)

# Đóng file
# file.close()
with open("Resource.txt", "r", encoding="utf-8") as file:
    noidung = file.read()
    print(noidung)

# Realline có s
with open("Resource.txt", "r", encoding="utf-8") as file:
    dong = file.readlines()
    print(dong)
    for d in dong:
        print(d)

with open("Resource.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line, end="")

with open("Resource.txt", "r",encoding="utf-8") as file:
    for line in file:
        print(line.strip())  # Xóa ký tự xuống dòng và khoảng trắng thừa

# Đọc từng dòng một và đếm số dòng
with open("Resource.txt", "r", encoding="utf-8") as file:
    count = 0
    for line in file:
        count += 1
        print(f"Dòng {count}: {line.strip()}")

# Mode w (ghi đè lên)
file = open("Resource1.txt", "w", encoding="utf-8")
noidung = file.read()
print(noidung)

# Mode a+ (ghi nội dung)
file =  open("Resource.txt", "a+", encoding="utf-8")
file =  open("Resource.txt", "r", encoding="utf-8")
noidung = file.read()
print(noidung)

# Khi open file với mode w lỗi
file = open("Resource2.txt", "w", encoding="utf-8")
file.write("Đây là dòng đầu tiên.\n")
file.close()
file.open("Resource2.txt", "r", encoding="utf-8")
noidung = file.read()
print(noidung)

file = open("Resource2.txt", "a", encoding="utf-8")
file.write("Đây là dòng đầu tiên.\n")
file.close()
file.open("Resource2.txt", "r", encoding="utf-8")
noidung = file.read()
print(noidung)
