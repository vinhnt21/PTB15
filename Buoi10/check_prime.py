# names = ["Nguyen", "Kien", "Cuong", "Ngoc"]
# print(names)
# names[2] = "Phong"
# print(names)
# names.append("Trong Kien")
# print(names)
# print(len(names))
# for i in range(len(names)):
#     print(names[i])


a = 3
b = 4
c = 5


if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Tam giac deu")
    elif a == b or a == c or b == c:
        print("Tam giac can")
    elif a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
        print("Tam giac vuong")
    else:
        print("Tam giac thuong")
else:
    print("Khong phai tam giac")
