# crie um programa que peça o nome do usuário 

usuário = input("Digite seu nome: ")
print('O usuário chama-se {}.'.format(usuário))

# Crie um programa que leia dois números e mostre a soma entre eles.

x = 1 
y = 2 
soma = x+y 
print('A soma de x e y é igual a:', soma)

# Faça um programa que leia algo pelo teclado e mostre
# na tela o seu tipo primitivo e todas as informações
# possíveis sobre ele. 

# Digite algo
# O tipo primitivo desse valor é <class ''>
# Só tem espaços? 
# É um número?
# É alfabético?
# É alfanumérico?
# Está em maiúsculas?
# Está em minúsculas?
# Está capitalizada


a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfanumérico? ', a.isalnum())
print('Está em maiúsculas? ', a.isupper())
print('Está em minúsculas?', a.islower())
print('Está capitalizada? ', a.istitle())


### utilizando módulos 

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz))) # arredonda pra cima; floor, arredonda pra baixo

### outro jeito

from math import sqrt  
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}.'.format(num, floor(raiz)))

# random 

import random
num = random.random 
print(num)


# randint 

import random
num = random.randint(1, 10)
print(num)

# digite import e aperte a tecla espaço (no pycharm).
# checar PyPI Index

# emoji - ver emoji sheet 

import emoji
print(emoji.emojize("Olá mundo :world_map:", use_aliases=True))


### Faça um programa que leia um número inteiro e mostre na 
### tela o seu sucessor e seu antecessor.

n = int(input('Digite um número: '))
a = n -1 
s = n + 1 
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, a, s))


### outro jeito:


n = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))


###  Crie um algoritmo que leia um número e mostre o seu dobro,
### o triplo e a raiz quadrada. 

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}.'.format(n, d))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, t, n, r))


### outro jeito 
n = int(input('Digite um número: '))
print('O dobro de {} vale {}.'.format(n, (n*2)))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*3), n, (n**(1/2))))

### outro jeito

n = int(input('Digite um número: '))
print('O dobro de {} vale {}.'.format(n, (n*2)))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*3), n, pow(n, (1/2))))


# Desenvolva um programa que leia as duas notas de um aluno,
# calcule e mostre a sua média.

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
média = (n1 + n2) / 2 # utilize parênteses para não dar erro!
print('A média entre {:.1f} e {:1f} é igual a {:.1f}'.format(n1, n2, média))

# Escreva um programa que leia um valor em metros e o exiba convertido
# em centímetros e milímetros. 

# km hm dam m dm cm mm 

medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('A média de {}m corresponde a`{:.0f}cm e {:.0f}m'.format(medida, cm, mm))


### incrementando 

# dm(Decímetro) = valor*10
# cm(Centímetro) = valor*100
# mm(Milímetro) = valor*1000
# dam(Decâmetro) = valor/10
# hm(Hectômetro) = valor/100
# km(Quilômetro) = valor/1000

a = float(input('Digite um valor em metro: '))
print(f'A medida de {a} metros é igual a {a*10} decímetros')
print(f'A medida de {a} metros é igual a {a*100} centímetros')
print(f'A medida de {a} metros é igual a {a*1000} milímetros')
print(f'A medida de {a} metros é igual a {a/10} decâmetros')
print(f'A medida de {a} metros é igual a {a/100} hectômetros')
print(f'A medida de {a} metros é igual a {a/1000} quilômetros')
print(f'A medida de {a} metros é igual a {a/10:.1f} decâmetros')

### Faça um programa que leia um número inteiro qualquer e mostre
# na tela a sua tabuada. 

num = int(input('Digite um número para ver sua tabuada: '))

print('-'*12)
print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 2, num*2))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*6))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*8))
print('{} x {:2} = {}'.format(num, 9, num*9))
print('{} x {:2} = {}'.format(num, 10, num*10))
print('-'*12)

### Crie um programa que leia quanto dinheiro uma pessoa
### tem na carteira e mostre quantos Dólares ela pode comprar.

# Considere US$1,00 = R$4,96

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dólar = real / 3.27
print('Com R${} você pode comprar US${:.2f}'.format(real, dólar))

# Faça um programa que leia a largura e a altura de uma parede 
# em metros, calcule a sua área e a quantidade de tinta necessária
# para pintá-la, sabendo que cada litro de tinta, pinta uma área
# de 2m². 

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'format(larg, alt, área))
tinta = área / 2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))


### Faça um algoritmo que leia o salário de um funcionário
# e mostre seu salário com 15% de aumento. 

