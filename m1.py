#Создать функцию которая принимает 3 параметра, первые два диапазон,
# 3-е кол-во чисел в списке,
# сгенерировать список с случайными числами этого диапазона. Все функции независимые

import random

def RNC(p1,p2,p3):
    num=[]
    for i in range(p3):
        num.append(random.randint(p1, p2))
    return num

def manager():
    p1 = int(input(("число от")))
    p2= int(input(("число до")))
    p3= int(input(("количество чисел")))
    print(RNC(p1,p2,p3))
manager()