# n = int(input())

# is_prime = True


# for i in range(2, n):
#     if n % i == 0:
#         is_prime = False
#         break

# if is_prime:
#     print(n, 'là số nguyên tố')
# else:
#     print(n, 'không phải là số nguyên tố')

'''
Nhập vào 1 số n

In ra các số nguyên tố trong khoảng từ 1 đến n

Ví dụ:
- Nhập n = 20
- In ra: 2 3 5 7 11 13 17 19
'''

n = int(input())

for i in range(2, n+1):
    is_prime = True
    
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    
    if is_prime:
        print(i, end=' ')
