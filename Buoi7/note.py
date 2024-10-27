import random
secret_number = random.randint(1, 15)
is_guessing = True
while is_guessing:
    guess = int(input("Nhập số dự đoán của bạn: "))
    if guess == secret_number:
        print("Chúc mừng bạn iu nhé 💩!")
        is_guessing = False
    else:
        print("Sai rồi con 😼 ạ!") 