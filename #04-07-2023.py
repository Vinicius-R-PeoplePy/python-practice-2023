#04-07-2023

'''variavel = 'valor' # escopo global 

def func():
    print(variavel)

def func2(arg=None):
    #global variavel
    #variavel = 'Outro valor' # escopo local
    #print(variavel)
    arg = arg.replace('v', 'c')
    return arg

func()
outra_variavel = func2(arg=variavel)

print(outra_variavel)'''

'''variavel = 'valor'

def func():
    print(variavel)
    variavel = 1234
    print(variavel)

func()'''

#variavel = 'valor'

def func():
    outra_variavel = 'valor'
    return outra_variavel

def func2(arg):
    print(arg)

var = func()
func2(var)


# --------------------------

# expressões lambda 

#def funcao(arg, arg2):
#    return arg * arg2

#var = funcao(2,2)

'''a = lambda x, y: x * y 

print(a(2,2))



lista = [ 
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

def func(item):
    return item[1]

lista.sort(key=func, reverse=True)
print(lista)'''


lista = [ 
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

#lista.sort(key=lambda item: item[1], reverse=False)
print(sorted(lista, key=lambda i: i[1], reverse=False)) #experimente i[0]
print(lista)



# --------------- x ------------------

# tuplas

t1 = (1,2,3, 'a', 'Luiz Otávio')

print(t1)
print(t1[4])

for v in t1:
    print(v)

print(t1[2:])

t2 = 1,

print(t1, type(t1))

t1 = 1,2,'Luiz',4,5
t2 = 5,7,8,9,10
t3 = t1 + t2

n1, n2, n3, *_, n10 = t3
print(t3)
print(n3)

# -------------

t4 = (1,2,'Luiz',4,5) * 20
print(t1)

# -------------

t1 =(1,2,3,4,5)
t1 = list(t1)
t1[1] = 3000
t1 = tuple(t1)

print(t1)

# ---------------------------

# trocando o valor entre variáveis em Python 

x = 10 #Luiz
y = 'Luiz' #10
z = 'Otávio'

#z = x 
#x = y 
#y = z

x, y, z = z, x, y

print(f'x={x} e y={y} e z={z}')






















