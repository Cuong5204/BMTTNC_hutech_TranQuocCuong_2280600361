# Tạo một danh sách rỗng để lưu trữ kết quả
j = []
# Duyệt qua các số trong khoảng từ 2000 đến 3200, Kiểm tra xem số i
#  có chia hết cho 7 và không phải là bội số của 5 hay không
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))
print(','.join(j))