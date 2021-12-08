# -- coding: utf-8 --
print("Введите свой возраст")
age=int(input())
print("Вас зовут Иван?(0 - нет, 1 - да)")
a=int(input())
if a == 1:
    print("Иванам нельзя")
elif age <= 0:
    print("Введите корректно возраст")
elif age >= 75:
    print("Вы уже старый для обучения")
elif age==16 or age>=16:
    print("Поздравляю, вы поступили во ВГУИТ")
elif age <16:
    b = 16 - age
    if b <= 9:
        print("Вам учиться в школе ещё",b,"лет")
    else: print("Вам ещё мало лет")
