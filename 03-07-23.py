"""
Operador ternário em Python
"""

'''logged_user = False 

if logged_used:
    msg = 'Usuário logado.'
else:
    msg = 'Usuário precisa logar.'

print(msg)'''

'''logged_user = True 
msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar.'

print(msg)

idade = 18 
e_de_maior = (idade >= 18)


if idade >= 18:
    print('Pode acessar.')
else:
    print('Não pode acessar.')



idade = input('Qual a sua idade?')

if not idade.isnumeric():
        print('Você precisa digitar apenas números')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = 'Pode acessar' if e_de_maior else 'Não pode acessar.'
'''

"""
Funções - def em Python (Parte 1)
"""

'''def funcao():
     print('Hello World!')

funcao()
funcao()
funcao()
funcao()
funcao()'''

'''def saudacao(msg='Olá', nome='usuário'):
     print(msg, nome)

saudacao(nome='Zezinho', msg='Hi')
saudacao('Oi', 'Luiz')
saudacao('Hello', 'Maria')
saudacao('Olá', 'Otávio')
saudacao('Olá', 'João')'''

'''def saudacao(msg='Olá', nome='usuário'):
     nome = nome.replace('e', '3')
     msg = msg.repalce('e', '3')
     return f'{msg} {nome}'

variavel = saudacao()

print(variavel)'''

'''def funcao(var):
    print('Isso não será executado.')
    return var 

variavel = funcao('Valor que eu quero')

if variavel:
    print(variavel)
else:
    print('Nenhum valor.')'''

'''def divisao(n1, n2):
    if n2 == 0:
        return

    return n1 / n2 

divide = divisao(8,-1)

if divide:
    print(divide)
else:
    print('Conta inválida')'''

def dumb():
    return [1,2,3,4,5]

def duumb():
    return True

def f(var):
    print(var)

def duuumb():
    return f 



var1 = dumb()
var2 = duumb() 
var3 = duuumb()
print(var1, type(var1))
print(var2, type(var2))
print(type(f))
print(type(duuumb))
print(id(var3), id(f))

if var3== f:
    print('var é igual a f')
else:
    print('Blaaaaaaaaa')



def dumbb():
    return('água', 'de coco')

var = dumb()

print(var[0], type(var))
print(var[1], type(var))

"""
Funções (def) em Python - *args **kwargs -
Aula 16 (Parte 3)
"""
'''def func(a1, a2, a3, a4, a5, nome=None, a6=None):
    print(a1, a2, a3, a4, a5, nome, a6)
    return nome, a6

var = func(1,2,3,4,5, nome='Luiz', a6='5')
print(var)

def func(*args):
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))

lista = [1,2,3,4,5]
n1, n2, *n = lista 
print(n1, n2, n)
print(*lista, sep='-')'''

'''def func(*args):
    args = list(args)
    args[0] = 20 
    print(args)

func(1,2,3,4,5)'''

'''def func(*args):
    for v in args:
        print(v)

func(1,2,3,4,5)'''

'''def func(*args):
    print(args)


lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]

func(lista, '6')
func(*lista, 10,20,30,40,50)
func(type(lista))
func(type(func))

def func2(*args, **kwargs):
    print(args)
    print(kwargs['nome'], kwargs['sobrenome'])

func2(*lista, *lista2, nome='Luiz', sobrenome='Miranda')'''

'''def func(*args, **kwargs):
    print(args)

    idade = kwargs.get('idade')

    if idade is not None:
        print(idade)
    else:
        print('Idade não existe')

lista = [1,2,3,4,5]
lista2 = [20,30,40,50]
func(*lista, *lista2, nome='Luiz', sobrenome='Miranda')'''

def func(*args, **kwargs):
    print(args)

    idade = kwargs['idade']
    print(idade)

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
func(*lista, *lista2, nome='Luiz', sobrenome='Miranda', idade=30)





















 















