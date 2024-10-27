'''
Yêu cầu người dùng nhập 3 cạnh:
- Nếu không hợp lệ thì thông báo 'Không phải tam giác'
- Nếu 3 cạnh bằng nhau thì là 'Tam giác đều'
- Nếu 2 cạnh bằng nhau thì là 'Tam giác cân'
- Còn lại là 'Tam giác thường'
'''

a = float(input('Nhập cạnh a: '))
b = float(input('Nhập cạnh b: '))
c = float(input('Nhập cạnh c: '))

if not (a+b>c and a+c>b and b+c>a):
    print('Không phải tam giác')
else:
    if a == b == c:
        print('Tam giác đều')
    elif a==b or a==c or b==c:
        print('Tam giác cân')
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
        print("Tam giác vuông")
    else:
        print('Tam giác thường')