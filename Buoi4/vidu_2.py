username = 'kien_xau_trai'
password = '123456'

username_input = input('Username: ')
password_input = input('Password: ')


if username_input == username and password_input == password:
    print('Đăng nhập thành công!!!')
elif username_input == username and password_input != password:
    print('Sai mật khẩu')
elif username_input != username and password_input == password:
    print('Sai tên đăng nhập')
else:
    print('Đăng nhập thất bại')
    print('Vui lòng nhập kien_xau_trai')
    