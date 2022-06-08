

def change(st):
    stl=st.split(" ")
    str2=[1,1]
    str2[0]=stl[-1]
    str2[-1]=stl[0]
    str3=" ".join(str2)
    return str3

def manager():
    st = input(("введите строку с двумя словами"))
    print(change(st))
manager()
