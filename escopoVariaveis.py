CONT = 0

def inc():
    global CONT
    CONT +=1
    return CONT


def genCont():
    c = 0
    
    def incC():

        nonlocal c

        c += 1

        return c
    
    return incC

# def funcao():
#     a = 1
#     global b
#     b=b+2
#     c=3+1
#     print(a, "e", b, "e", c)

# b=3
# c=2
# funcao()
# print("'b' Fora:",b)
# print("'c' Fora:",c)

print("Início")
cPess = genCont()
cLivro= genCont()
cProf = genCont()

print('Pessoa: ', cPess())
print('Livro: ', cLivro())
print('Professor: ', cProf())
print('Pessoa: ', cPess())
print('Livro: ', cLivro())