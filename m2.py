#напишите программу реализующую переводы суток в часы,
# дни в минуты, минуты в секунды.
# Каждый перевод отдельная функция

def DH(days):
    d1=days*24
    return d1

def HM(days):
    d2=days*24*360
    return d2

def MS(days):
    d3=days*24*360*60
    return d3

def manager():
    days = int(input(("введите кол-во суток: ")))
    print("Часы",DH(days))
    print("Минуты",HM(days))
    print("Секунды", MS(days))
manager()