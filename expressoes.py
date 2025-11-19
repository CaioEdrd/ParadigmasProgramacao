def f1():
    soma = 1 + 2 
    return soma

def f2():
    return '-1'

a = f1() if 3 == 3 else f2()
print(a)