salário = float(input("Qual é o salário do funcionário? R$'))
novo = salário + (salário * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salário, novo))


## criar um programa que calcule o preço de um produto com desconto versus parcelado ###


### Escreva um programa que converta uma temperatura 
### digitada em °C e converta

c = float(input('Informe a temperatura em °C: '))
f = ((9*c)/5)+32
print('A temperatura de {}°C corresponde a {}°F!'.format(c, f))

### Escreva um programa que pergunte a quantidade de Km percorridos
### por um carro alugado e a quantidade de dias pelos
### quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
### custa R$60 por dia e R$0,15 por Km rodado. 

dias = int(input('Quantos dias alugado?'))
km = float(input('Quantos Km rodados? '))
pago = (dias * 60)  + (km * 0.15)
print('O total a pagar é de R$ {:.2f}'.format(pago))


# Crie um programa que leia um número Real qualquer pelo teclado
# e mostre na tela a sua porção inteira. 

#Ex.: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6. 

num = float(input('Digite um número: '))
print('A porção inteira do número digitado é {:.0f}'.format(num))


#  Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triângulo retângulo, calcule 
# e mostre o comprimento da hipotenusa. 

# O quadrado da hipotenusa é igual à soma do quadrado dos catetos
# A hipotenusa é a raiz quadrada da soma do quadrado dos catetos 

'''co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi =  math.hypot(ca, co)
print('A hipotenusa vai medir {:.2f}'.format(hi))

# Faça um programa que leia um ângulo qualquer e 
# mostre na tela o valor do seno, cosseno e 
# tangente desse ângulo. 

# eixo vertical: seno; eixo horizontal: cosseno. 

'''import math
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo, tangente))'''

from math import radians, sin, cos, tan
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo, tangente))

# Um professor quer sortear um dos seus quatro alunos para 
# apagar o quadro. Faça um programa que ajude ele, lendo o nome
# deles e escrevendo o nome do escolhido. 

'''import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista) # método choice da classe random 
print('O aluno escolhido foi {}'.format(escolhido))'''

from random import choice 
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista) # método choice da classe random 
print('O aluno escolhido foi {}'.format(escolhido))


# O mesmo professor do desafio anterior quer sortear a 
# ordem de apresentação de trabalhos dos alunos. Faça um 
# programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

'''n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação será ')
print(lista)'''

from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será ')
print(lista)

# Faça um programa em Python que abra e reproduza o áudio 
# de um arquivo MP3. 

# obs.: colocar mp3 na mesma pasta do código. 

import pygame
pygame.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
pygame.event.wait()


# Crie um programa que leia o nome completo de uma pessoa
# e mostre:
# O nome com todas as letras maiúsculas e minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome 

nome = str(input('Digite seu nome completo: ')).strip() # elimina espaços antes e depois
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome, lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' '))) # conta quantas letras tem desconsiderando espaço no meio
#print('Seu primeiro nome tem {} letras'.format(nome.find(' '))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))


# Faça um programa que leia um número de 0 a 9999 e
# mostre na tela cada um dos dígitos separados.
# Ex.: Digite um número: 1834
# unidade: 4 	dezena: 3 	centena:8 	milhar:1

'''num = int(input('Informe um número: '))
n = str(num)
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))''' # dá erro caso não digite 4 dígitos

num = int(input('Informe um número: '))
u = num // 1 % 10 
d = num // 10 % 10 
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezema: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

### Crie um programa que leia o nome de uma cidade
# e diga se ela começa ou não com o nome "SANTO"

cid = str(input('Em que cidade você nasceu? ')).strip # caso o usuário insira espaços
print(cid[:5].upper() == 'SANTO') # upper(), caso usuário digite tudo em minúsculo

# Crie um programa que leia o nome de uma pessoa e diga
# se ela tem "SILVA" no nome. 

nome = str(input('Qual é o seu nome completo?')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.upper())) # 'in' -> operador; não é um método. 

# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez. 

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('a')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))

# Faça um programa que leia o nome completo de uma pessoa
# mostrando em seguida o primeiro e o último nome separadamente.
# Ex.: Ana Maria de Souza
# primeiro: Ana
# último: Souza 

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome {}'.format(nome[len(nome)-1]))

# Escreva um programa que faça o computador "pensar" em 
# um número inteiro entre 0 e 5 e peça para o usuário 
# tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu. 


from random import randint 
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('=' * 20)
jogador = int(input('Em que número eu pensei? '))
PRINT('PROCESSANDO...')
sleep(10)
if jogador == computador:
	print('PARABÉNS! Você conseguiu me vencer!')
else:
	print('GANHEI! Você conseguiu me vencer!')

# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que
# ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Qual é a velocidade atual do carro?'))
if velocidade > 80:
	print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
	multa = (velocidade-80) * 7
	print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')

# Crie um programa que leia um número inteiro 
# e mostre na tela se ele é PAR ou ÍMPAR. 

num = int(input('Me diga um número qualquer: '))
resultado = num % 2
if resultado == 0:
	print('O número {} é PAR'.format(num))
else:
	print('O número {} é ÍMPAR'.format(num))

# Desenvolva um programa que pergunte a distância de uma viagem
# em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para
# viagens de até 200Km e R$0,45 para viagens mais longas. 

dist = float(input('Qual é a distância da sua viagem?'))
print('Você está prestes a começar uma viagem de {}Km.'.format(distância))
'''if dist <= 200:
	preço = dist * 0.50
else:
	preço = dist * 0.45'''
preço = dist * 0.50 if dist <= 200 else dist * 0.45:
print('E o preço da sua passagem será de R${:.2f}'.format(preço))

# Faça um programa que leia um ano qualquer
# e mostre se ele é BISSEXTO. 

from datetime import date 
ano = int(input('Que ano quer analisar? Digite 0 para analisar o ano atual: '))
if ano == 0:
	ano = date.today().year # data/dia/ano da máquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
	print('O ano {} é BISSEXTO'.format(ano))
else:
	print('O ano {} NÃO é BISSEXTO'.format(ano))

# Faça um programa que leia três números
# e mostre qual é o maior e qual é o menor. 

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificando quem é menor 
menor = a 
if b<a and b<c:
	menor = b
if c<a and c<b:
	menor = c 
# Verificando quem é o maior 
maior = a 
if b>a and b>c:
	maior = b
if c>a and c>b:
	maior = c 
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))

# Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento. 
# Para salários superiores a R$1.2500.00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%. 

salário - float(input('Qual é o salário do funcionário? R$'))
if salário <= 1250:
	novo = salário + (salário * 15 / 100)
else:
	novo = salário + (salário * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, novo))


# Desenvolva um programa que leia o comprimento
# de três segmentos de reta e confirme se elas 
# formam um triângulo ou não.


print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Primeiro triângulo: '))
r2 = float(input('Segundo triângulo: '))
r3 = float(input('Terceiro triângulo: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
	print('Os segmentos acima PODEM FORMAR triângulo.')
else:
	print('Os segmentos acima não podem formar triângulo.')

# Escreva um programa para aprovar o empréstimo bancário 
# para a compra de uma casa. Pergunte o valor da casa, o salário
# do comprador e em quantos anos ele vai pagar.
# A prestação ḿensal, não pode exceder 30% do salário ou então
# o empréstimo será negado.

casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print('A prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
	print('Empréstimo pode ser CONDECIDO!')
#print('COMPARANDO tem que pagar{} e o mínimo é de {}',format(prestação, mínimo))


# Escreva unm programa que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal
# Notação Posicional. 

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão
[1] converter para BINÁRIO
[2] converter para OCTAL 
[3] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
	print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
	print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
	print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
	print('Opção inválida. Tente novamente')


# Escreva um programa que leia dois números inteiros e compare-os,
# mostrando na tela uma mensagem:
# - O primeiro valor é maior 
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais 

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num1> num2:
    print(f'O valor digitado {num1} é maior que o valor digitado {num2}')
elif num2 > num1:
    print(f'O valor digitado {num2} é maior que o valor digitado {num1}')
else:
    print('Não existe valor maior, os dois números são iguais.')


# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora de se alistar ou se já passou do tempo de alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou 
# do prazo. 


'''idade = int(input('Digite sua idade: '))
if idade == 18: 
	print('É hora de se alistar.')
elif idade < 18:
	print('Ainda vai se alistar.')
