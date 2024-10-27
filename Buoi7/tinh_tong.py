n = int(input("Nhập số n: "))
tong = 0
i = 2
while i <= n:
    tong += i
    i += 2
# tong = 1 + 2 + 3 + ... + n
print(f"Tổng các số từ 1 đến {n} là: {tong}")
