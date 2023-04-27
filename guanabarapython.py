#Exercício 035 mundo1 

# Analisando um triângulo. 

# 035 Desenvolva um programa que leia o comprimento de três retas
# e ao usuário se elas podem ou não formar um triângulo.


print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
   print('Os segmentos acima PODEM FORMAR triângulo!')
else:
  print('Os segmentos acima NÃO PODEM FORMAR triângulo!')

#Exercício 006

# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada. 

'''n = int(input('Digite um número: )
d = n * 2 
t = n * 3 
r = n ** (1/2) 
print('O dobro de {} vale {}.'format(n, d))
print('O triplo de {} vale {}.\n A raiz quadrada de {:.2f} é igual a {}.'format(n, t, n, r))'''

n = int(input('Digite um número: '))
print('O dobro de {} vale {}.'format(n, (n*2)))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'format(n, (n*3), n (n**(1/2))))

#Exercício 09 - tabuada

# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada. 

num =int(input('Digite um número para ver sua tabuada: '))
print('-'*12)
print('{} x {} = {}'.format(num, 1, num*1))
print('{} x {} = {}'.format(num, 2, num*2))
print('{} x {} = {}'.format(num, 3, num*3))
print('{} x {} = {}'.format(num, 4, num*4))
print('{} x {} = {}'.format(num, 5, num*5))
print('{} x {} = {}'.fotmat(num, 6, num*6))
print('{} x {} = {}'.format(num, 7, num*7))
print('{} x {} = {}'.format(num. 8, num*8))
print('{} x {} = {}'.format(num, 9, num*9))
print('{} x {} = {}'.format(num, 10, num*10))
print('-'*12)

# 012 Faça um algoritmo que leia o preço de um produto e mostre
# seu novo preço, com 5% de desconto. 

# 10 reais = 100% /// 5% de 10 reais = x /// 10*5/100

1500*10/100

875*15/100 

preço = float(input('Qual é o preço do produto? R$'))
novo = preço - (preço * 5 / 100)  # preço menos cinco por cento 
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))


 #013 Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento. 

salário = float(input('Qual é o salário do Funcionário?' R$'))
novo = salário + (salário * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salário, novo))
 

# Criar programas com preços de produtos, com descontos à vista, e aumentos se parcelados

# 015 Escreva um programa que pergunte a quantidade de KM percorridos por um carro 
# alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custaR$60 por dia e R$0,15 por KM rodado. 

dias = int(input('Quantos dias alugados?')
km = float(input('Quantos KM rodados? '))
pago = (dias * 60 ) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))

#  017 Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa. 

# hipotenusa = raiz quadrada da soma dos catetos 

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))

# --------------

import math
co = float(input('Comprimento do cateto oposto: ')) 
ca = float(input('Comprimento do cateto adjacente: ')) 
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

# ---------------

from math import hypot
co = float(input('Comprimento do cateto oposto: ')) 
ca = float(input('Comprimento do cateto adjacente: ')) 
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

# 011 Faça um programa que leia a largura e a altura de uma parede
# em metros, calcule a sua área e a quantidade de tinta necessária 
# para pintá-la, sabendo que cada litro de tinta, pinta uma 
# área de 2m².

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt 
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, área)
tinta = área / 2 
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))

# -------------- estudo de funções -------------------

def teste():
	x = 8 
	print(f'Na função teste, n vale {n}')
	print(f'Na função teste, n vale {x}')


# Programa Principal
n = 2 
print(f'No programa principal, n vale {n}')
teste()
print(f'No programa principal, x vale {x}') # Output: erro ( x é variável local)

# ---------------

def teste(b):
    a=8 
    b+=4
    c=2 
    print(f'A dentro vale{a}')
    print(f'B dentro vale{b}')
    print(f'C dentro vale{c}') # escopo local 

a = 5 
teste(a)		       # escopo global 
print(f'A fora vale{a}')

# ---------------------

def funcao():
    n1=4
    print(f'N1 dentro vale {n1}')


n1=2
funcao()
print(f'N1 fora fale {n1}')


# -----------------------

def teste(b):
    global a # substitui  a=5 por a=8
    a=8 
    b+=4
    c=2 
    print(f'A dentro vale{a}')
    print(f'B dentro vale{b}')
    print(f'C dentro vale{c}') # escopo local 

a = 5 
teste(a)                       # escopo global 
print(f'A fora vale{a}')


# ------------------------

def somar(a=0,b=0,c=0)
    s = a + b + c 
    return s


#resp = somar(3, 2, 5)
#print(somar(3, 2, 5))
r1 = somar(3, 2, 5)
r2 = somar (2, 2)
r3 = somar(6)

print(f'Os resultados foram {r1}, {r2}, {r3}')

# ----------------------

def fatorial(num=1):
    f = 1 
    for c in range(num, 0, -1):
        f += c 
    return f 

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2}, {}')

# ------------------------

def par(n=0)
    if n % 2 == 0:
	return True
    else:
	return False 

num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')

# Desafio 101 - Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de 
# nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem votodo NEGADO, OPCIONAL
# ou OBRIGATÓRIO nas eleições.

# Desafio 102 - Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que
# indique o número a calcular e o outro chamado show, que será mostrado ou não na tela o processo de 
# cálculo do fatorial. 

# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
#o nome de um jogador e quantos gols ele marcou.
#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado 
# corretamente.

def ficha(nome='<desconhecido>', gols=0):
     jogador = input('Nome do jogador: ')
     contagem = int(input('Número de Gols: ')

nome = jogador
gols = contagem
ficha()
print(f'O jogador {} fez {} gol(s) no campeonato.)


# Desafio 104 - Crie um programa que tenha a função leiaint(), que vai funcionar de forma
# semelhante à função input() do Python, só que fazendo a validação para aceitar apenas
# um valor numérico.

# Ex:
# n = leiaInt('Digite um n')

# Desafio 105 - Faça um programa que tenha uma função chamada notas() que pode receber várias notas 
# de alunos e vai retornar um dicionário com as seguintes informações:

# Quantidade de notas; A maior nota; A menor nota; A média da turma; A situação(opcional)

# Adicione também as docstrings da função

  