elif idade > 18:
	print('Já passou do prazo de alistamento.')'''

from datetime import date 
atual = date.today().year 
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc 
print('Quem nasceu em {} tem {} anos.'.format(nasc, idade, atual))
if idade == 18:
	print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
	saldo - 18 - idade
	print('Ainda faltam {} anos para o alistamento.'.format(saldo))
	ano = atual + saldo
	print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
	saldo = 18 - idade
	print('Você já deveria ter se alistado há {} anos.'.format(saldo))
	ano = atual - saldo
	print('Seu alistamento será em {}'.format(ano))


# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# - média abaixo de 5.0: REPROVADO
# - média entre 5.0 e 6.9: RECUPERAÇÃO 
# Média 7.0 ou superior: APROVADO

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
média = (n1 + n2) // 2 
if média < 5.0:
	print(f'Sua primeira nota foi {n1}, sua segunda nota foi {n2}, sua média é de {média} e você está REPROVADO.')
elif 6.9 > média >= 5:
	print(f'Sua primeira nota foi {n1}, sua segunda nota foi {n2}, sua média é de {média} e você está em RECUPERAÇÃO.')
elif média > 7.0:
	print(f'Sua primeira nota foi {n1}, sua segunda nota foi {n2}, sua média é de {média} e você está APROVADO.') 



# A Confederação Nacional de Natação precisa de um programa que leia 
# o ano de nascimento de um atleta e mostre sua categoria, de acordo
# com a idade:
# - até 9 anos: MIRIM 
# - até 14 anos: INFANTIL 
# - até 19 anos: JUNIOR
# - até 25 anos: SÊNIOR
# - Acima: MASTER

from datetime import date
ano_nasc = int(input('Digite o ano de nascimento do atleta: '))
atual = date.today().year 
idade = atual - nasc 
mirim = 9 
infantil = 14 
junior = 19 
senior = 25 
master = master > senior 
if idade <= mirim:
	print(f'O(a) atleta tem {atual} anos e sua categoria é MIRIM.'
if idade <= infantil:
	print(f'O(a) atleta tem {atual} anos e sua categoria é INFANTIL.')
if idade <= junior = 19:
	print(f'O(a) atleta tem {atual} anos e sua categoria é JUNIOR.')
if idade <= senior:
	print(f'O)a) atleta tem {atual} anos e sua categoria é SÊNIOR')
if idade > master: 
	print(f'O(a) atleta tem {atual} anos e sua categoria é MASTER.')


# Refaça o exercício dos triângulos, acrescentando o recurso de 
# mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais 
# - Isósceles: dois lados iguais 
# - Escaleno: todos os lados diferentes 

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r2 + r3 and r3 < r1 + r2:
	print('Os segmentos acima PODEM FORMAR um triângulo!')
	if r1 == r2 == r3:
		print('EQUILÁTERO')
	if r1 != r2 != r3 != r1:
		print('ESCALENO')
	else:
		print('ISÓSCELES')
else:
	print('Os segmentos acima NÃO PODEM FORMAR triângulo')


# Desenvolva uma lógica que leia o peso e a altura de uma pessoa.
# calcule o IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal 
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade 
# Acima de 40: Obesidade mórbida 

peso = float(input('Qual é seu peso?(Kg)  '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura**2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
	print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
	print('Você está na faixa de peso normal')
elif 25 <= imc < 30:
	print('Você está em SOBREPESO!)
elif 3- <= imc < 40:
	print('Você está em OBESIDADE MÓRBIDA, cuidado!)

# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10& de desconto 
# à vista no cartão: 5% de desconto 
# em até 2x no cartão: preço normal 
# 3x ou mais no cartão: 20% de juros 

print("{:=^40}".format("LOJA TALS E TALS"))
preço = float(input('Preço das compras: R$'))
print('''	FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão 
[4] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas?'))
else:
    total = 0
    print('OPÇÃO INVÁLIDA. Tente novamente')
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(
        totparc, parcela))
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(
    preço, total))



#Crie um programa que faça o computador jogar Jokenpô 
#com você. 

# 0 = Pedra
# 1 = Papel 
# 2 = Tesoura


'''from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0,2)
#print('O pc escolheu {}'.format(itens[pc]))
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*11)
print('Computador jogou {}'.format(itens[pc]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*11)
if pc == 0: # pc jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
    
elif pc == 1: # pc jogou PAPEL 
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    
    else:
        print('JOGADA INVÁLIDA!')
elif pc == 2: # pc jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')'''
        


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# aninhamento, estruturas de repetição, laços, for (...) ->

#print('Oi')
#print('Oi')
#print('Oi')
#print('Oi')
#print('Oi')
#print('Oi')

#for c in range(0, 6):
#    print('Oi')
#
#for c in range(6, 0, -1):
#    print(c)
#print('FIM')

'''i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM!')'''

#for c in range(0, 3):
#    n = int(input('Digite um valor: '))
#print('fim')

'''s = 0 
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n 
print('O somatório de todos os valores foi {}'.format(s))'''



# Faça um programa que mostre na tela uma contagem regressiva 
# para o estouro de fogos de artifício, indo de 10 até 0, com 
# uma pausa de 1 segundo entre eles.

'''from time import sleep
for cont in range(10, -1, -1):
    print(cont)
    sleep(0.5)
print('BUM! BUM! BUM!')'''



# Crie um programa que mostre na tela
# todos os números pares que estão no intervalo 
# entre 1 e 50. 

'''for n in range(2, 51, 2):
        print(n, end=' ')
print('Acabou')'''






# Faça um programa que calcule a soma entre todos os números ímpares
# que são múltiplos de três e que se encontram no intervalo de 1 
# até 500. 


'''soma = 0
cont = 0
for c in range(1, 501, 2):
        if c % 3 == 0:
             soma = soma + c
             cont += 1 
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))'''




### Faça uma tabuada de um número que o usuário escolher
# só que agora utilizando o laço for. 

'''num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))'''

# Desenvolva um programa que leia seis números inteiros 
# e mostre apenas aqueles que forem pares. Se o valor digitado for
# ímpar, desconsidere-o. 


'''soma = 0
cont = 0 
for c in range(1, 11):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        soma += num 
        cont += 1 
print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))'''




# Desenvolva um programa que leia o primeiro termo e a razão 
# de uma PA. No final, mostre os 10 primeiros 
# termos dessa progressão. 

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão 
for c in range(primeiro, décimo + razão, razão):
    print('{} '.format(c), end='→ ')
print('ACABOU')


# Faça um programa que leia um número inteiro 
# e diga se ele é ou não um número primo. 



num = int(input('Digite um número: '))
tot = 0 
for c in range(1, num +1):
	if num % c == 0:
		print('\033[33m', end='')
		tot += 1
	else:
		print('\033[31m', end='')
	print('{} '.format(c)), end='')
print('\n033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
	print('E por isso ele É PRIMO!)
else:
	print('E por isso ele NÃO É PRIMO!')


# Crie um programa que leia uma frase qualquer e diga
# se ela é um palíndromo, desconsiderando os espaços. 

# Ex.: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA

frase = str(input('Digite um frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
'''for letra in range(len(junto) -1, -1, -1):
	inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))'''
print(junto, inverso)
if inverso == junto:
	print('Temos um palíndromo!')
else:
	print('A frase digitada não é um palíndromo!')


# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores.

from datetime import datetimeatual = date.today().year
atual = date.today().year
totmaior = 0 
totmenor = 0 
for pess in range(1, 8):
	nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
	idade = atual - nasc 
	if idade > 21:
		totmaior += 1
	else:
		totmenor += 1 
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))



######################################################

# Faça um programa que leia o peso de cinco pessoas. 
# No final, mostre qual foi o maior e o menor peso lidos. 

maior = 0 
menor = 0 
for p in range(1, 6):
	peso = float(input('Peso da {}ª pessoa: '.format(p)))
	if p == 1:
		maior = p 
		menor = p 
	else:
		if peso > maior:
			maior = peso 
		if peso < menor:
			menor = peso 
print('O maior peso lido foi de {}kg'.format(maior))
print('O menor peso lido foi de {}kg'.format(menor))



######################################################

# Desenvolva um programa que leia o nome, idade e sexo
# de 4 pessoas. No final do programa, mostre:

# A média de idade do grupo 
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.

somaidade = 0
médiaidade = 0
maioriadade = 0 
nomevelho = ''
totmulher = 20 

for p in range(1, 5):
    print('----------{}ª PESSOA ------------'.format(p))
    nome = str(input('Nome:').strip())
    idade = int(input('Idade : '))
    sexo = str(input('Sexo [M/F]:	')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
    	maioridadedehomem = idade 
    	nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem: 
    	maioriadade = idade 
    	nomevelho = nome 
    if sexo in 'Ff' and idade < 20:
    	totmulher20 += 1

médiaidade = somaidade / 4 

print('A média de idade do grupo é de {} anos'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))


######################################################

# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
# 'M' ou'F'. Caso esteja errado, peça a digitação novamente até ter um 
# valor correto. 

sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
	sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))



