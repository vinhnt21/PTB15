'''
Yêu cầu người dùng nhập  vào 1 số n
In ra các từ n đến 1, đảm bảo
    Chia hết cho 5 
    hoặc chia hết cho 2 
    và không chia hết cho 3
Ví dụ:
    - Người dùng nhập vào 5
    - In ra: 1 2 3 4 5
'''
n = 100
for i in range(n, 1, -1):
    if i%5 == 0 or i%2 == 0 and i%3 != 0:
        print(i, end=' ')
    