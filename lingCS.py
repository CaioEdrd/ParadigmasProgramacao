from lark import Lark
from lark import Tree, Token


#Gramática
G_Calc = """
?start: sum
      | NAME "=" sum    -> assign_var

?sum: product
    | sum "+" product   -> add
    | sum "-" product   -> sub

?product: expo
    | product "*" expo  -> mul
    | product "/" expo  -> div

?expo: atom
    | atom "^" expo     -> pot

?atom: NUMBER           -> number
     | "-" atom         -> neg
     | NAME             -> var
     | "(" sum ")"

%import common.CNAME -> NAME
%import common.NUMBER
%import common.WS_INLINE
%ignore WS_INLINE
"""
parser = Lark(G_Calc)

text = '2+1/3^2'
print("Implementação realizada por:\nAdriel Ravi\nCaio Eduardo\nPedro Henrique\n")
AST = parser.parse(text)
print(AST)
print()
print(AST.pretty())