######################################################

# Crie um programa que faça o pc "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando
# no final quantos palpites foram necessários para vencer.

from random import randint 
computador = randint(0, 10)
print('Sou seu pc... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0 
while not acertou:
	jogador = int(input('Qual é seu palpite? ')
	palpites += 1 
	if jogador  == computador:
		acertou = True
	else:
		if jogador < computador:
			print('Mais... Tente mais uma vez.')
		elif jogador > computador:
			print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))



######################################################

# Crie um programa que leia dois vaores e mostre um menu como ao lado
# na tela: 
# Seu programa deverá realizar a operação solicitada em cada caso. 
# [1] somar, [2]multiplicar, [3] maior, [4] novos números, [5] sair do programa 

from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''[1] somar
		[2] multiplicar 
		[3] maior 
		[4] novos números 
		[5] sair do programa''')
    opção = int(input('Qual é a sua opção? '))
    if opção == 1:
        psoma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, produto))
    elif opção == 2:
        produto = n1 * n2
        print('O resultado de  {} x {} é {}'.format(n1, n2, soma))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print('Entre {} e {} o maior valor de é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
        print('=-=' * 10)
        sleep(5)

print('Fim do programa! Volte sempre!')



######################################################

# Faça um programa que leia um número qualquer
# e mostre o seu fatorial. 

# Ex.: 5!= 5x4x3x2x1=120


'''from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'format(n, f))'''

n = int('Digite um número para calcular seu fatorial: ')
c = n 
f = 1
print('Calculando {}!'.format(n), end='')
while c > 0:
	print('{} '.format(c), end='')
	print(' x ' if c > 1 else ' = ', end='')
	f *= c 
	c -= 1 
print('{}'.format(f))



######################################################

# Leia o primeiro termo e a razão de uma PA, mostrando
# os 10 primeiros termos da progressão usando a 
# estrutura while. 


print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1 
while cont <= 10:
	print('{} -> '.format(termo), end='') 
	termo += razão 
	cont += 1 
print('FIM')



######################################################

### refazendo -> perguntando para o usuário se ele quer 
### mostrar mais alguns termos. O programa encerra
# quando ele disser que quer mostrar 0 termos. 


print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1 
total = 0 
while mais != 0:
	total = total + mais 
	while cont <= 10:
		print('{} -> '.format(termo), end='') 
		termo += razão 
		cont += 1 
	print('PAUSA')
	mais = int(input('Quantos termos você quer mostrar a mais?'))
print('Progressão finalizada com {} termos mostrados.'.format(total))


######################################################


# Escreva um programa que leia um número n inteiro qualquer
# e mostre na tela os n primeiros elementos de uma Sequência de 
# Fibonacci. 
# Ex.: 0 - 1 - 1 - 2 - 3 - 5 - 8 

print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos võcê quer mostrar? '))
t1 = 0 
t2 = 1 
print('~'*30)
print('{} -> {}'.format(t1, t2), end='')
cont = 3 
while cont <= n:
	t3 = t1 + t2 
	print(' -> {}'.format(t3), end='')
	t1 = t2 
	t2 = t3 
	cont += 1 
print(' -> FIM')
print('~'*30)


######################################################

# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram
# digitados e qual foi a soma entre eles (desconsiderando o flag).

num = cont = soma = 0 
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
	soma += num
	cont += 1 
	num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {] números e a soma entre eles foi {}'.format(cont, soma))



######################################################

# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual 
# foi o maior e o menor valores lidos. O programa deve perguntar ao 
# usuário se ele quer ou não continuar a digitar valores. 

resp = 'S'
soma = quant = média = 0 
while resp in 'Ss':
	num = int(input('Digite um número: '))
	soma += num 
	quant += 1 
	if quant == 1:
		maior = menor = num 
	else:
		if num > maior:
			maior = num 
		if num < menor:
			menor = num 
	resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
média = soma / quant 
print('Você digitou {] números e a média foi {}'.format(quant, média))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))


### + while 

'''cont = 1 
while True:
	print(cont, '-> ', end='')
	cont += 1 
print('Acabou')'''



######################################################

'''n = 0
while n != 999:
	n = int(input('Digite um número: '))'''

n = s = 0
while True:
	n = int(input('Digite um número: '))
	if n == 999:
		break
	s += n 
#print('A soma vale {}'.format(s))'''
print(f'A soma vale {s}')


#####

nome = José
idade = 33
salário = 987.35
print(f'O {nome} tem {idade} anos e ganha R${salário:.2f}')
#print('O {} tem {} anos.'.format(nome, idade))



######################################################


# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, 
# que  é a condição de parada. No final, mostre quantos números foram 
# digitados e qual foi a soa entre eles (desconsiderando o flag).

soma = count = 0 
while True:
	num = int(input('Digite um valor (999 para parar): '))
	if num == 999:
		break
	cont += 1 
	soma += num 
print("A soma dos {cont} valores foi {soma}!")



######################################################

### faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for
# negativo.

while True:
	n = int(input('Quer ver a tabuada de qual valor?'))
	print('-'*30)
	if n < 0:
		break
	for c in range(1, 11):
		print(f'{n} x {c} = {n*c}')
	print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')



######################################################

# Faça um programa que jogue par ou ímpar com o pc. 
# O jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vitórias consecutivas que ele
# conquistou no final do jogo. 

from random import randint

while True:
	jogador = int(input('Diga um valor: '))
	pc = randint(0, 11)
	total = jogador + pc
	tipo = ' '
	while tipo not in 'PI':
		tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
	print(f'Você jogou {jogador} e pc {pc}. Total de {total}')
	print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
	if tipo == 'P':
		if total % 2 == 0:
			print('Você VENCEU!')
			v += 1
		else:
			print('Você PERDEU!')
	if tipo == 'I':
		if total % 2 == 1:
			print('Você VENCEU!')
			v += 1 
		else: 
			print('Você PERDEU!')
			break 
	print('Vamos jogar novamente...')
print('GANE OVER! Você venceu {v} vezes.')


######################################################

# Crie um programa que leia a idade e o sexo
# de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário 
# quer ou não continuar. No final, mostre:

