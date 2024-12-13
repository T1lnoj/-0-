import random
#я пишу каменты просто ради коментов и баллов в какойто системи, чтобы меня не очислили, ну вот и все
number0 = random.randint(1, 10)

user_name = input("придумайте имя:")
password = int(input("придймайте пароль:"))
print("")#<--- тут принт

def password_encryption (password0):
    for i in range(1,1000):
        password0 = password + i

password_encryption(password)

print("##############################")
print("")
print("пароль сахранен")
print("")

sing_up = int(input("хотите войти?"))
sing_in = int(input("хотите рарегистрироватся?"))

if sing_up == 1 and sing_in == 0:#<---- тута ивы, вот

    user_name = input("придумайте имя:")
    password = int(input("придймайте пароль:"))
    print("")

elif sing_in == 1 and sing_up == 0:

    user_name0 = input("напешите свое имя:")
    sing_in0 = int(input("напешите свой пароль:"))

if user_name0 == user_name and sing_in0 == sing_in:

    print("##############################")
    print("")
    print("вы вошли!!!")
    print("")

print("поттвердите что вы человек")

random_number = input("введите число от 1 до 10")

if random_number == number0:#<---- а ето капча, вот

    print("вы робот!!!!!!!!!!!")

else:
    print("вы человек")