# A) quantas pessoas tem mais de 18 anos. 
# B) quantos homens foram cadastrados 
# C) quantas mulheres tem menos de 20 anos. 

tot18 = totH = totM20 = 0 
while True:
	idade = int(input('Idade: '))
	sexo = ' '
	while sexo not in 'MF':
		sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
	if idade >= 18:
		tot18 += 1
	if sexo == 'M':
		totH += 1 
	if sexo == 'F' and idade < 20:
		totM20 += 1 
	resp = ' '
	while resp not in 'SN':
		resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
	if resp == 'N':
		break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados.')
print(f'E temos {totM20} mulheres com menos de 20 anos.')


######################################################

# Crie um programa que leia o nome e o preço 
# de vários produtos. O programa deverá perguntar
# se o usuário vai continuar. No final, mostre:

# A) Qual é o total gasto na compra. 
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato. 

total = totmil = menor = cont = 0 
barato = ''
while True:
	produto = str(input('Nome do produto: '))
	preço = float(input('Preço: R$'))
	cont += 1
	total += preço
	if preço > 1000:
		totmil += 1
	if cont == 1 or preço < menor:
		menor = preço 
		barato = produto
	resp = ' '
	while resp not in 'SN':
		resp = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
	if resp == 'N':
		break 
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')


######################################################

# Crie um programa que simule o funcionamento
# de um caixa eletRônico.
# No início, pergunte ao usuário qual será
# o valor a ser sacado (número inteiro) e o programa
# vai informar quantas cédulas de cada valor serão entregues

# OBS.: Considere que o caixa possui cédulas de R$50, R$20, R$10, R$1.

print('=' * 30)
print('{:^30}'.format('BANCO TALS')
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor 
céd = 50
totcéd = 0 
while True:
	if total >= céd:
		total -= céd 
		totcéd += 1 
	else:
		if totcéd > 0:
			print(f'Total de {totcéd} cédulas de R${céd}')
		if céd == 50:
			céd = 20 
		elif céd == 20:
			céd = 10
		elif céd == 10:
			céd = 1 
		totcéd = 0 
		if total == 0:
			break 
print('=' * 30)
print('Volte sempre ao BANCO TALS! Tenha um bom dia!')



######################################################

### TUPLAS ###
# tuplas são imutáveis (não podem ter itens atribuídos)

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche[1]) # Suco 
print(lanche[-2]) # Pizza 
print(lanche[1:3] # Suco, Pizza 
print(lanche[2:]) # Pizza, Pudim 
print(lanche[:2]) # Hambúrguer, 'Suco'
print(lanche[-2:]) # Pizza, Pudim 
print(lanche[-3:]) # Suco, Pizza, Pudim 
for cont in range(0, len(lanche)):
	print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for comida in lanche:
	print(f'Eu vou comer {comida}')

for pos, comida in enumerate(lanche):
	print(f'Vou comer {comida} na posição {pos}')

print(sorted(lanche))
print(lanche)

#	print(lanche[cont])
#print(lanche)
#for comida in lanche:
#	print(f'Eu vou comer {comida}')


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b 
print(c)
c = b + a 
print(c)
print(c.count[5])
print(c.index(8))
print(c.index(5, 1)) # deslocamento 

################################


pessoa = ('Fulano', 30, 'M', 80.0)
del(pessoa)
#del(pessoa[1]) -> erro, tupla é imutável. 
print(pessoa) # erro -> pessoa não está definido.



######################################################


# Crie um programa que tenha uma tupla totalmente preenchida 
# com uma contagem por extenso, de zero até vinte. 

# Seu programa deverá ler um número pelo teclado (entre 0 e 20)
# e mostrá-lo por extenso. 

cont = ('zero', 'um', 'dois', 'três', 'quatro',
	'cinco', 'seis, 'sete', 'oito', 'nove',
	'dez', 'onze', 'doze', 'treze', 'catorze',
	'quinze', 'dezesseis', 'dezessete', 'dezoito',
	'dezenove', 'vinte')
while True:
	num = int(input('Digite um número entre 0 e 20: '))
	if - <= num <= 20:
		break 
	print('Tente novamente.', end='')
print(f'Você digitou o número {cont[num]}')


######################################################

# Crie uma tupla preenchida com os 20 primeiros 
# colocados na Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:

# A) Os 5 primeiros.
# B) OIs últimos 4 colocados. 
# C) Times em ordem alfabética.
# D) Em que posição está o time da Chapecoense. 

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
		 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
		 'São Paulo', 'Fluminense', 'Sport Recife', 
		 'EC Vitória' , 'Coritiba', 'Avaí', 'Ponte Preta',
		 'Atlético-GO')
print('-='*15)
print(f'Lista de times: {times}')
print('-='*15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os quatro últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1ª posição')


'''for t in times:
	print(t)'''


######################################################

### Crie um programa que vai gerar cinco números aleatórios 
# e colocar em uma tupla. Depois disso, mostre a listagem de 
# números gerados e também indique o menor e o maior valor 
# que estão na tupla. 

from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10),
	randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for n in num:
	print(f'{num} ', end='')
print(f'\nO maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')


######################################################

### Desenvolva um programa que leia quatro valores
# pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3. 
# C) Quais foram os números pares. 

num = (int(input('Digite um número: ')),
	   int(input('Digite um número: ')),
	   int(input('Digite um número: ')),
	   int(input('Digite um número: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
	print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
else:
	print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram ', end='')
for n in num:
	if n % 2 == 0:
		print(n, end=' ')



######################################################


# Crie um programa que tenha uma tupla única com 
# nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os
# dados em forma tabular. No

listagem = ('Lápis', 1.75,
			'Borracha', 2,
			'Caderno', 15.90,
			'Estojo', 25,
			'Transferidor', 4.20,
			'Compasso', 9.99, 
			'Mochila', 120.32, 
			'Canetas', 22.30,
			'Livro', 34.90)
#print(listagem)
#for item in listagem:
#	print(item)print
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":40}')
print('-' * 40)
for pos in range(0, len(listagem)):
	if pos % 2 == 0:
		print(f'{listagem[pos]:.<30}', end='')
	else:
		print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)


######################################################


# Crie um programa que tenha uma tupla com várias palavras
# (não usar acentos). Depois disso, você deve mostrar,
# para cada palavra, quais são as suas vogais. 

palavras = ('aprender', 'programar', 'linguagem', 'python',
			'curso', 'gratis', 'estudar', 'praticar',
			'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
	print(f'\nNa palavra {p,upper()} temos ', end='')
	for letra in p:
		if letra.lower() in 'aeiou':
			print(letra, end=' ')


######################################################


# ~~~~~ LISTAS ~~~~~~~~

'''num = (2, 5, 9, 1)
num[2] = 3
print(num) # erro. tupla imutável.'''

'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
num.remove(2)
if 4 in num:
	num.remove(4) 
else:
	print('Não achei o número 5')
#num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos.')'''

'''valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
	print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')'''

a = [2, 3, 4, 7]
#b = a # ligação
b = a[:] # cópia dos valores de a
b[2] = 8 
print(f'Lista A: {a}')
print(f'Lista B: {b}')

######################################################

# Faça um programa que leia 5 valores numéricos e guarde-os em
# uma lista. No final, mostre qual foi o maior e o menor valor 
# digitado e as suas respectivas posições na lista.

listanum = []
mai = 0 
men = 0 
for c in range(0, 5):
	listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
	if c == 0:
		mai = men = listanum[c]
	else:
		if listanum[c] > mai:
			mai = listanum[c]
		if listanum[c] < men:
			men = listanum[c]
print('=-'*30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
	if v == mai:
		print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
	if v == men:
		print(f'{i}... ')
print()

######################################################

# Crie um programa onde o usuário possa digitar vários valores
# numéricos e cadastre-os em uma lista. Caso o número já exista
# lá dentro, ele não será adicionado. No final, serão exibidos
# todos os valores únicos digitados, em ordem crescente. 

num = list()
while True: 
	n = int(input('Digite um valor: '))
	if n not in números:
		num.append(n)
		print('Valor adicionado com sucesso...')
	else:
		print('Valor duplicado! Não vou adicionar...')
	r = str(input('Quer continuar? [S/N]'))
	if r in 'Nn':
		break 
print('-='*30)
num.sort()
print('Você digitou os valores {num}')

######################################################


# Crie um programa ondeo usuário possa digitar cinco valores
# numéricos e cadastre-os em uma lista, já na posição correta
# de inserção (sem usar o sort()). No final, mostre a lista ordenada
# na tela.  

lista = []
for c in range(0, 5):
	n = int(input('Digite um valor: '))
	if c == 0 or n > lista [-1]:
		lista.append(n)
	else:
		pos = 0 
		while pos < len(lista):
			if n <= lista[pos]:
				lista.append(pos, n)
				print(f'Adicionado na posição {pos} da lista...')
				break 
			pos += 1 
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}') 

######################################################

# Crie um programa que vai ler vários números e colocar em
# uma lista. Depois disso, mostre:
# A) Quantos números foram digitados;
# B) A lista de valores, ordenada de forma descrescente; 
# C) Se o valor 5 foi digitado e está ou não na lista. 

valores = []
while True:
	valores.append(int(input('Digite um valor: ')))
	resp = str(input('Quer continua? [S/N]'))
	if resp in 'Nn':
		break 
print('-='*30')
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem descrescente são {valores}')
if 5 in valores:
	print('O valor 5 faz parte da lista.')
else:
	print('O valor 5 não foi encontrado na lista.')

######################################################

Crie um programa que vai ler vários números e colocar em uma lista
# Depois disso, crie duas listas extras que vão conter apenas os valores 
# pares e os valores ímpares digitados, respectivamente. Ao final, mostre
# o conteúdo das três listas geradas. 

num = list()
pares = []
ímpares = []
while True:
	num.append(int(input('Digite um número: ')))
	resp = str(input('Quer continuar? [S/N]'))
	if resp in 'Nn':
		break
for i, v in enumerate(num):
	if v % 2 == 0:
		pares.append(v)
	elif v % 2 == 1:
		ímpares.append(v) 
print('-='*30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')



######################################################

# Crie um programa onde o usuário digite uma expressão
# qualquer que use parênteses. Seu aplicativo deverá analisar
# se a expressão passada está com os parênteses abertos e  
# fechados na ordem correta. 

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
	if simb == '(':
		pilha.append('(')
	elif simb == ')':
		if len(pilha) > 0:
			pilha.pop()
		else:
			pilha.append('(')
			break 
if len(pilha) == 0:
	print('Sua expressão está válida!')
else:
	print('Sua expressão está errada.')


######################################################

# listas compostas num


teste = list()
teste.append('Gustavo')
test.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)


galera = [['João', 19], ['Ana', 33]], ['Joaquim', 13], ['Maria', 45]
for p in galera:
	#print(p)
	print(f'{p[0]} tem {p[1]} anos de idade.')


galera = list()
dado = list()
for c in range(0, 3):
	dado.append(str(input('Nome: ')))
	dado.append(int(input('Idade: ')))
	galera.append(dado[:])
	dado.clear()
#print(galera)


galera = list()
dado = list()
totmai = totmen = 0 
for p in galera:
	if p[1] >= 21:
		print(f'{p[0]} é maior de idade.')
		totmai += 1 
	else:
		print(f'{p[0]} é menor de idade.')
		totmen += 1 

print(f'Temos {totmai} maiores e {totmen} menores de idade.')

######################################################

#Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas. 
# B) Uma listagem com as pessoas mais pesadas. 
# C) Uma listagem com as pessoas mais leves. 

temp = []
princ = [] 
mai = men = 0 
while True: 
	temp.append(str(input('Nome: ')))
	temp.append(float(input('Peso: ')))
	if len(princ) == 0:
		mai = men = temp[1]
	else:
		if temp[1] > mai:
			mai = temp[1]
		if temp[1] < men: 
			men = temp[1]
	princ.append(temp[:])
	temp.clear()
	resp = str(input('Quer continuar? [S/N]'))
	if resp in 'Nn':
		break
print('-='*30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
	if p[1] == mai:
		print(f'{p[0]}', end= '')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end=' )
for p in princ: 
	if p[1] == men: 
		print(f'[{p[0]}]', end='')
print()


######################################################

# Crie um programa onde o usuário possa digitar sete valores 
# numéricos e cadastre-os em uma lista única que mantenha
# separados os valores pares e ímpares. No final, mostre os 
# valores pares e ímpares em ordem crescente. 

num =[[], []]
valor = 0 
for c in range(1, 8):
	valor = int(input('Digite {c}º valor: '))
	if valor % 2 == 0:
		num[0].append(valor)
	else:
		num[1].append(valor)
print('-='*30)
#print(f'Todos os valores: {num}')
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')

######################################################

# Crie um programa que crie uma matriz de dimensão
# 3x3 e preencha com valores lidos pelo teclado.  
# No final, mostre a matriz na tela, com a formatação correta. 

matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for l in range(0, 3):
	for c in range(0, 3):
		matriz[l][c] = int(input(f'Digite um valor: '))

#print(matriz)
print('-='*30)
for l in range(0, 3):
	for c in range(0, 3):
		print(f'[{matriz[l][c]:^5}]', end='')
	print()


######################################################


# aprimore a matriz, mostrando no final 
# A) A soma de todos os valores pares digitados. 
# B) A soma dos valores da terceira coluna. 
# C) O maior valor da segunda linha. 


matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
	for c in range(0, 3):
		matriz[l][c] = int(input(f'Digite um valor: '))

#print(matriz)
print('-='*30)
for l in range(0, 3):
	for c in range(0, 3):
		print(f'[{matriz[l][c]:^5}]', end='')
		if matriz[l][c] % 2 == 0:
			spar += matriz[l][c]
	print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
	scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0, 3):
	if c == 0:
		mai = matriz[1][c]
	elif matriz[1][c] > mai:
		mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}.')

######################################################

# Faça um programa que ajude um jogador da MEGA SENA a criar
# palpites. O programa vai perguntar quantos jogos serão gerados
# e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando
# tudo em uma lista composta. 

from random import randint 
from time import sleep
lista = list()
jogos = list()
print('-'*30)
print('		JOGA NA MEGA SENA 	')
print('-='*30)
quant = int(input('Quantos jogos você quer que eu sorteie?'))
tot = 1
while tot <= quant:
	cont = 0 
	while True:
		num = randint(1, 60)
		if num not in lista:
			lista.append(num)
			cont += 1 
		if cont >= 6:
			break 
	lista.sort()
	jogos.append(lista[:])
	lista.clear()
	tot += 1 
print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3')
for i, l in enumerate(jogos):
	print(f'Jogo {i+1}: {l}}')
	sleep(2)
print('-=' * 5, '<BOA SORTE! >', '-=' *  5)


######################################################

# Crie um programa que leia nome e duas notas de vários alunos
# e guarde tudo em uma lista composta. No final, mostre um boletim
# contendo a média de cada um e permita que o usuário possa mostrar
# as notas de cada aluno individualmente. 

ficha = list()
while True:
	nome = str(input('Nome:'))
	nota1 = str(input('Nota1: ' ))
	nota2 = str(input('Nota2: '))
	media = (nota1 + nota2) / 2
	ficha.append([nome, [nota1, nota2], media])
	resp = str(input('Quer continuar? [S/N]'))
	if resp in 'Nn':
		break
print('-='*30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
	print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
	print('-' * 35)
	opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
	if opc == 999: 
		print('FINALIZANDO...')
		break 
	if opc <= len(ficha) - 1:
		print(f'Notas de {ficha[opc[0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')

######################################################

# Faça um programa que leia nome e média de 
# um aluno, guardando também a situação 
# em um dicionário. No final, mostre o 
# conteúdo da estrutura na tela. 

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
	aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
	aluno['situação'] = 'Recuperação'
else:
	aluno['situação'] = 'Reprovado'
print('-='*30)
for k, v in alunos.items():
	print(f'{k} é igual a {v}')

######################################################


# Crie um programa onde 4 jogadores joguem um dado e tenham
# resultados aleatórios. Guarde esses resultados em um dicionário.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor
# tirou o maior número no dado. 

from random import randint 
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
		'jogador2': randint(1, 6),
		'jogador3': randint(1, 6),
		'jogador4': randint(1, 6)}
ranking = dict()
print('Valores sorteados: ')
for k, v in jogo.items():
	print(f'{k} tirou {v} no dado.')
	sleep(2)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print('== 	RANKING DOS JOGADORES	==')
for i, v in enumerate(ranking):
	print(f'{i} lugar: {v[0]} com {v[1]}.')
	sleep(1)


######################################################


# Crie um programa que leia nome, ano de nascimento e carteira de trabalho
# e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente
# de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule
# e acrescente além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
idade = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
	dados['contratação'] = int(input('Ano de Contratação: '))
	dados['salário'] = float(input('Salário: R$'))
	dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-='*30)
#print(dados)
for k, v in dados.items():
	print(f'	- {k} tem o valor {v}')

######################################################

# Crie um programa que gerencie o aproveitamento de um jogador
# de futebol. O programa vai ler o nome do jogador e quantas partidas
# ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. 
# No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato. 

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
for c in range(0, tot):
	partidas.append(int(input(f'	Quantos gols na partida {c}?')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
	print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
	print(f'	=> Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')

######################################################

# Crie um programa que leia o nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os 
# dicionários em uma lista. No final, mostre: 

# A) Quantas pessoas cadastradas. 
# B) A média de idade. 
# C) Uma lista com mulheres.
# D) Uma lista com idade acima da média. 

galera = list()
pessoa = dict()
soma = média = 0 
while True:
	pessoa.clear()
	pessoa['nome'] = str(input('Nome: '))
	while True:
		pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
		if pessoa['sexo'] in 'MF':
			break 
		print('ERRO! Por favor, digite apenas M ou F.')
	pessoa['idade'] = int(input('Idade: '))
	soma += pessoa['idade']
	galera.append(pessoa.copy())
	while True:
		resp = str(input('Quer continuar? [S/N]')).upper()[0]
		if resp in 'SN':
			break
		print('ERRO! Responda apenas S ou N.')
	if resp == 'N':
		break 
print('-='*30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas')
média = soma / len(galera)
print(f'A média de idade é de {média:5.2f} anos.')
print('As mulheres cadastradas foram ', end='')
for p in galera:
	if p['sexo'] in 'Ff':
		print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
	if p['idade'] >= média:
		print('		')
		for k, v in p.items():
			print(f'{k} = {v}; ', end='')
		print()
print('<< ENCERRADO >>')


######################################################

# Aprimore o código dos jogadores de futebol, incluindo
# um sistema de visualização de detalhes do aproveitamento
# de cada jogador. 


time = list()
jogador = dict()
partidas = list()

while True:
	jogador.clear()
	jogador['nome'] = str(input('Nome do jogador: '))
	tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
	partidas.clear()
	for c in range(0, tot):
		partidas.append(int(input(f'	Quantos gols na partida {c}?')))
	jogador['gols'] = partidas[:]
	jogador['total'] = sum(partidas)
	time.append(jogador.copy())
	while True:
		resp = str(input('Quer continuar? [S/N] ')).upper()[0]
		if resp in 'SN':
			break 
		print('ERRO! Responda apenas S ou N.')
	if resp == 'N':
		break 
print('-'*30)
print('cod ', end='')
for i in jogador.keys():
	print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
	print(f'{k:>3} ', end='')
	for d in v.values():
		print(f'{str(d):<15}', end='')
	print()
print('-' * 40)
while True:
	busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
	if busca == 999:
		break
	if busca >= len(time):
		print(f'ERRO! Não existe jogador com código {busca}!')
	else:
		print(f'  --- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
		for i, g in enumerate(time[busca]['gols']):
			print(f'	No jogo {i+1} fez {g} gols')
	print('-' * 40)
print('<<VOLTE SEMPRE>>')

# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno. 


######################################################

def área(larg, comp):
	a = larg * comp 
	print(f'A área de um terreno {larg}x{comp é de {a}m².')


# Programa principal
print(' Controle de Terrenos')
print('-'*20')
l = float(input('LARGURA(m): '))
c = float(input('COMPRIMENTO(m): '))
área(l, c)

######################################################

# Faça um programa que tenha uma função chamada escreva(), 
# que receba um texto qualquer como parâmetro e mostre uma 
# mensagem com tamanho adaptável. 

def escreva(msg):
	tam = len(msg) + 4 
	print('~'*tam)
	print(f' {msg}')
	print('~'*tam)

escreva('Python prática')
escreva('Funções, classes, métodos, criar')

######################################################

# Faça um programa que tenha uma fução chamada contador(),
# que receba três parâmetros? início, fim e passo. 
# Seu programa tem que realizar três contagens através 
# da função criada:

# a) de 1 até 10, de 1 em 1 
# b) de 10 até 0, de 2 em 2 
# c) Uma contagem personalizada. 

from time import sleep

def contador(i, f, p):
	if p < 0:
		p*= -1
	if p == 0:
		p = 1


	print('-='*20)
	print(f'Contagem de {i} até {f} em {p} em {p}')
	sleep(2.5)

	if i < f:	
		cont = i 
		while cont <= f:
			print(f'{cont} ', end='', flush=True)
			sleep(0.5)
			cont += p 
		print('FIM!')
	else:
		cont = i 
		while cont >= f:
			print(f'{cont} ', end='', flush=True)
			sleep(0.5)
			cont -= p
		print('FIM!')

# programa principal 
contador(1, 10, 1)
contador(1, 100, 2)
contador(10, 0, 2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)



######################################################

# Faça um programa que tenha uma função 
# chamada maior(), que receba vários parâmetros
# com parâmetros com valores inteiros. 
# Seu programa tem que analisar todos os valores
# e dizer qual deles é o maior. 

from time import sleep

def maior(* num):
	cont = maior = 0 
	print('-='*30)
	print('\nAnalisando os valores passados...')
	for valor in num:
		print(f'{valor} ', end='', flush=True)
		sleep(0.3)
		if cont == 0:
			maior = valor 
		else:
			if valor > maior
			maior = valor 
		cont += 1 
	print(f'Foram informados {cont} valores ao todo.')
	print(f'O maior valor informado foi {maior}.')





# programa principal 
maior(2, 7, 6, 4, 7, 9)
maior(1, 5, 7, 9)
maior(1, 2)
maior(6)
maior()

######################################################

# Faça um programa que tenha uma lista chamada números e
# duas funções chamadas sorteie() e somaPar(). 
# A primeira função vai sortear 5 números e vai
# colocá-los dentro da lista e a segunda função 
# vai mostrar a soma entre todos os valores PARES 
# sorteados pela função anterior. 

from random import randint
from time import sleep

def sorteia(lista):
	print('Sorteando 5 valores da lista: ', end='')
	for cont in range(0, 5):
		n = randint(1, 10)
		lista.append(randint)
		print(f'{n} ', end='', flush=True)
		sleep(0.3)
	print('PRONTO!')



def somaPar(lista):
	soma = 0 
	for valor in lista:
		if valor % 2 == 0:
			soma += valor 
	print(f'Somando os valores pares de {lista}, temos {soma}')


números = list()
sorteia(números)
somaPar(números)


######################################################

# Crie um programa que tenha uma função chamada voto() que
# vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto 
# NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições. 




def voto(ano):
	from datetime import date 
	atual = date.today().year
	idade = atual - ano 
	if idade < 16:
		return f'Com {idade} anos NÃO VOTA.'
	elif 16 <= idade < 18 or idade > 65:
		return f'Com {idade} anos: VOTO OPCIONAL.'
	else:
		return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


nasc = int(input('Em que ano você nasceu?')
print(voto(nasc))


######################################################

#Crie um programa que tenha uma função chamada fatorial() que receba
# dois parâmetros: o primeiro que indique o número a calcular e o outro
# chamado show, que será um valor lógico(opcional) indicando se
# será mostrado ou não na tela o processo de cálculo do fatorial. 


def fatorial(n, show=False):
	"""
	-> Calcula o fatorial de um número.
	:param n: O número a ser calculado. 
	:param show: (opcional) mostrar ou não a conta
	:return: O valor do fatorial de um número n. 
	"""
	f = 1 
	for c in range(n, 0, -1):
		if show:
			print(c, end='')
			if c > 1:
				print(' x ', end='')
			else: 
				print(' = ', end='')
		f *= c 
	return f 

print(fatorial(5, show=True))
help(fatorial)


######################################################

# Faça um programa que tenha uma função chamada ficha(), que
# receba dois parãmetros opcionais: o nome de um jogador e quantos 
# gols ele marcou. O programa deverá ser capaz de mostrar 
# a ficha do jogador, mesmo que algum dado não tenha sido informado 
# corretamente. 


def ficha(jog, gol):
	print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')

# programa principal
n = str(inpit('Nome do jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
	g = int(g)
else:
	g = 0 
if n.strip() == '':
	ficha(gol=g)
else:
	ficha(n, g)


######################################################

# Crie um programa que tenha a função leiaint(), que vai funcionar
# de forma semelhante à função input() do Python, só que fazendo
# a validação para aceitar apenas um valor numérico. 
# Ex.: leiaInt('Digite um n')

def leiaInt(msg):
	ok = False
	valor = 0 
	while True:
		n = str(input(msg))
		if n.isnumeric():
			valor = int(n)
			ok = True
		else:
			print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
		if ok:
			break
	return valor

# programa principal	
n = leiaInt('Digite um número: '))
print(f'Você acabou de digitar o número {n}')

######################################################

# Fala um programa que tenha uma função notas() que pode receber
# várias notas de alunos e vai retornar um dicionário com as 
# seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota 
# - A média da turma 
# - A situação (opcional)
# Adicione também docstrings. 


def notas(*n, sit=False):
	"""
	-> Função para analisar notas e situações de vários alunos.
	:param n: uma ou mais notas dos alunos (aceita várias)
	:param sit: valor opcional, indicando se deve ou não adicionar a situação 
	:return: dicionário com várias informações sobre a situação da turma. 
	"""
	
	r = dict()
	r['total'] = len(n)
	r['maior'] = max(n)
	r['menor'] = min(n)
	r['média'] = sum(n)/len(n)
	if sit:
		if r['média'] >= 7:
			r['situação'] = 'BOA'
		elif r['média'] >= 5:
			r['situação'] = 'RAZOÁVEL'
		else:
			r['situação'] = 'RUIM'
	return r 




# programa principal 
resp = notas(9, 10, 5.5, 2.5, 9, 8.5, sit=True)
print(resp)
help(notas)


######################################################

# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer. 
# Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

#OBS.: use cores. 


from time import sleep

c = ('\033[m', 	# 0 - sem cores
	'\033[0;30;41m',  # 1 - vermelho
	'\033[0;30;42m',  # 2 - verde 
	'\033[0;30;43m',  # 3 - amarelo 
	'\033[0;30;44m',  # 4 - azul 
	'\033[0;30;45m',  # 5 - roxo 
	'\033[7;30m'	  # 6 - branco
	);


def ajuda(com):
	titulo(f'Acessando o manual do comando \'{com}\'', 4)
	print(c[6], end='')
	help(com)
	print(c[0], end='')
	sleep(2)


def título(msg, cor):
	tam = len(msg) + 4
	print(c[cor], end='')
	print('~'*tam)
	print(f ' {msg}')
	print('~'*tam)
	print(c[0], end='')
	sleep(1)


# programa principal
comando = ''
while True:
	título('SISTEMA DE AJUDA PyHELP', 2)
	comando = str(input('Função ou Biblioteca > '))
	if comando.upper() == 'FIM':
		break 
	else:
		ajuda(comando)
título('ATÉ LOGO!', 1)