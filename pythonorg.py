# EstruturaSequencial

# 1.Faça um programa que mostre a mensagem "Alo mundo", na tela.

print('Alo mundo')

# 2. Faça um programa que peça um número e então mostre a mensagem O número informado foi [número]

num = int(input('Digite um número: '))
print('O número digitado foi: {}'.format(num))
# ou print(f'O número digitado foi {num}.')

# 3. Faça um programa que peça dois números e imprima a soma.

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))

# 4. Faça um programa que peça as 4 notas bimestrais e mostre a média.

bim1 = int(input('Digite a nota do 1° bimestre: '))
bim2 = int(input('Digite a nota do 2° bimestre: '))
bim3 = int(input('Digite a nota do 3° bimestre: '))
bim4 = int(input('Digite a nota do 4° bimestre: '))

print('As notas do 1°, 2°, 3° e 4° bimestre, foram, respectivamente: {}, {}, {}, {}'.format(
    bim1, bim2, bim3, bim4))

# 5. Faça um programa que converta metros para centímetros.

m = float(input('Informe valor em metros: '))
c = m*100
print(
    f'O valor digitado em metros, convertido para centímetros, corresponde a: {c:.0f}cm')

# 6. Faça um programa que peça o raio de um círculo, calcule e mostre a sua área.

r = float(input('Informe o valor do raio do círculo: '))
a = r*(3.14)
print(f'O valor da ÁREA do círculo equivale a {a:.2f}')

# 7. Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
larg = float(input('Informe a largura do quadrado: '))
alt = float(input('Informe a altura do quadrado: '))
quad_area = larg*alt
area_dobro = quad_area*2
print(
    f'A área do quadrado corresponde a {quad_area}m² e o dobro da área é {area_dobro}m²')


# 8. Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

hora = float(input('Quanto você ganha por hora? '))
horas_mes = float(input('Quantas horas trabalha por mês? '))
salario = hora*horas_mes
print(
    f'Você ganha R${hora:.2f} por hora, trabalhando {horas_mes:.0f} horas por mês, o seu salário é de R${salario:.2f}')

# 9. Faça um programa que peça a temperatura em graus Fahrenheit, transforme e msotre a temperatura em graus Celsius.
# C = 5*((F-32/9))

fahr = float(input('Informe a temperatura em fahrenheit: '))
cel = 5*(fahr-32)//9
print(f'A temperatura {fahr}°F convertida para Celsius é {cel}°C. ')

# 10. Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# F = 9*(C//5)+32

celsius = float(input('Digite a temperatura em graus °Celsius: '))
fahr = (9*celsius)//5+32
print(f'A temperatura °C{celsius} informada, convertida para fahreinheit, corresponde a °F{fahr}')

# 11. Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:
#   a. O produto do dobro do primeiro com metade do segundo. 
#   b. A soma do triplo do primeiro com o terceiro. 
#   c. O terceiro elevado ao cubo. 

num1 = int(input('Digite o 1° valor inteiro: '))
num2 = int(input('Digite o 2° valor inteiro: '))
num3 = float(input('Digite o 3° valor real: '))

print(f'O produto do dobro do primeiro com metade do segundo é {num1*2} e a soma do triplo do primeiro com o terceiro é {num1*3} e o terceiro elevado ao cubo é {num1**3}')



# 12. Tendo como dados de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmula:
#   a. Para homens: (72.7*h) - 58

h = float(input('Digite a altura em metros: '))
peso = (72.7*h) - 58
print(f'O seu peso ideal é de {peso:.2f}kg')


# 13. Tendo como dados de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmula:
#   a. Para homens: (72.7*h) - 58
#   b. Para mulheres: (62.1*h) - 44.7

h = float(input('Digite a altura em metros: '))
pesohomem = (72.7*h) - 58
pesomulher = (62.1*h) - 44.7
print(f'O peso ideal para mulheres é de {pesomulher:.2f}kg')
print(f'O peso ideal para homens é de {pesohomem:.2f}kg')

# 14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
# (50 quilos) deve pagar uma multa de R$ 4.00 por quilo excedente. João precisa que você faça um programa que leia a 
# variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite
# e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

print("/tJoão Papo-de-Pescador/n")

peso = float(input("Peso: "))
excesso = 0 
multa = 0 

if peso <= 50:
    print("Excesso: %.2f" %excesso)
    print("Multa: %.2f" %multa)
else:
    excesso = peso - 50
    multa = excesso * 4.00
    print("Excesso: %.2f" %excesso)
    print("Multa: %.2f" %multa)





# 15. Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre
# o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS
# e 5% para o sindicato, faça um programa que nos dê:
#   a. salário bruto 
#   b. quanto pagou ao INSS.
#   c. quanto pagou ao sindicato. 
#   d. o salário líquido. 
#   e. calcule os descontos e o salário líquido. Obs.: salário bruto - descontos = salário líquido.

ganhahora = float(input("Quanto você ganha por hora? "))
horasmês = float(input("Quantas horas trabalhadas no mês? "))
salario = ganhahora * horasmês
imposto = salario * 0.11
inss = salario * 0.08
sindicato = salario * 0.05

print(f"Salário bruto: R${salario:.2f}")
print(f"Imposto de Renda: R${imposto:.2f}")
print(f"INSS: R${inss:.2f}")
print(f"Sindicato: R${sindicato:.2f}")
print(f"Salário líquido: R${salario - (imposto + inss + sindicato):.2f}")

# 16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80.00. Informe ao usuário a quantidade de latas de tinta a serem compradas e o preço total. 

tamanho = float(input('Quantos metros quadrados devem ser pintados: '))

litros = tamanho / 3.0 
latas = int(litros / 18.0)
if litros % 18 != 0:
    latas += 1 

print('Você deverá comprar', latas, 'latas.')
print('O valor total é:', latas * 80)



# 17. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80.00 ou em galões de 3.6 litros, que custam R$ 25.00. 

# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas gações de 3.6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde
# os valores para cima, isto é, considere latas cheias. 

tamanho = float(input('Digite o tamanho da área: '))

litros = tamanho / 6.0
latas = int(litros / 18)
if litros % 18 != 0:
    latas += 1
preço = latas * 80

galões = litros / 3.6 
if galões % 3.6 != 0:
    galões += 1
preço2 = galões * 25

# mistura de latas e galões 
mistura_lata = int(litros / 18.0)
mistura_galão = int((litros - (mistura_lata * 18)) / 3.6)

if litros - (mistura_lata * 18) % 3.6 != 0:
    mistura_galão += 1

print('Apenas latas de 18 litros: %d' % latas, 'preço: %d' % preço)
print('Apenas galões de 3.6 litros: %d' % galões, 'preço: %d' % preço2)
print('Mistura: %d latas e %d galões = %.2f' % (
    mistura_lata, mistura_galão, ((mistura_lata * 80)) + (mistura_galão * 25)))

# 18. Faça um programa qe peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho = float(input('Tamanho do arquivo (MB): ')
velocidade = float(input('Velocidade de internet (MBps): '))
print('Tempo aproximado de download: %.0f Minutos ' %((tamanho / velocidade) *))

# ------------------------------------------------- - --------------------------------------------------------


# Estrutura de Decisão 

# 1. Faça um programa que peça dois números e imprima o maior deles. 

num1 = float(input('Digite o primeiro número: '))  
num2 = float(input('Digite o segundo número: '))
if num 1 > num 2:
    print(f'O número digitado {num1} é maior do que o segundo número.')
elif num2 < num1:
    print(f'O número digitado {num2} é maior do que o primeiro número.')
else:
    print(f'Os números digitados {num1} e {num2} são iguais.')

# 2. Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor = float(input('Informe um valor: '))
if valor > 0:
    print(f'O valor informado {valor} é positivo.')
elif valor < 0:
    print(f'O valor informado {valor} é negativo.')
elif valor == 0:
    print(f'O valor informado {valor} é zero.')

# 3. Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
# F - Feminino, M - Masculino, Sexo Invlálido. 

check = input('Digite F para Feminino ou M para Masculino: ')
if check == 'F':
    print('Sexo Feminino')
elif check == 'M':
    print('Sexo Masculino')
else:
    print('Sexo Inválido')

# 4. Faça um programa que verifique se uma letra digitada é vogal ou consoante. 

letra = input('Digite uma letra: ').lower()
if letra in 'aeiou':
    print('Vogal')
else:
    print('Consoante')


# 5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média
# alcançada por aluno e apresentar:
#   A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#   A mensagem "Reprovado", se a média for menos do que sete;
#   A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input('Informe o valor da 1ª nota: '))
nota2 = float(input('Informe o valor da 2° nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print('Aprovado com Distinção')
elif media >= 5:
    print('Aprovado')
else:
    print('Reprovado')

# 6. Faça um programa que leia três números e mostre o maior deles.

num1 = float(input('Digite o 1° número: '))
num2 = float(input('Digite o 2° número: '))
num3 = float(input('Digite o 3° número: '))
if num1 > num2 and num1 > num3:
    print(f'O maior número é {num1}')
elif num2 > num1 and num2 > num3:
    print(f'O maior número é {num2}')
else:
    print(f'O maior número é {num3}')

# 7. Faça um programa que leia três números e mostre o maior e o menor deles.

num1 = float(input('Digite o 1° número: '))
num2 = flaot(input('Digite o 2° número: '))
num3 = float(input('Digite o 3° número: '))

if num1 > num2 and num1 > num3:
    print(f'O maior número é {num1}')
elif num2 > num1 and num2 > num3:
    print(f'O maior número é {num2}')
else:
    print(f'O maior número é {num3}')

if num1 < num2 and num1 < num3:
    print(f'O menor número é {num1}')
elif num2 < num1 and num2 < num3:
    print(f'O menor número é {num2}')
else:
    print(f'O menor número é {num3}')

# 8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato. 

produto1 = float(input('Qual o preço do 1° produto? '))
produto2 = float(input('Qual o preço do 2° produto? '))
produto3 = float(input('Qual o preço do 3° produto? '))

if produto1 < produto2 and produto1 < produto3:
    print(f'O menor preço é {produto1}')
elif produto2 < produto1 and produto2 < produto3:
    print(f'O menor preço é {produto2}')
else:
    print(f'O menor preço é {produto3}')


# 9. Faça um programa que leia três números e mostre-os em ordem decrescente. 

num1 = float(input('Digite o 1° número: '))
num2 = float(input('Digite o 2° número: '))
num3 = float(input('Digite o 3° número: '))

print(f'Os números digitados foram: {num1}, {num2}, {num3}...')
sorted_numbers = sorted([num1, num2, num3], reverse=True)
print(f'Em ordem decrescente: {sorted_numbers[0]}, {sorted_numbers[1]}, {sorted_numbers[2]}')


# 10. Faça um programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-vespertino ou N-Noturno.
# Imprima a mensagem "Bom dia!", "Boa tarde!" ou "Boa noite!" ou "Valor Inválido!", conforme o caso. 

turno = input('Em que turno você estuda? (M - Matutino; V - Vespertino; N - Noturno)' )
if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa noite!')
else:
    print('Valor Inválido!')

# 11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores para desenvolver o programa
# que calculará os reajustes.
#   Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
#   baseado no salário atual:
#   salários até R$ 280.00 (incluindo): aumento de 20%
#   salários entre R$280.00 e R$700.00: aumento de 15%
#   salários entre R$700.00 e R$1500.00: aumento de 10%
#   salários de R$ 1.500.00 em diante: aumento de 5%. Após o aumento ser realizado, informe na tela:
#   o salário antes do reajuste
#   o percentual de aumento aplicado 
#   o valor do aumento
#   o novo salário, após o aumento. 

salario = float(input('Digite o seu salário: '))

valor_baixo = salario * 0.20 
valor_medio = salario * 0.15
valor_alto = salario * 0.10
valor_acima = salario * 0.05

if salario <= 280.00:
    print(f'O seu salário antes do reajuste é de R${salario:.2f} e o percentual de aumento aplicado é de 20%') 
elif salario > 280.00 and salario <= 700.00:
    print(f'O seu salário antes do reajuste é de R${salario:.2f} e o percentual de aumento aplicado é de 15%')
elif salario > 700.00 and salario <= 1500.00:
    print(f'O seu salário antes do reajuste é de R${salario:.2f} e o percentual de aumento aplicado é de 10%')
elif salario > 1500.00:
    print(f'O seu salário antes do reajuste é de R${salario:.2f} e o percentual de aumento aplicado é de 5%')

else:
    print('Valor Inválido!') 


# 12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
# que depende do salário bruto (conforme tabela) e 3% para o Sindicato e que o FGTS corresponde a 11% do salário bruto,
# mas não é descontado ( é a empresa que deposita). O salário líquido corresponde ao salário bruto menos os descontos.
# O programa deverá pedir ao usuário o valor de sua hora e a quantidade de horas trabalhadas no mês:
#   Desconto do IR:
#   Salário bruto até 900 (inclusive) - isento 
#   Salário bruto até 1500 (inclusive) - desconto de 5%
#   Salário bruto até 2500 (inclusive) - desconto de 10%
#   Salário bruto acima de 2500 - desconto de 20%. Imprima na tela as informações, dispostas conforme o exemplo.
#   No exemplo o valor da hora é 5 e a quantidade de hora é 220. 

valor_da_hora = float(input("Digite quanto você recebe por hora: "))
horas_trabalhadas = float(input("Digite quantas horas você trabalhou esse mês: "))
salario_bruto = valor_da_hora * horas_trabalhadas
if salario_bruto <= 900:
    desconto_ir = 0.0 
elif salario_bruto > 900 and salario_bruto <= 1500:
    desconto_ir = 0.05
elif salario_bruto > 1500 and salario_bruto <= 2500:
    desconto_ir = 0.10
elif salario_bruto > 2500:
    desconto_ir = 0.20

IR = salario_bruto * (desconto_ir / 100)
INSS = salario_bruto * (10 / 100)
FGTS = salario_bruto * (11/100)
total_de_descontos = IR + INSS 
salario_liquido = salario_bruto - total_de_descontos

print(
    f"\nSalário Bruto       : R${salario_bruto:.2f}",
    f"\n(-) IR (5%)         : R${IR:.2f}",
    f"\n(-) INSS (10%)       : R${INSS:.2f}",
    f"\n(-) FGTS (11%)       : R${FGTS:.2f}",
    f"\n(-) Total de descontos: R${total_de_descontos:.2f}",
    f"\n(-) Salário líquido  : R${salario_liquido:.2f}"
)

# 13. Faça um programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2-Segunda, 3-Terça, 4-Quarta,
# 5-Quinta, 6-Sexta, 7-Sábado), se digitar outro valor, deve aparecer valor inválido. 

num = input('Digite um número de 1 a 7 para um dia da semana: ')
if num == 1:
    print('Domingo')
elif num == 2:
    print('Segunda')
elif num == 3:
    print('Terça')
elif num == 4:
    print('Quarta')
elif num == 5:
    print('Quinta')
elif num == 6:
    print('Sexta')
elif num == 7:
    print('Sábado')
else:
    print('Valor Inválido!')


# 14 - Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de aproveitamento Conceito
# Entre 9.0 e 10.0          A
# Entre 7.5 e 9.0           B
# Entre 6.0 e 7.5           C
# Entre 4.0 e 6.0           D
# Entre 4.0 e 0             E 

nota1 = float(input('Digite o valor da 1° nota: '))
nota2 = float(input('Digite o valor da 2° nota: '))
media = (nota1 + nota2) / 2

if media >= 9.0 and media <= 10.0:
    conceito = 'A'
elif media >= 7.5 and media <= 9.0:
    conceito = 'B'
elif media >= 6.0 and media <= 7.5:
    conceito = 'C'
elif media >= 4.0 and media <= 6.0:
    conceito = 'D'
elif media <= 4.0:
    conceito = 'E'
else:
    conceito = 'Valor Inválido!'

if conceito == 'A':
    print(f'A sua média foi de {media:.1f} e você foi aprovado com conceito {conceito}')
elif conceito == 'B':
    print(f'A sua média foi de {media:.1f} e você foi reprovado com conceito {conceito}')
elif conceito == 'C':
    print(f'A sua média foi de {media:.1f} e você foi reprovado com conceito {conceito}')
elif conceito == 'D':
    print(f'A sua média foi de {media:.1f} e você foi reprovado com conceito {conceito}')
elif conceito == 'E':
    print(f'A sua média foi de {media:.1f} e você foi reprovado com conceito {conceito}')
else:
    print('Valor Inválido!')


# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem "APROVADO" se o conceito 
# for A, B ou C ou "REPROVADO" se o conceito for D ou E. 


nota1 = float(input('Digite o valor da 1° nota: '))
nota2 = float(input('Digite o valor da 2° nota: '))
media = (nota1 + nota2) / 2

if media >= 9.0 and media <= 10.0:
    conceito = 'A'
    print(f'A sua média foi de {media:.1f} e você foi aprovado com conceito {conceito}')
elif media >= 7.5 and media <= 9.0:
    conceito = 'B'
    print(f'A sua média foi de {media:.1f} e você foi aprovado com conceito {conceito}')
elif media >= 6.0 and media <= 7.5:
    conceito = 'C'
    print(f'A sua média foi de {media:.1f} e você foi aprovado com conceito {conceito}')
elif media >= 4.0 and media <= 6.0:
    conceito = 'D'
    print(f'A sua média foi de {media:.1f} e você foi reprovado com conceito {conceito}')
elif media <= 4.0:
    conceito = 'E'
    print(f'A sua média foi de {media:.1f} e você foi reprovado com conceito {conceito}')



# 15. Faça um programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. 
#   Dicas:
#   Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#   Triângulo Equillátero: três lados iguais;
#   Triângulo Isósceles: quaisquer dois lados iguais;
#   Triângulo Escaleno: Três lados diferentes;

l1 = int(input("Lado 1: "))
l2 = int(input("Lado 2: "))
l3 = int(input("Lado 3: "))

if l1 > (l2 + l3) or l2 > (l1 + l3) or l3 > (l1 + l2):
        print("Não é um triângulo")
elif l1 == l2 == l3:
        print("É um triângulo Equilátero")
elif l1 == l2 or l1 == l3 or l2 == l3:
        print("É um triângulo Isósceles")
else:
        print("É um triângulo Escaleno")



# 16. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir
# os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#   a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer 
#   pedir os demais valores, sendo encerrado;
#   b. Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário e encerre o programa.
#   c. Se p delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#   d. Se o delta for positivo, a equação possui duas raízes reais; informe-as ao usuário;

import math 
a = float(input("Digite A: "))
if a == 0:
    print("Não é uma equação do segundo grau.")
else:
    b = float(input("Digite B: "))
    c = float(input("Digite C: "))

delta = (b ** 2) - (4 * a * c)

if delta < 0:
    print("A equação não possui raízes reais.")
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
if delta == 0:
        print("1 Raiz real: ", x1)
else:
        print("2 Raizes reais, x1: ", x1, "\nx2: ", x2)


# 17. Faça um programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano = int(input("Digite um ano: "))
if ano % 4 == 0:
    print(f"{ano} é bissexto!")
else:
    print(f"{ano} não é bissexto!")


# 18. Faça um programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

if dia > 31 or dia < 1 or mes > 12 or mes < 1 or ano > 2020 or ano < 1900:
    print("Data inválida!")
else:
    print(f" A data digitada {data}/{mes}/{ano} é válida!")

# 19. Faça um programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
#   Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#   326 = 3 centenas, 2 dezenas, 6 unidades.
#   12 = 1 dezena e 2 unidades.
#   Testar com: 326, 300, 100, 320, 310, 305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16.

for numero in [
    326,
    300,
    100,
    320,
    310,
    305,
    301,
    101,
    311,
    111,
    25,
    20,
    10,
    21,
    11,
    1,
    7,
    16
]:
    print(f"\nNúmero: {numero}")
    unidade = numero % 10 
    dezena = (numero % 100) // 10 
    centena = numero // 100 
    separador1 = ""
    separador2 = ""
    # Se tivermos ambos unidade, dezena e centena
    if centena > 0 and dezena > 0 and unidade > 0:
        separador1 = " , "
        separador2 = " e "
    # Senão, se tivermos uma centena e uma dezena
    elif centena > 0 and dezena > 0:
        separador1 = " e "
        separador2 = ""
    # Já se tivermos só a centena e a unidade, ou só a dezena e a unidade
    elif (centena > 0 and unidade > 0) or (dezena > 0 and unidade > 0):
        separador1 = ""
        separador2 = " e "
    
    #Se a centena não estiver zerada
    if centena > 0:
        if centena == 1:
            centana = "1 centena"
        else:
            centena = f"{centena} centenas"
    else:
        centena = ""
    
    if dezena > 0:
        if dezena == 1:
            dezena = "1 dezena"
        else:
            dezena = f"{dezena} dezenas"
    else:
        dezena = ""
    
    if unidade > 0:
        if unidade == 1:
            unidade = "1 unidade"
        else:
            unidade = f"{unidade} unidades"
    else:
        unidade = ""

    print(f"{centena}{separador1}{dezena}{separador2}{unidade}")

     
    

# 20. Faça um programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno
#   e apresentar:

#   a. A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#   b. A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#   c. A mensagem "Aprovado com Distinção", se a média for igual a 10. 


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2 

if media >= 7 and media < 10:
    print("APROVADO!")
elif media < 7:
    print("REPROVADO!")
else:
    print("APROVADO com DISTINÇÃO")




# 21. Faça um programa para um caixa eletrônico. O programa deverá perguntar ao usuário o valor ndo saque e depois informar
# quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é
# de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#   a. Exemplo 1: para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5
# e uma nota de 1.
#   b. Exemplo 2: para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
#   uma nota de 5 e quatro notas de 1. 

valor = int(input("Digite o valor a ser sacado (entre 10 e 600): "))
if (valor < 10 or valor > 600):
    print("Valor inválido!")
else:
    cem = valor // 100 
    valor -= cem * 100 
    cinquenta = valor // 50 
    valor -= cinquenta * 50 
    dez = valor // 10 
    valor -= dez * 10
    cinco = valor // 5 
    valor -= cinco * 5 
    um = valor 
    if cem > 0:
        print(f"{cem} nota(s) de cem")
    if cinquenta > 0:
        print(f"{cinquenta} nota(s) de cinquenta")
    if dez > 0:
        print(f"{dez} nota(s) de dez")
    if cinco > 0:
        print(f"{cinco} nota(s) de cinco")
    if um > 0:
        print(f"{um} nota(s) de um")        

# 22. Faça um programa que peça um número inteiro e determine se ele é par ou ímpar. Dica: utilize o operador módulo
# (resto da divisão).

num = int(input('Digite um número inteiro: '))
if num 2 % 0:
    print(f'O número digitado {num} é par')
elif num 2 % 1:
    print(f'O número digitado {num} é ímpar')
else:
    print('Erro')




# 23. Faça um programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

numero = float(input("Digite um número: "))
if numero % 1 == 0:
    print("Inteiro")
else;
    print("Decimal")

# 24. Faça um programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado
# da operação deve ser acompanhado de uma frase que diga se o número é:
#   a. par ou ímpar;
#   b. positivo ou negativo;
#   c. inteiro ou decimal. 

numero1 = float(input("Digite o número 1: "))
numero2 = float(input("Digite o número 2: "))
operacao = input("Digite a operação que deseja realizar: [+, -, /, *]: ")

def checar():
    if (resultado_operacao // 1 == resultado_operacao):
        print("Inteiro")
        if resultado_operacao % 2 == 0:
            print("Par")
            if resultado_operacao > 0:
                print("Positivo")
            else:
                print("Negativo")
        else:
            print("Ímpar")
    else:
        print("Decimal")

if operacao == '+':
    resultado_operacao = numero1 + numero2
    print("Resultado: ", resultado_operacao)
    checar()
elif operacao == '-':
    resultado_operacao = numero1 - numero2
    print("Resultado: ", resultado_operacao)
    checar()
elif operacao == '/':
    resultado_operacao = numero1 / numero2 
    print("Resultado: ", resultado_operacao)
    checar()
elif operacao == '*':
    resultado_operacao = numero1 * numero2
    print("Resultado: ", resultado_operacao)
    checar()
else:
    print("Valor Inválido!")


# 25. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#   a. "Telefonou para a vítima?"
#   b. "Esteve no local do crime?"
#   c. "Mora perto da vítima?"
#   d. "Devia para a vítima?"
#   e. "Já trabalhou com a vítima?"
#   O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
#   Se a pessoa responder positivamente a 2 questões, ela deve ser classificada como "Suspeita",
#   entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado 
#   como "Inocente".

positivos = 0 
resposta = input("Telefonou para a vítima? (S ou N): ")
if resposta.upper() == 'S':
    positivos += 1
resposta = input("Esteve no local do crime? (S ou N): ")
if resposta.upper() == 'S':
    positivos += 1 
resposta = input("Mora perto da vítima? (S ou N): ")
if resposta.upper == 'S':
    positivos += 1 
resposta = input("Devia para a vítima? (S ou N): ")
if resposta.upper == 'S':
    positivos += 1 
resposta = input("Já trabalhou com a vítima? (S ou N): ")
if resposta.upper == 'S':
    positivos += 1 

if positivos < 2:
    print("Inocente")
elif positivos == 2:
    print("Suspeita")
elif positivos < 5:
    print("Cúmplice")
else:
    print("Assassino")



# 26. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#   a. Álcool;
#   b. até 20 litros, desconto de 3% por litro;
#   c. acima de 20 litros, desconto de 5% por litro;
#   d. Gasolina:
#   e. até 20 litros, descontos de 4% por litro:
#   f. acima de 20 litros, desconto de 6% por litro.
#   Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma:
#   A - álcool, G - gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro
#   da gasolina é R$2.50 e o preço do álcool é R$ R$1.90

litros = float(input("Digite quantos litros você quer abastece: "))
combustivel = input("Digite A para álcool ou G para gasolina: ")
preço = 0 
if combustivel == "A" or combustivel == "a":
    preço = litros * 1.9 
    if litros <= 20:
        preço -= 1.9 * litros * 3 / 100 
    else:
        preço -= 1.9 * litros * 5 / 100 
elif combustivel == "G" or combustivel == "g":
    preço = litros * 2.5
    if litros <= 20:
        preço -= 2.5 * litros * 4 / 100 
    else:
        preço -= 2.5 * litros * 6 / 100 
print(f"O preço a pagar é R${preço:.2f}")


# 27. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#           Até 5kg             Acima de 5kg
# Morango   R$2.50 por kg       R$2.20 por kg
# Maçã      R$.1.80 por kg      1.50 por Kg

# Se o cliente comprar mais de 8kg em frutas ou o valor total da compra ultrapasssar R$25.00, receberá ainda um desconto
# de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maçãs
# adquiridas e escreva o valor a ser pago pelo cliente.

morangos = int(input("Digite a quantidade de morangos [kg]: "))
macas = int(input("Digite a quantidade de maçãs [kg]: "))
preco_morango1 = morangos * 2.50 
preco_morango2 = morangos * 2.20

preco_maca1 = macas * 1.80
preco_maca2 = macas * 1.50 

print("Quantidade de maçãs: ", macas, "\nQuantidade de morangos: ", morangos)

if morangos > 5:
    preco_certo_morango = preco_morango1
else:
    preco_certo_morango = preco_morango2

if macas > 5:
    preco_certo_maca = preco_maca1
else:
    preco_certo_maca = preco_maca2

preco_total = preco_certo_maca + preco_certo_morango 

if preco_total > 25 or (macas + morangos) > 8:
    print("Preço final: ", (preco_total - (preco_total * 0.1)))
else:
    print("Preço final: ", preco_total)


# 28. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#       Até 5Kg                 Acima de 5Kg
#  Filé Duplo   R$4.90 por Kg   R$5.90 por Kg
#  Alcatra      R$5.90 por Kg   R$6.80 por Kg
#  Picanha      R$6.90 por Kg   R$7.80 por Kg

# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
# porém não há limites para a quantidade de carne por cliente. Se a compra for feita no cartão Tabajara,
# o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo
# e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra:
# tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar. 

print("1- Filé Duplo\n2- Alcatra\n3- Picanha\n\n")
tipo = int(input("Digite o tipo: "))
quantidade = int(input("Digite a quantidade comprada: "))
resposta = int(input("A compra será realizada com cartão Tabajara? 1p/ SIM - 2p / NÃO: "))

if tipo == 1:
    nome = "Filé Duplo"
    if quantidade <= 5:
        preco = quantidade * 4.90 
    else:
        preco = quantidade * 5.80 
    
if tipo == 2:
    nome = "Alcatra"
    if quantidade <= 5:
        preco = quantidade * 5.90 
    else: 
        preco = quantidade * 6.80 

if tipo == 3:
    nome = "Picanha"
    if quantidade <= 5:
        preco = quantidade * 6.90 
    else:
        preco = quantidade * 7.80

if resposta == 1:
    r = "SIM"

    desconto = ((preco * 5) / 100)
    total = preco - desconto 
else:
    r = "NÃO"
    total = preco 

print("\n******************** CUPOM FISCAL ***************************")
print("* Carne ............................................. %s " %nome)
print("* Quantidade ........................................ %d KG " %quantidade)
print("* Preço ............................................. %.2f R$" %preco)
print("*Cartão Tabajara..................................... %s " %r)
print("* Total com desconto................................. %.2f R$ " %total)
print("*********************************************************************")

# ------------------------------------------------- - --------------------------------------------------------

# Estrutura de Repetição

# 1 - Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido
# e continue pedindo até que o usuário informe um valor válido.


num = int(input('Digite um número entre 0 e 10: '))
while (nota>10) or (nota<0):
    nota = int(input('Digite um número entre 0 e 10: '))



# 2- Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

print("-=*10\n\tCadastro\t\n-=*10")
usuario = str(input("usuário: "))
senha = str(input("senha: "))
while usuario == senha:
    print("ERRO: o usuário não pode ser igual a senha, tente novamente")
    usuario = str(input("usuário: "))
    senha = str(input("senha: "))
else:
    print("Cadastrado com sucesso")

# 3 - Faça um programa que leia e valide as seguintes informações:
#   a. Nome: maior que 3 caracteres;
#   b. Idade: entre 0 e 150;
#   c. Salário: maior que zero;
#   d. Sexo: 'f' ou 'm';
#   e. Estado Civil: 's', 'c', 'v', 'd';

nome = str(input("Informe um nome: "))
while(len(nome) <= 3):
    nome = str(input("Informe um nome: "))

idade = int(input("Informe a idade: "))
while(idade > 150 or idade < 0):
    idade = int(input("Informe a idade: "))

salario = float(input("Informe um salário: "))
while (salario < 0):
    salario = float(input("Informe um salário: "))

sexo = str(input("Informe sexo, F ou M: ")).lower()
while sexo != "f" and sexo != "m":
    sexo = str(input("Informe sexo, F ou M: "))

estado_civil = str(input("Informe estado civil (S, C, V ou D): ")).lower()
while(estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d"):
    estado_civil = str(input("Informe estado civil (S, C, V ou D): "))


# 4. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
# e que a população B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e 
# escreva o número de anos necessários para que a população dos país A ultrapasse ou igualge a população do país B,
# mantidas as taxas de crescimento. 

populaçãoA=80000
populaçãoB=200000
ano=0
while populaçãoA < populaçãoB:
    populaçãoA += round((populaçãoA*3.0)/100)
    populaçãoB += round((populaçãoB*1.5)/100)
    ano=ano+1

print("Levará", ano, "anos para população da cidade A ser maior que a cidade B")
print("População B -->", populaçãoB, "habitantes")
print("População A -->", populaçãoA, "habitantes")



# 5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a 
# entrada e permita repetir a operação. 

populaçãoA=float(input("Informe a população da cidade A: "))
populaçãoB=float(input("Informe a população da cidade B: "))
ano=0
taxa_crescimentoA=float(input("Informe a taxa de crescimento da população da cidade A: "))
taxa_crescimentoB=float(input("Informe a taxa de crescimento da população da cidade B: "))
while populaçãoA < populaçãoB:
    populaçãoA+=round((populaçãoA*taxa_crescimentoA)/100)
    populaçãoB+=round((populaçãoB*taxa_crescimentoB)/100)
    ano=ano+1

print("Levará", ano, "anos para população da cidade A ser maior que a cidade B")
print("População B -->", populaçãoB, "habitantes")
print("População A -->", populaçãoA, "habitantes")


# 6. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que
# ele mostre os números um ao lado do outro. 

for i in range(21):
    print(i)
print(list(range(1, 21)))

# 7. Faça um programa que leia 5 números e informe o maior número. 

num1 = float(input("Digite o 1° número: "))
num2 = float(input("Digite o 2° número: "))
num3 = float(input("Digite o 3° número: "))
num4 = float(input("Digite o 4° número: "))
num5 = float(input("Digite o 5° número: "))
if (num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5):
    print("O maior número é o 1°: ", num1)
if (num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5):
    print("O maior número é o 2°: ", num2)
if (num3 > num2 and num3 > num1 and num3 > num4 and num3 > num5):
    print("O maior número é o 3°: ", num3)
elif (num4 > num2 and num4 > num3 and num4 > num1 and num4 > num5):
    print("O maior número é o 4°: ")
else:
    print("O maior número é o 5°: ")


# 8. Faça um programa que leia 5 números e informe a soma e a média dos números.

num1 = float(input("Digite o 1° número: "))
num2 = float(input("Digite o 2° número: "))
num3 = float(input("Digite o 3° número: "))
num4 = float(input("Digite o 4° número: "))
num5 = float(input("Digite o 5° número: "))

soma = num1 + num2 + num3 + num4 + num5
print("Soma-> ", soma)
print("Média--> ", soma/5)

# 9. Faça um programa que imprima na tela apenas os números impares entre 1 e 50.

for i in range(1, 51, 2):
    print(i)

# 10. Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
while num2 < num1:
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
else:
    for i in range(num1, num2, 1):
        print(i)

# 11. Altere o programa anterior para mostrar no final a soma dos números.

início = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))
soma = 0 
while (início < fim -1):
    início = início + 1 
    print(início)
    soma = início + soma 

print("A soma dos intervalos é = ", soma)


# 12. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
# O usuário deve informar de qual número ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

# Tabuada de 5: 
# 5 x 1 = 5 
# 5 x 2 = 10 
# ... 
# 5 x 10 = 50 

while 1 == 1:
    tabuada = int(input("Informe a tabuada que você deseja ver: "))
    numero = tabuada 
    contador = 0 
    while (contador <= 9):
        contador = contador + 1 
        print(numero, "*", contador, "=", tabuada)
        tabuada = tabuada + numero 

# 13. Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
# Não utilize a função de potência da linguagem.

base = int(input("Informe a base: \n"))
expoente = int(input("Informe o expoente: \n"))
acumulador = 1 
for c in range (0, expoente):
    acumulador = base * acumulador
print("Resultado = ", acumulador)

# 14. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de 
# números ímpares.

print("Calcular quantidade de números ímpares e pares")
par = 0 
ímpar = 0 
for i in range(10):
    numero = int(input("Digite um número: "))
    if(numero % 2 = 0):
        par = par + 1 
    else:
        ímpar = ímpar + 1 
print("Temos", par, "números pares")
print("Temos", ímpar, "números ímpares")

# 15. A série de Fibonacci é formada pela sequência 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
# Faça um programa capaz de gerar a série até o n-ésimo termo. 

Fibonacci = eval(input("informe o final da seqüência-->")) 
x, y = 1, 1
for c in range(Fibonacci):
    print (x)
    soma = x + y
    x,y = y,soma + y 
    
# 16. A série de Fibonacci é formada pela sequência 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
# Faça um programa que gere a série até que o valor seja maior que 500. 

x, y = 1, 1 
while ( x < 600):
    print(x)
    soma = x + y 
    x, y = y, soma 

# 17. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
# Ex.: 5! = 5.4.3.2.1 = 120 

numero = int(input("Informe um numero: "))
fatorial = numero 
while fatorial > 1:
    fatorial = fatorial - 1 
    numero = numero*fatorial 
    print(numero)

# 18. Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

quantidade = int(input("Indique a quantidade de números que deseja: "))
valor = int(input("Digite um número: "))
maior = valor 
menor = valor 
soma = valor 
contador = 0 
while contador < quantidade - 1:
    valor = int(input("Digite outro número: "))
    soma = valor + soma 
    contador = contador + 1 
    if valor > maior:
        maior = valor 
    elif valor < menor:
        menor = valor 
print("O menor valor é --> ", menor)
print("O maior valor é -->", maior)
print("Soma = ", soma)


# 19. Altere o programa anterior para que ele aceite apenas números entre 0 a 1000. 

quantidade = int(input("Indique a quantidade de números: "))
valor = int(input("Digite um número: "))
while valor < 0 or valor > 1000:
    valor = int(input("Valor não aceito, digite um número: "))
else:
    maior = valor 
    menor = valor 
    soma = valor 
    contador = 0 
    while contador < quantidade - 1:
        valor = int(input("Digite outro número: "))
        while valor < 0 or valor > 1000:
            valor = int(input("Valor não aceito, digite outro número: "))
        else:
            soma = valor + soma 
            contador = contador + 1 
            if valor > maior:
                maior = valor 
            elif valor < menor:
                menor = valor 
print("O menor valor é: ", menor)
print("O maior valor é: ", maior)
print("Soma = ", soma)

# 20. Altere o programa de cálculo fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial
# a números inteiros positivos e menores que 16.

while 1 == 1:
    numero = int(input("Informe um número: "))
    while numero > 16 or numero < 0:
        numero = int(input("Número incorreto, informe outro número: "))
    else:
        contar_multiplicador = numero 
        while contar_multiplicador > 1:
            contar_multiplicador = contar_multiplicador - 1 
            numero = numero * contar_multiplicador
            print(numero)

# 21. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que 
# é divisível somente por ele mesmo e por 1. 

num = int(input("Digite um número: "))
contaresto = 0 
for c in range(1, num+1):
    resto = num % c 
    if resto == 0:
        contaresto = contaresto + 1 
if contaresto == 1 or contaresto == 2:
    print(num, "é primo")
else:
    print(num, "não é primo")


# 22. Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais números ele é divisível.

numero = int(input("Digite um número inteiro: "))
primo = True 
for i in range(2, numero):
    if numero % i == 0:
        primo = False 
        print(f"{numero} não é primo! É divisível por {i}.")
if primo:
    print(f"{numero} é primo!")


# 23. Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro forncecido pelo usuário. O programa deverá
# mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo 
# e o número de testes (divisões) executados.

numero = int(input("Digite um número inteiro: "))
if numero == 1 or numero == 2:
    print(f"{numero} é primo e foram executadas 0 divisões para descobrir isso")
elif numero % 2 == 0:
    print(f"{numero} não é primo e foi executada uma divisão para descobrir isso")
else:
    contador = 1
    primo = True 
    for i in range(3, numero, 2):
        contador += 1 
        if numero % i == 0:
            primo = False 
            break 
    if primo:
        print(
            f"{numero} é primo e foram executadas"
            f"{contador} divisões para descobrir isso"
        )
    else:
        print(
            f"{numero} não é primo e foram executadas"
            f"{contador} divisões para descobrir isso"
        )

# 24. Faça um programa que calcule e mostre a média aritmética de N notas.

print("Calcular médias")
quantidadenotas = int(input("Digite a quantidade de notas--> "))
contadormedia = 0 
for x in range(1, quantidadenotas + 1):
    notas = int(input("Digite sua nota :\n "))
    contadormedia = contadormedia + notas
media = contadormedia / quantidadenotas 
print("Sua média é-->", media)

# 25. Faça um programa que peça para n pessoas a sua idade, ao final o programa deverá verificar se a média de idade da turma
# varia entre 0 e 25.26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

print("Calcular idade média da turma")
quantidadenotas = int(input("Digite a quantidade de pessoas: "))
contadormedia = 0 
for x in range(1, quantidadenotas + 1):
    notas = int(input("Informe a idade :\n "))
    contadormedia = contadormedia + notas 
media = contadormedia / quantidadenotas 
print("A média de idade da turma é --> ", media)
if media < 26:
    print("A turma é jovem")
elif media > 26 and media < 60:
    print("A turma é adulta")
else:
    print("A turma é idosa")


# 26. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor
# votar e ao final mostrar o número de votos de cada candidato. 

print("Calcular votos de cada candidato")
quantidade_eleitores = int(input("Digite a quantidade de eleitores: "))
contador = 0 
for x in range(1, quantidade_eleitores + 1):
    candidato = str(input("Informe o candidato que irá votar (1, 2 ou 3): "))
if candidato == "1":
    contador1 = contador1 + 1 
elif candidato == "2":
    contador2 = contador2 + 1 
else:
    contador3 = contador3 + 1 
print(contador1)
print(contador2)
print(contador3)

# 27. Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade
# de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

turma = int(input("Informe a quantidade de turma: "))
alunos1 = 0 
for c in range(1, turma + 1):
    alunos = int(input("Informe a quantidade de alunos em cada turma: "))
    while alunos > 40:
        alunos = int(input("Valor incorreto, informe novamente a quantidade de alunos em casa turma--> "))
    alunos1 = alunos1 + alunos 
media_alunos = alunos1/turma
print(media_alunos)

# 28. Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CD's e 
# o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CD's e o valor para cada um.

quantidade_cd = int(input("Informe a quantidade de CDs adquiridos: \n"))
somador = 0 
for c in range(1, quantidade_cd + 1):
    preco = float(input("Informe o preço de cada CD: "))
    somador = somador + preco 
    media = somador / quantidade_cd
print("Total investido: ", somador, "$")
print("Valor gasto em cada CD =", media, "$")

# 29. O Sr. Manoel Joaquim possui uma grande loja de artigos nde R$1.99, com cerca nde 10 caixas. Para agilizar o cálculo
# de quanto cada cliente deve pagar ele desenvolveu uma tabela que contém o número de itens que o cliente comprou
# e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está
# levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa que conterá os preços de 1
# até 50 produtos, conforme o exemplo: 
# Loja Quase dois - Tabela de preços
# 1 - R$1.99
# 2 - R$3.98 
# ... 
# 50 - R$99.50

for c in range(1, 51):
    somador = 1.99*c
    print(c, "-", somador, "$")

# 30. O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já
# é um sucesso na sua loja de 1.99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães,
# de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
# Preço do pão: R$ 0.18 
# Panificadora Pão de Ontem - Tabela de preços 
# 1 - R$0.18
# 2 - R$0.36
# ... 
# 50 - R$9.00

precopao = float(input("Informe o preço do pão: "))
print("Panificadora Pão de Ontem - Tabela de preços")
for c in range(1, 50 + 1):
    somador = precopao * c 
    print(c, "-", somador, "$")


# 31 - O Sr. Manoel expandiu seus negócios para além dos negócios de 1.99 e agora possui uma loja de conveniências. 
# Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido 
# de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o 
# final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu,
# para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para 
# registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
# Lojas Tabajara
# Produto 1: R$2.20
# Produto 2: R$ 5.80
# Produto 3: R$0.
# Total: R$ 9.00
# Dinheiro: R$ 20.00
# Troco: R$ 11.00
# ... 

quantidade = int(input("Quantidade de produtos comprados: "))
soma = 0 
for produtos in range(1, quantidade + 1):
    preco = float(input("Informe o preço dos produtos: "))
    soma = soma + preço 

print("Total = R$", soma)
dinheiro = float(input("Dinheiro total: "))
troco = dinheiro - soma 
print("Troco: R$", troco)


# 32. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
# Ex.: 5! = 5.4.3.2.1 - 120 

import math 
numero = int(input("\nDigite o número que quer realizar o fatorial: "))
count = numero 
fatorial = math.factorial(numero)

for i in range(numero - 1):
    print(count, end=" * ")
    count -= 1 
print("1 =", fatorial)

# 33. O Departamento Estadual de Metereologia lhe contratou para desenvolver um programa que leia um conjunto indeterminado
# de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas. 

n_temperaturas = int(input("Quantidade de temperaturas que irá digitar: "))
temperaturas = [] 
n_temperatura = 1 
for i in range(n_temperaturas):
    print("Temperatura n° ", n_temperatura)
    temperatura = temperaturas.append(float(input("Digite a temperatura: ")))
    n_temperatura += 1 

print("Maior temperatura = ", max(temperaturas))
print("Menor temperatura = ", min(temperaturas))
print("Média = ", round(sum(temperatura) / len(temperaturas), 2))



# 34. Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. 
# Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número
# inteiro e determine se ele é ou não um número primo. 

numero = int(input("\nDigite um número: "))

if numero % 2 == 0 and numero != 2:
    print("não é primo")
else:
    print("primo")



# 35. Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes
# entre 1 e um número inteiro informado pelo usuário. 

numero = int(input("\nDigite um número: "))
lista = []

for i in range(numero + 1):
    if i % 2 == 1 and i != 2:
        lista.append(i)

print("Números primos: ", lista)


# 36. Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário,
# mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados
# também pelo usuário, conforme exemplo:
# Montar a tabuada de: 5
# Começar por: 4
# Terminar em: 7 

# Vou montar a tabuada de 5 começando em 4 e terminando em 7:

# 5 x 4 = 20 
# 5 x 5 = 25 
# 5 x 6 = 30 
# 5 x 7 = 35...
# Obs.: Você deve verificar se o usuário não digitou o final menor que o inicial. 

comeco = 4 
final = 7 
tabuada = 5 

while (comeco >= final):
    tabuada = int(input("Digite a tabuada que deseja (1 a 10): "))
    comeco = int(input("Digite por qual número deseja começar: "))
    final = int(input("Digite por qual número deseja finalizar: "))
    if (começco >= final):
        print("")
        print("O valor inicial não pode ser maior que o final!\n")
        print("")

print("")
print("Tabuada de: ", tabuada)
print("Inicializada por: ", comeco)
print("Finalizada por: ", final)

while (comeco < (final + 1)):
    print(tabuada, "X", comeco, "=", tabuada * comeco)
    comeco = comeco + 1


# 37. Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, o mais gordo
# e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código,
# sua altura e seu peso. O final da digitação de dados deve ser dado quando o usuário digitar zero no campo código.
# Ao encerrar o programa, também devem ser informados os códigos e valores do cliente mais alto, do mais baixo,
# do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes.

cod_clientes = []
altura_clientes = []
peso_clientes = []
n_cliente = 1 
codigo = True 

while codigo != 0:
    print("\nCliente n° ", n_cliente)
    codigo = int(input("Digite o código: "))
    if codigo == 0:
        break 
    else:
        altura = float(input("Digite a altura: "))
        peso = float(input("Digite o peso: "))
        cod_clientes.append(codigo)
        altura_clientes.append(altura)
        peso_clientes.append(peso)
        n_cliente += 1 

cod_magro = peso_clientes.index(min(peso_clientes))
cod_gordo = peso_clientes.index(max(peso_clientes))
cod_alto = altura_clientes.index(max(altura_clientes))
cod_baixo = altura_clientes.index(min(altura_clientes))
print("\n" * 5)
print("Código do mais magro: ", cod_clientes[cod_magro])
print("Código do mais gordo: ", cod_clientes[cod_gordo])
print("Código do mais alto: ", cod_clientes[cod_alto])
print("Código do mais baixo: ", cod_clientes[cod_baixo])
print("Média de altura: ", sum(altura_clientes) / len(altura_clientes))
print("Média de peso: ", sum(peso_clientes) / len(peso_clientes))


# 38. Um funcionário de uma empresa recebe aumento salarial anualmente. Sabe-se que:
#   a. Esse funcionário foi contratado em 1995, com salário incial de R$ 1.000.00;
#   b. Em 1996 recebeu aumento de 1.5% sobre seu salário inicial;
#   c. A partir de 1997(inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
#   Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo
#   que o usuário digite o salário inicial do funcionário.

salario = float(input("Digite o salário inicial do funcionário: "))
aumento = 1.5 

for i in range(1996, 2018 + 1):
    aumento = aumento * 2 
    salario_atual = salario + (salario * (aumento / 100))
    print("Salário em ", i, " = ", salario_atual)

# 39. Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
# representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais
# alto e o número do aluno mais baixo, junto com suas alturas.

numero_alunos = []
altura_alunos = []

for i in range(10):
    print("\nDigitação número ", i + 1, " :")
    n_aluno = int(input("Digite o número do aluno: "))
    while n_aluno in numero_alunos:
        print("[Este número já foi digitado]")
        n_aluno = int(input("Digite outro número: "))
    a_aluno = altura_alunos.append(float(input("Digite a altura do aluno: ")))
    numero_alunos.append(n_aluno)

indice_baixo = altura_alunos.index(min(altura_alunos))
indice_alto = altura_alunos.index(max(altura_alunos))

print("Aluno mais baixo \nNúmero: ", numero_alunos[indice_baixo], "\nAltura: ", min(altura_alunos))
print("Aluno mais alto \nNúmero: ", numero_alunos[indice_alto], "\nAltura: ", max(altura_alunos))

# 40. Foi feita uma estatatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. 
# Foram obtidos os seguintes dados:
# a. Código da cidade;
# b. Número de veículos de passeio ( em 1999 );
# c. Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
# d. Qual o maior e menor índice de acidentes de trânsito e a que cidade pertence;
# e. Qual a média de veículos nas cinco cidades juntas;
# f. Qual a média de acidentes de trânsito nas cidades com menos de 2000 veículos de passeio.

cod_cidades = []
n_veiculos = []
n_acidentes = []
acidentes_2000 = [] 

for i in range(5):
    print("\nCidade número ", i + 1)
    codigo_cidade = int(input("Digite o código da cidade: "))
    while codigo_cidade in cod_cidades:
        print("[Código já digitado]")
        codigo_cidade = int(input("Digite outro código: "))

    numero_acidentes = int(input("Digite o número de acidentes: "))
    numero_veiculos = int(input("Digite o número de veículos: "))

    if numero_veiculos > 2000:
        acidentes_2000.append(numero_acidentes)
        n_acidentes.append(numero_acidentes)
    else:
        n_acidentes.append(numero_acidentes)

    n_veiculos.append(numero_veiculos)
    cod_cidades.append(codigo_cidade)

indice_acidentes_menor = n_acidentes.index(min(n_acidentes))
indice_acidentes_maior = n_acidentes.index(max(n_acidentes))

print("\nMenos acidentes\nQuantidade de acidentes: ", min(n_acidentes), "\nCódigo da cidade: ", cod_cidades[indice_acidentes_menor])
print("\nMais acidentes\nQuantidade de acidentes: ", max(n_acidentes), "\nCódigo da cidade: ", cod_cidades[indice_acidentes_maior])

media_veiculos = sum(n_veiculos) / len(n_veiculos)
print("\nMédia de veículos nas 5 cidades: ", media_veiculos)

media_acidentes_2000 = sum(acidentes_2000) / len(acidentes_2000)
print("\nMédia de acidentes nas cidades com menos de 2000 veículos: ", media_acidentes_2000)

# 41. Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados:
# valor da dívida, valor dos juros, quantidade de parcelas, valor da parcela.
# Os juros e a quantidade de parcelas seguem abaiaxo:
# Quantidade de Parcelas % de Juros sobre o valor inicial da dívida:
# 1         0
# 3         10 
# 6         15
# 9         20
# 12        25 

# Exemplo da saída do programa:

# Valor da Dívida   Valor dos Juros     Quantidade de Parcelas      Valor da parcela 

# R$1.000.00        0                   1                           R$1.000.00
# R$ 1.100.00       100                 3                           R$ 366.00
# R$ 1.150.00       150                 6                           R$ 191.67

print("\n" * 5)
divida = float(input("Digite o valor da dívida: "))
parcela = 1 
print("\n" * 5)
print("Valor da dívida: ", end=" ")
print("Valor dos juros: ", end=" ")
print("Quantidade de parcelas: ", end=" ")
print("Valor da parcela: ")

for i in range(5):
    if parcela == 1:
        juros = 1 
        valor_juros = 0 
    elif parcela == 4:
        parcela = 3 
        juros = 1.10
    elif parcela == 7 or parcela == 6:
        parcela = 6
        juros = 1.15
    elif parcela == 10 or parcela == 9:
        parcela = 9
        juros = 1.20 
    elif parcela == 13 or parcela == 12:
        parcela = 12 
        juros = 1.25

valor_juros = divida * juros 
divida_com_juros = divida * juros 
valor_parcela = divida_com_juros  / parcela 

print("R$", round(divida_com_juros, 2), end="                 ")
print(round(valor_juros, 2),  end="                 ")
print(parcela, end="                       ")
print("R$", round(valor_parcela, 2))
parcela += 3

# 42. Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão
# nos seguintes intervalos: [0-25], [26-50], [51-75], [76-100]. A entrada de dados deverá terminar quando foi
# lido um número negativo. 

n25 = []
n50 = []
n75 = []
n100 = []
numero = True 
while numero > 0:
    numero = float(input("Digite um número: "))
    if numero >L 0 and numero <= 25:
        n25.append(numero)
    elif numero > 25 and numero <= 50:
        n50.append(numero)
    elif numero > 50 and numero <= 75:
        n75.append(numero)
    elif numero > 75 and numero <= 100:
        n100.append(numero)

print("\n[0, 25]: ", len(n25))
print("[26, 50]: ", len(n50))
print("[51, 75]: ", len(n75))
print("[76, 100]: ", len(n100))

# 43. O cardápio de uma lanchonete é o seguinte:
#   Especificação       Código      Preço
#   Cachorro Quente     100         R$1.20
#   Bauru Simples       101         R$1.30
#   Bauru com ovo       102         R$1.50
#   Hambúrguer          103         R$1.20
#   Cheeseburguer       104         R$1.30
#   Refrigerante        105         R$1.00

# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor
# a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar
# quando o pedido deve ser encerrado. 

codigos = [100, 101, 102, 103, 104, 105]
comidas = ['Cachorro-quente', 'Bauru Simples', 'Bauru com ovo', 'Hamburguer', 'CheeseBurguer', 'Refrigerante']
precos = [1.20, 1.30, 1.50, 1.20, 1.30, 1.0]
codigo = True 
n_pedido = 1 
pedido = []

while codigo != 0:
    print("\nPedido n°", n_pedido)
    codigo = int(input("Digite o código do alimento: "))
    if codigo == 0:
        break 
    else:
        while codigo not in codigos:
            print("[Este código não corresponde a nenhum alimento.]")
            codigo = int(input("Digite o código do alimento: "))
        
        indice = codigos.index(codigo)
        quantidade = int(input("Digite a quantidade: "))
        valor_pedido = precos[indice] * quantidade 
        pedido.append(valor_pedido)
    n_pedido += 1 

pedido_nota = 0 
print("\n" * 2)
for i in range(n_pedido - 1):
    print("Pedido n°", pedido_nota + 1, "= R$". round(pedido[pedido_nota], 2))
    pedido_nota += 1 
print("Total: R$", round(sum(pedido), 2))

# 44. Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados
# são:
# 1, 2, 3, 4 - Votos para os respectivos candidatos
# ( 1 - José; 2 - João; etc.)
# 5 - Voto Nulo
# 6 - Voto em Branco. 
# Faça um programa que calcule e mostre:
# O total de votos para cada candidato. 
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero. 

possiveis_votos = [1, 2, 3, 4, 5, 6]
candidatos = ['Ciro Gomes', 'Bolsonaro', 'João Amoedo', 'Lula Molusco', 'Nulo', 'Branco']
votos = [] 

voto = True 
n_votos = 1 
while voto != 0:
    print("Voto n°", n_votos)
    if voto == 0:
        break
    else:
        while voto not in possiveis_votos:
            print("Voto inválido")
            voto = int(input("Digite o seu voto: "))
        votos.append(voto)
    n_votos += 1 

contador = 0 
print("\n" * 2)
for i in range(len(candidatos)):
    print("Votos para ", candidatos[contador], end=" : ")
    if votos.count == 0:
        print("0")
        contador += 1 
    else:
        print(votos.count(contador + 1))
        contador += 1 

porcentagem_nulo = (votos.count(5) / len(votos)) * 100 
porcentagem_branco = (votos.count(6) / len(votos)) * 100 
print("\nPorcentagem Nulos: ", round(porcentagem_nulo, 2), "%Porcentagem Brancos: ", round(porcentagem_branco, 2), "%")


# 45. Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões. O programa deve perguntar ao aluno
# a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota 
# (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai
# utilizar o sistema. Após todos os alunos terem respondido, informar:
#   a. Maior e Menor acerto;
#   b. Total de Alunos que utilizaram o sistema;
#   c. A Média das Notas da Turma.
# Gabarito da Prova:
# 01 - A 
# 02 - B 
# 03 - C 
# 04 - D 
# 05 - E 
# 06 - E 
# 07 - D 
# 08 - C 
# 09 - B 
# 10 - A 
# Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos
# usarem o programa. 

gabarito = [] 
respostas_aluno = [] 
notas_tiradas = [] 
print = ("\nProfessor: ")
for i in ragne(10):
    print("Questão: ", i + 1)
    resposta_certa = gabarito.append(input("Digite a alternativa certa: "))
n_aluno = 1 
continuar = True 
while continuar != 'n':
    print("\n" * 5)
    print("Aluno n°", n_aluno, ":")
    respostas_aluno.clear()
    for i in range(10):
        print("Questão: ", i + 1)
        resposta_aluno = respostas_aluno.append(iput("Escolha a alternativa: "))
    nota = 0 
    for i in range(10):
        if respostas_aluno[i] == gabarito[i]:
            nota += 1 
    notas_tiradas.append(nota)
    continuar = input("Outro aluno vai utilziar o sistema? [s/n]: ")
    n_aluno += 1 
print(len(notas_tiradas), "alunos utilizaram o sistema")
print("\nA maior nota tirada foi: ", max(notas_tiradas))
print("A menor nota tirada foi: ", min(notas_tiradas))
print("A média de notas da turma foi de: ", sum(notas_tiradas / len(notas_tiradas))
print(notas_tiradas)

# 46. Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta,
# o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um 
# programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos
# conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para
# armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. O programa deve ser encerrado
# quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

# Atleta: Rodrigo Curvello

# Primeiro salto: 6.5m
# Segundo salto: 6.1m
# Terceiro salto: 6.2m
# Quarto salto: 5.4m
# Quinto salto: 5.3m

#Melhor salto: 6.5m
#Pior salto: 5.3m
#Média dos demais saltos: 5.9m

# Resultado final:
# Rodrigo Curvello: 5.9m 

nome_atleta = True 
n_atleta = 1 
while nome_atleta != '':
    saltos = [] 
    print("\n"*5)
    print("Atleta n°", n_atleta)
    nome_atleta = input(("Digite o nome do atleta: "))
    if nome_atleta == '':
        break 
    else:
        n_salto = 1 
        print("\n" * 3)
        for i in range(5):
            print("Salto n° ", n_salto)
            distancia_salto = float(input("Digite a distância do salto: "))
            saltos.append(distancia_salto)
            n_salto += 1 
        print("Atleta: ", nome_atleta)
        n_salto = 1 
        count = 0 
        for i in range(5):
            print(n_salto, "° salto : ", saltos[count], " m")
            n_salto += 1 
            count += 1 
        print("Melhor salto: ", max(saltos), " m")
        print("Pior salto: ", min(saltos), " m")

        saltos.remove(max(saltos))
        saltos.remove(min(saltos))
        media = sum(saltos) / len(saltos)
        print("Média dos demais saltos: ", round(media, 2))
        print("Resultado Final: \n", nome_atleta, " :", round(media, 2))
        n_atleta += 1 


# 47. Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas.
# A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas
# dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima
# informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informadas
# ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:

# Atleta: Aparecido Parente
# Nota: 9.9
# Nota: 7.5
# Nota: 9.5
# Nota: 8.5
# Nota: 9.0
# Nota: 8.5
# Nota: 9.7 

# Resultado final:
# Atleta: Aparecido Parente
# Melhor nota: 9.9 
# Pior nota: 7.5
# Média: 9.04 

import time 
nome_atleta = True 
n_atleta = 1 
while nome_atleta != '':
    notas = []
    print("\n" * 5)
    print("Atleta n°", n_atleta)
    nome_atleta = input("Digite o nome do atleta: ")
    if nome_atleta == '':
        break 
    else:
        n_jurado = 1 
        print("\n" * 3)
        for i in range(7):
            print("Jurado n° ", n_jurado)
            nota = float(input("Digite a nota: "))
            notas.append(nota)
            n_jurado += 1 
        print("Atleta: ", nome_atleta)
        n_jurado = 1 
        count = 0 
        for i in range(7):
            print(n_jurado, "° Jurado : ", notas[count])
            n_jurado += 1 
            count += 1
        print("Resultado Final: ")
        print("Nome do atleta: ", nome_atleta)
        print("Melhor nota: ", max(notas))
        print("Pior nota: ", min(notas))
        notas.remove(max(notas))
        notas.remove(min(notas))
        media = sum(notas) / len(notas)
        print("Média: ", round(media, 2))
        n_atleta += 1
        print("Reiniciando em 5 segundos")
        time.sleep(5)


# 48. Faça um programa que peça um número inteiro positivo e em seguida mostre este número invertido.
# Por exemplo:
# 123456789
# -> 987654321

numero = input("Digite um número: ")
print("Número invertido: ", numero[:: -1])


# 49. Faça um programa que mostre os n termos da Série a seguir:
# S = 1/1 + 2/3 + 3/5 + 4/7 + ... + n/m. 
# Imprima no final a soma da série.

n1 = 1
n2 = 1 
n1_lista = []
n2_lista = [] 
print("S = ", end = "")
while n1 <= 10 -1:
    print(n1, "/", n2, " + ", end="")
    n1_lista.append(n1)
    n2_lista.append(n2)
    n1 += 1
    n2 += 2 

print(n1, "/", n2, " = ", sum(n1_lista), "/", sum(n2_lista))


# 50. Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

h = 1
n = 2 
h_lista = []
n_lista = []
print("H = 1 +", end = "")
while n <= 10 -1:
    print(" ", h, "/", n, " + ", end="")
    h_lista.append(h)
    n_lista.append(n)
    n += 1

print(h, "/", n, " =>", sum(h_lista), "/", sum(n_lista), " =>", round(sum(h_lista) / sum(n_lista)), 2)


# 51. Faça um programa que mostre os n termos da Série a seguir:
#   S = 1/1 + 2/3 + 3/5 + 4/7+ 5/9 + ... + n/m.

n1 = 1 
n2 = 1 
n1_lista = []
n2_lista = [] 
print("S = ", end = "")
while n1 <= 10 -1:
    print(n1, "/", n2, " + ", end="")
    n1_lista.append(n1)
    n2_lista.append(n2)
    n1 += 1 
    n2 += 2

print(n1, "/", n2, " = ", sum(n1_lista), "/", sum(n2_lista))


# -------------------------------------------------------------------------------

# Exercícios com Listas 

# 1. Faça um programa que leia um vetor de 5 números inteiros e mostre-os. 

listaNumeros = [] 
print('Informe os 5 números: ')
for i in range(5):
    listaNumeros.append(input('Número ' + str(i+1) + ':\n'))
print(listaNumeros)

# 2. Faça um programa que leia um vetor de 10 números reais e mostre-os na ordem inversa. 

listaNumerosReais = []
print('Informe 10 números reais: ')
for i in range(10):
    listaNumerosReais.append(float(input('Número ' + str(i+1) + ':\n')))
listaNumerosReais.reverse()
print(listaNumerosReais)


# 3. Faça um programa que leia 4 notas, mostre as notas e a média na tela. 

listaNotas = []
media = 0 
print('Informe 4 notas: ')
for i in range(4):
    listaNotas.append(float('Nota ' + str(i+1) + ':\n')))
    media += listaNotas[i]
media = media/4
print(listaNotas)
print(media)

# 4. Faça um programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas.
# Imprima as consoantes.

listaChar = [] 
consoantes = 0 
print('Informe os caracteres: ')
for i in range(10):
    listaChar.append((input('Caracter ' + str(i+1) + ':\n')))
    char = listaChar[i]
    if(char not in ('a', 'e', 'i', 'o', 'u')):
        consoantes += 1 
print(consoantes)

# 5. Faça um programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares 
# no vetor PAR e o os números ÍMPARES no vetor ímpar. Imprima os três vetores. 

listaPar = []
listaImpar = [] 
listaNumeros = [] 
numero = 0 
print('Informe os números: ')
for i in range(20):
    listaNumeros.append(int(input('Número: ' + str(i+1) + ':\n')))
    numero = listaNumeros[i]
    print(numero)
    if numero % 2 == 0:
        listaPar.append(numero)
    else:
        listaImpar.append(numero)
print(listaNumeros)
print(listaPar)
print(listaImpar)


# 6. Faça um programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de 
# cada aluno, imprima o número de alunos com média maior ou igual a 7.0. 

listaNotas = []
notasAluno = []
print('Notas dos Alunos')
for i in range(10):
    media = 0 
    notasAluno = []
    print('Aluno: ' + str(i+1))
    for j in range(4):
        notasAluno.append(float(input('Nota: ' + str(j+1) + '\n')))
        media += 1 notasAluno[j]
        print(media)
    media = media/4
    listaNotas.append(media)

print(listaNotas)

# 7. Faça um programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números. 

lista1 = []
lista2 = []
listaInter = []

for i in range(10):
    print('lista 1: ')
    lista1.append(input('Elemento: ' + str(i+1) + '\n'))

for j in range(10):
    print('lista 2: ')
    lista2.append(input('Elemento: ' + str(i+j) + '\n'))

for m in range(10):
    listaInter.append(lista1[m])
    listaInter.append(lista2[m])

print(lista1)
print(lista2)
print(listaInter)


# 8. Faça um programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
# Imprima a idade e a altura na ordem inversa à ordem lida.

temperatura = []
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
media = 0 
acimaMedia = {}
for i in range(len(meses)):
    if temperatura[i] > media:
        acimaMedia.update({meses[i]: temperatura[i]})

print('Média das temperaturas: Anual -> ' + str(media))
print('Meses com temperaturas acima da média: ' + str(acimaMedia))

# 9. Faça um programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados
# dos elementos do vetor.

soma_dos_quadrados = 0 
for i in range(10):
    soma_dos_quadrados += int(input(f"Digite o {i+1}° número inteiro: ")) ** 2
print(f"A soma dos quadrados dos números digitados é {soma_dos_quadrados}")

# 10. Faça um programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
# cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

elementos = 10 
vetor1 = []
vetor2 = []
vetor3 = []
for i in range(elementos):
    vetor1.append(int(input(f"Entre com {i+1}° número inteiro para o vetor 1: ")))
for i in range(elementos):
    vetor2.append(int(input(f"Entre com o {i+1}° número inteiro para o vetor 2: ")))
for i in range(elementos):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])
print("O vetor com os elementos intercalados dos vetores 1 e 2 é: ")
for i in range(elementos * 2)
print(vetor3[i], end='')


# 11. Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
B = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
C = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
intercalada = []
contador = 0 
for i in range(10):
    intercalada.append(A[contador])
    intercalada.append(B[contador])
    intercalada.append(C[contador])
    contador += 1 
print(intercalada)


# 12. Foram anotadas as idades e alturas de 30 alunos. Faça um programa que determine quantos alunos
# com mais de 13 anos possuem altura inferior à média de altura desses alunos.

import random
idades = []
alturas = []
aluno_13 = []
media_13 = []

for i in range(30):
    numero_aleatorio = idades.append(random.randrange(1, 20))
    numero_aleatorio2 = alturas.append(random.randrange(50, 200))

for i in range(30):
    if idades[i] > 13:
        aluno_13.append(alturas[i])
    
media = sum(aluno_13) / len(aluno_13)

for i in range(len(aluno_13)):
    if aluno_13[i] < media:
        media_13.append(aluno_13[i])
    
print('\nAs idades dos alunos são:\n', idades, '\nA altura dos alunos em cm são:\n', alturas)
print('\nForam ', len(aluno_13), ' alunos com idade acima de 13 anos que são:\n', aluno_13)
print('\nA média de altura desses ', len(aluno_13), ' alunos é:', media, 'cm')
print('\nForam ', len(media_13), ' alunos com mais de 13 anos que possuem altura inferior à media de altura:\n', media_13)

# 13. Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto,
# calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas 
# ocorreram (mostrar o mês por extenso: 1 - Janeiro, 2 - Fevereiro, ...)

temperatura_meses = []
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

for i in range(12):
    print('\nMês de ', meses[i], ' :')
    media = temperatura_meses.append(float(input('Digite a temperatura média: ')))

media_anual = sum(temperatura_meses / 12)
print('\n /' * 3)
for i in range(12):
    if temperatura_meses[i] > media_anual:
        print('Temperatura acima da média do mês: ', meses[i])

# 14. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#
#    "Telefonou para a vítima?"
#    "Esteve no local do crime?"
#    "Mora perto da vítima?"
#    "Devia para a vítima?"
#    "Já trabalhou com a vítima?"
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
#Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
#entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente"

sim = 0 
perguntas = ['Telefonou para a vítima? [s/n]',
             'Esteve no local do crime? [s/n]',
             'Mora perto da vítima? [s/n]',
             'Devia para a vítima? [s/n]',
             'Já trabalhou com a vítima? [s/n]'
             ]
for i in range(len(perguntas)):
    resposta = input(perguntas[i])
    if resposta == 's':
        sim += 1 
if sim == 2:
    print('\nSuspeita')
elif sim > 2 and and sim <= 4:
    print('\nCúmplice')
elif sim == 5:
    print('\nAssassino')
else:
    print('\nInocente')

# 15. Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada
# de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
#   a. Mostre a quantidade de valores que foram lidos;
#   b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#   c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#   d. Calcule e mostre a soma dos valores;
#   e. Calcule e mostre a média dos valores;
#   f. Calcule e mostre a quantidade de valores acima da média calculada;
#   g. Calcule e mostre a quantidade de valores abaixo de sete;
#   h. Encerre o programa com uma mensagem; 

valores = []
media_alta = []
valores_7 = []
cont -= 1 
rep = True 

while rep != 0:
    print('\nValor n° ', cont)
    val = int(input('\nDigite o valor: '))
    if val == -1:
        break 
    else:
        valores.append(val)
    cont += 1 

print('\n' * 2)
print('Quantidade de valores: \n', len(valores))
print('Os valores: \n', valores)
valores.reverse()
print('Osvalores na ordem inversa \n', valores)
print('A soma dos valores: \n', sum(valores))

media = sum(valores) / len(valores)
valores.reverse()

for i in range(len(valores)):
    if valores[i] > media:
        media_alta.append(valores[i])
    if valores[i] < 7:
        valores_7.append(valores[i])

print('A média dos valores: \n', media)
print('A quantidade de valores acima da média calculada: \n', media_alta)
print('A quantidade de valores abaixo de sete: \n', valores_7)
print('\nPrograma concluído!')



# 16. Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões.
# O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que 
# teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470.
# Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos
# de valores:
#   a. $200 - $299
#   b. $300 - $399
#   c. $400 - $499 
#   d. $500 - $599
#   e. $600 - $699
#   f. $700 - $799
#   g. $800 - $899
#   h. $900 - $999
#   i. $1000 em diante
# Desafio: Crie uma fórmula para chegar na posição da lista a partir do salário, sem fazer vários
# ifs aninhados. 

possiveis_salarios = [
    [200,299], [300,399],[400,499],
    [500,599],[600.699],[700,799],
    [800,899],[900,999]
]
quantidades = [0,0,0,0,0,0,0,0,0]

salarios = []
vendas_brutas = True 
while vendas_brutas != 0:
    vendas_brutas = float(input("\nDigite o valor das vendas: "))
    if vendas_brutas == 0:
        break 
    else:
        salario = (vendas_brutas * 0.09) + 200 
        if salario < 1000:
            for i in range(len(possiveis_salarios)):
                if salario > possiveis_salarios[i][0] and salario < possiveis_salarios[i][1]:
                    quantidades[i] += 1
        else:
            quantidades[8] += 1 
print("\n" * 3)
for i in range(len(possiveis_salarios)):
    print("Entre R$", possiveis_salarios[i][0], "e R$",possiveis_salarios[i][1], ":", quantidades[i])
print("Salários maiores que R$1000:", quantidades[8])

# 17. Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
#O resultado do atleta será determinado pela média dos cinco valores restantes.
#Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta
#em seus saltos e depois informe o nome, os saltos e a média dos saltos.
#O programa deve ser encerrado quando não for informado o nome do atleta.
#A saída do programa deve ser conforme o exemplo abaixo:

#Atleta: Rodrigo Curvêllo
 
#Primeiro Salto: 6.5 m
#Segundo Salto: 6.1 m
#Terceiro Salto: 6.2 m
#Quarto Salto: 5.4 m
#Quinto Salto: 5.3 m
#
#Resultado final:
#Atleta: Rodrigo Curvêllo
#Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
#Média dos saltos: 5.9 m

nome = True 
contador += 1 
saltos = [] 

while nome != 0:
    print('atleta', contador)
    nome = str(input('Digite o nome do atleta: '))
    if nome == '':
        break 
    else:
        for i in range(5):
            print(i + 1,'° Salto')
            distancia = float(input('Digite a distância em metros do salto: '))
            saltos.append(distancia)
    media = sum(saltos) / len(saltos)

    print('\nAtleta: ', nome, '\n')

    for i in range(5):
        print(i + 1, '°Salto: ', saltos[i], 'm')
    
    print('\nResultado final: ')
    print('Atleta: ', nome)
    print('Saltos: ', saltos)
    print('Média dos saltos: ', media, 'm')
    print('\n' * 3)
    contador += 1 


# 18. Uma grande emissora de televisão quer fazer uma enquete entre os seus telecpectadores para saber qual o 
# melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado
# pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando 
# a linguagem de programação C++. [???]
# Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador.
# Um número de jogador igual a zero, indica que a votação foi encerrada. Se um número inválido for digitado, o programa
# deve ignorá-lo, mosntrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa
# deverá exibir:
#           a. O total de votos computados;
#           b. Os números e respectivos votos de todos os jogadores que receberam votos; 
#           c. O percentual de votos de cada um destes jogadores; 
#           d. O número do jogador escolhido como o melhor jogador da partida, juntamente com o número
#           de votos e o percentual de votos dados a ele.
#  Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece 
# ordenado pelo número do jogador. O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual
# de cada jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos.
# A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. A disposição das informações
# deve ser a mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa. 
# Ao final, o programa que deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco,
# obedecendo a mesma disposição apresentada na tela. 

'''
Enquete: Quem foi o melhor jogador?

Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 11
Número do jogador (0=fim): 10
Número do jogador (0=fim): 50
Informe um valor entre 1 e 23 ou 0 para sair!
Número do jogador (0=fim): 9
Número do jogador (0=fim): 9
Número do jogador (0=fim): 0

Resultado da votação:

Foram computados 8 votos.

Jogador Votos           %
9               4               50,0%
10              3               37,5%
11              1               12,5%
O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.
'''

votos = [] 
votos_jogadores_votados = []
numeros_jogadores_votados = []
voto = True 
n_voto = 1 
while voto != 0:
    print('Voto n°', n_voto)
    voto = int(input('Digite o número do jogador: '))
    if voto == 0:
        break 
    else:
        while voto > 23 or voto < 1:
            print('[Voto inválido]')
            print('Voto n°', n_voto)
            voto = int(input('Digite novamente: '))
        votos.append(voto)
    n_voto += 1 
print('\nTotal de votos: ', len(votos))
contador = 1 
for i in range(23):
    if contador not in votos:
        contador += 1 
        continue 
    else:
        votos_jogadores_votados.append(votos.count(contador))
        numeros_jogadores_votados.append(contador)
        print('\nVotos para o jogador camisa n°', contador, ' = ', votos.count(contador))
        print('Percentual de votos: ', round(100 * votos.count(contador) / len(votos), 2), '%')
        contador += 1 
melhor = votos_jogadores_votados.index(max(votos_jogadores_votados))
print('\nO jogador mais votado foi o n°', numeros_jogadores_votados[melhor], 'com ', votos_jogadores_votados[melhor], 'votos')
print('Ganhou com', round(100 * votos_jogadores_votados[melhor] / len(votos), 2), '% dos votos')


# 19. Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a uma grande 
# quantidade de organizações:

'''
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
'''

# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado
# da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. 
# Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma 
# das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá
# calcular o percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado 
# pela empresa, e é o seguinte; 

'''
Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
'''

urna = []
sistemas = ['Windows Server', 'Linux', 'Netware', 'Mac OS', 'Outro']
indice_vitoria = []
indice_porcentagem_vitoria = []
eleitor = True 
num_voto = 1 

while eleitor != 0:
    print(f'\nEleitor n° {num_voto}\n')
    voto = int(input('Digite o seu voto [1 a 6] ou Digite [0] para sair: '))
    if voto == 0:
        break 
    else:
        while voto < 0 or voto > 6:
            print('Número Inválido')
            voto = int(input('Digite o seu voto [1 a 6] ou Digite [0] para sair: '))
        print('Voto Confirmado\n')
        urna.append(voto)
    num_voto += 1 

print('\n' * 2)
print('{:<19}{:>10}{:>4}'.format('Sistema Operacional', 'Votos', '%'))
print('{:<19}{:>10}{:>6}'.format('-'*19,'-'*5,'-'*3))

contador = 0 
for i in range(len(sistemas)):
    porcentagem_voto = round((urna.count(contador+1) / len(urna) * 100)
    print('{:<19}{:>10}{:>5}%'.format(sistemas[contador],urna.count(contador+1),porcentagem_voto))
    contador += 1 
    indice_vitoria.append(urna.count(contador+1))
    indice_porcentagem_vitoria.append(porcentagem_voto)

print('{:<19}{:>10}'.format('-'*19,'-'*5,))
print('{:<19}{:>10}'.format('Total',len(urna)))

vitoria = max(indice_vitoria)
for i in range(len(sistemas)):
    if indice_vitoria[i] == vitoria:
        print('\nO sistema mais votado foi o ', sistema[i], end=' ')

print('com ', max(indice_vitoria), ' votos, correspondendo a ', max(indice_porcentagem_vitoria), '% dos votos.')

# 20. As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado
# alcançado durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma projeção
# de quanto será gasto com o pagamento deste abono. 
#   Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral,
#   chegou-se à seguinte forma de cálculo:
#   a. Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro;
#   b. O piso do abono será de 100 reaus, isto é, aqueles funcionários cujo salário for muito baixo,
#   recebem este valor mínimo; Neste momento, não se deve ter nenhuma preocupação com colaboradores com 
#   tempo menor de casa, descontos, impostos ou outras particularidades. Seu programa deverá permitir
#   a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero)
#   encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a 
#   cada colaborador, de acordo com a regra definida acima. Ai final, o programa deverá apresentar:
#   - O salário de cada funcionário; juntamente com o valor do abono;
#   - O número total de funcionários processados;
#   - O valor total a ser gasto com o pagamento do abono;
#   - O número de funcionários que receberá o valor mínimo de 100 reais;
#   - O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para
#   fins ilustrativos. Os valores podem mudar a cada execução do programa.

'''
Projeção de Gastos com Abono
============================ 
 
Salário: 1000
Salário: 300
Salário: 500
Salário: 100
Salário: 4500
Salário: 0
 
Salário    - Abono     
R$ 1000.00 - R$  200.00
R$  300.00 - R$  100.00
R$  500.00 - R$  100.00
R$  100.00 - R$  100.00
R$ 4500.00 - R$  900.00
 
Foram processados 5 colaboradores
Total gasto com abonos: R$ 1400.00
Valor mínimo pago a 3 colaboradores
Maior valor de abono pago: R$ 900.00
'''

print('Digite 0 para encerrar o programa')
salarios = [] 
while True:
    salario = float(input('Salário: '))
    if salario == 0:
        break 
    salarios.append(salario)

print('projeção de Gastos coom Abono')
print('=============================')

print('Salário - Abono')
abonos, minimo = 0, 0 
maior = 0 
for s in salarios:
    abono = (salario * 20) / 100 
    if abono < 100:
        abono = 100 
        minimo += 1 
    if abono > maior:
        maior = abono 
    abonos += abono 
    print('R$ %.2f - R$%.2f' % (s, abono))

print('Foram processador %d colaboradores' % (sum(salarios)))
print('Total gasto com abonos: R$ %.2f % abonos')
print('Valor mínimo pago a %d colaboradores' % minimo)
print('Maior valor de abono pago: R$ %.2f' % maior)





# 21. Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA
# etc.). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro
# de combustível. Calcule e mostre:
#   a. O modelo do carro mais econômico.
#   b. Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 
#   1000 quilômetros e quanto isto custará, considerando que a gasolina custe R$2.25 o litro. Abaixo segue
#   uma tela de exemplo. A disposição das informações deve ser a mais próxima possível ao exemplo. Os dados
#   são fictícios e podem mudar a cada execução do programa. 

'''
Comparativo de Consumo de Combustível

Veículo 1
Nome: fusca
Km por litro: 7
Veículo 2
Nome: gol
Km por litro: 10
Veículo 3
Nome: uno
Km por litro: 12.5
Veículo 4
Nome: Vectra
Km por litro: 9
Veículo 5
Nome: Peugeout
Km por litro: 14.5

Relatório Final
 1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
 2 - gol             -   10.0 -  100.0 litros - R$ 225.00
 3 - uno             -   12.5 -   80.0 litros - R$ 180.00
 4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
 5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
O menor consumo é do peugeout.
'''
modelos = [] 
consumos = [] 

for i in range(1, 6):
    print('Veículo %d' % i)
    modelos.append(input('Nome: '))
    consumos.append(float(input('Km por litro: ')))

print('Relatório Final')
cont, custo = 0, 0 
gasto = 0 
menorModelo = ''
menor = 0 
for m in modelos:
    custo = 1000 / consumos[cont]
    print('%s   - %.1f litros   - R$%.2f' % (m, consumo[cont], consumo, gasto))
    if cont == 0:
        menor = custo 
        menorModelo = m 
    if menor < custo:
        menor = custo 
        menorModelo = m 
    cont += 1 
print('O menor consumo é do %s.' % (menorModelo))






# 22. Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção
# de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de
# 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar
# deles. 
# Foi requisitado que você desenvolva um programa para registrar esse levantamento. O programa deverá receber um número
# indeterminado de entradas, cada uma contendo: um número de identificação do mouse e o tipo de defeito; 
# necessita da esfera;
# necessita de limpeza; troca do cabo ou conector; quebrado ou inutilizado.
# Uma identificação igual a zero encerra o programa. Ao final o proigrama deverá emitir o seguinte relatório:

'''
Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%
'''

problemas = [0] * 4 
print('''1- necessita da esfera
2- necessita de limpeza
3- necessita troca do cabo ou conector
4- quebrado ou inutilizado ''')
while True: 
    identificacao = int(input('Identificação: '))
    if identificacao == 0: 
        break 
    problema = int(input('Digite o número do problema: '))
    problemas[problema - 1] = problemas[problema - 1] + 1 

print('Situação             Quantidade              Percentual')
total = sum(problemas)
print('1- necessita da esfera       %d          %.2f' % (problemas[0], (100 * problemas[0]) / total))
print('2- necessita de limeza       %d          %.2f' % (problemas[1], (100 * problemas[1]) / total))
print('3- necessita troca do cabo ou conector   %d      %.2f' % (problemas[2], (100 * problemas[2]) / total))
print('4- quebrado ou inutilizado   %d          %.2f' % (problemas[3], (100 * problemas[3]) / total))

# 23. A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos.
# Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários,
# e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar
# o seguinte arquivo, chamdo "usuários.txt":

'''
alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125
'''

# Neste arquivo, o noome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar
# um programa que gere um relatório, chamado "relatório.txt", no seguinte formato: 

'''
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB
'''

# O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários.
# De forma a agilizar a execução do programa. A conversão do esáço ocupado em disco, de bytes para megabytes,
# deverá ser feita através de um função separada, que será chamada pelo programa principal. O cálculo 
# do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.

arquivo = open('usuarios.txt', 'r')

linhas = arquivo.readlines()

arquivo.close()

usuarios = []
espaõs = [] 
total = 0 
for l in linhas:
    linha = l.split()
    usuarios.append(linha[0])
    espacos.append(int(linha[1]))

arquivoRelatorio = open('relatorio.txt', 'w')
arquivoRelatorio.write('ACME Inc.        Uso do espaço em disco pelos usuários\n')
arquivoRelatorio.write(
    '-------------------------------------------------------------------------------'
)

for i in range(0, len(usuarios)):
    espacoMB = espacos[i] / (1024 * 1024.0)
    percentualUso = espacos[i] / total 
    arquivoRelatorio.write('\n%d - %s _ %.2f MB - %.2f%%' %
                        (i+1, usuarios[i], espacoMB, percentualUSO* 100.0))

arquivoRelatorio.write('\nEspaço total ocupado: %.2f MB' % (total / (1024.0 * 1024.0)))
arquivoRelatorio.write('\nEspaço médio ocupado: %.2f MB' % (total / len(usuarios) / (1024.0 * 1024.0)))

arquivoRelatorio.close()


# 24. Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor.
# Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores (1 - 6) e uma função
# para gerar números aleatórios, simulando os lançamentos dos dados. 

import random 

numeros = [0] * 6 
for i in range(1, 100):
    n = random.randint(1, 6)
    numeros[n- 1] = numeros[n - 1] + 1 

cont = 1 
for n in numeros:
    print('%d teve %d lançamentos' % (cont, n))
    cont += 1 

# ------------------ funções -------------------------------

# 1. Faça um programa para imprimir:

'''
 1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
'''
def lista(n):
    return list(str(n) * n)

n = int(input(('Digite o número: '))

for i in range(1, n + 1 ):
    print(' '.join(lista(i)))



#2. Faça um programa para imprimir:
# 1
#    1   2
#   1   2   3
#   .....
#  1   2   3   ...  n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até 
# a n-ésima linha. 


n = int(input('Digite o número: '))

def lista(n):
    for i in range(1, n + 1):
        l = [] 
        for j in range(i):
            l.append(str(j+1))
        print(' '.join(l))
lista(n)


# 3. Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma 
# desses três argumentos. 

def soma(num1, num2, num3):
    return num1 + num2 + num3 

# 4. Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere
# 'P', se seu argumento for positivo, e 'N' se seu argumento for zero ou negativo. 

def valor(n):
    print('-')
    return 'P' if n >= 0 else 'N'


# 5. Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto,
# que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto.
# A função "altera" o valor de custo para incluir o imposto sobre vendas. 

def somaIMposto(taxaImposto, valor):
    return valor + {{valor * taxaIMposto / 100}}


# 6. Faça um programa que converta da notação de 24 hotas para a notação de 12 horas. Por exemplo, o programa deve converter 
# 14:25 em 2:25P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão 
# e uma para a saída. Registre a informação A.M/P.M. como um valor 'A' para A.M. e 'P' para P.M. Assim, a função
# para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita
# que o usuário reíra esse cálculo para novos valores de entrada todas as vezes que desejar. 

def formar(h, m):
    horas = ''
    if h > 12: #pm
        horas = str(h - 12) + ':' + str(m) + ' P.M'
    else: #am
    horas = str(h) + ':' + str(m) + 'A.M'

    return horas 

while True:
    print('Digite -1 para sair')
    horas = int(input('Digite as horas: '))
    if horas < 0:
        break 
    minutos = int(input('Digite os minutos: '))

    print(formatar(horas, minutos))

# 7. Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação
# de uma conta. O programa deverá solicitar ao usuárioo valor da prestação e o numero de dias em atraso e 
# passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor
# ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa 
# deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero
# para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá
# a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma.
# Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de 
# juros por dia de atraso. 

def valorPagamento(valor, dias):
    juros = 0 
    if dias == 9:
        return valor 
    else:
        juros = 0.1 * dias 

        return valor + ((3 * valor)/100) + juros 

total = 0 
cont = 0 
while True:
    valor = float(input('Digite o valor da prestação: '))
    if valor == 0:
        break 
    dias = int(input('Digite o número de dias em atraso: '))
    total += valorPagamento(valor, dias)
    cont += 1 

print('Quantidade total: %d' % cont)
print('Valor total das prestações: %.2f' % total)

# 8. Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado. 


def digitos(n):
    return len(str(n))

# 9. Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo:
# 127 -> 721. 

def reverso(n):
    return str(n)[::-1]
print(reverso(127))




# 10. Jogo de Craps. Faça um programa que implemente um jogo de Craps. O jogador lança um par de dados, 
# obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou.
# Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira
# jogada, você fez um 4, 5, 6, 8, 9 ou 10, este é seu "Ponto". Seu objetivo agora é continuar jogando
# os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este
# Ponto novamente.

from random import randint 

def craps():
    dado = randint(2,13)
    if dado == 7 or dado == 11:
        print('Você é um natural e ganhou!')

    elif dado == 2 or dado == 3 or dado == 12:
        print('Craps você perdeu!')

    elif dado == 4 or dado == 5 or dado == 6 or dado == 8 or dado == 9 or dadp == 10:

        numero = 0 
        while dado != numero: 
            numero = raandint(2,13)
            if numero == 7:
                print('Você perdeu!')
                break 
        if numero != 7:
            print('Você ganhou!')

craps() 



# 11. Data com mês por extenso. Construa uma função que receba uma data no formato DD//MM/AAAA e devolva uma 
# string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja
# inválida. 

def data(data):
    dia = int(data[0:2])
    mes  int(data[3:5])
    ano = int(data[6::])

    if dia < 1 or dia > 31 or mes > 12 or mes < 1:
        print('Data inválida')
        return 0 

    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

    novaData = str(dia) + ' de ' + meses[mes - 1] +' de ' + str(ano)
    return novaData 
print(data('19/12/2000'))




# 12. Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com
# os caracteres embaralhados. Por exemplo: se a função receber a palavra python, pode retorn nphtyo, ophtyn
# ou qualquer outra combinação possível, de forma aleatória. Padronize nem sua função que todos os caracteres
# serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados. 

import random 

def embaralha(palavra):
    palavra = palavra.lower()

    embaralha = random.sample(palavra, len(palavra)) # string vira lista
    nova = ''.join(embaralha) # lista vira string 

    return nova 

print(embaralha('TESTE')) 

# 13. Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres '+' e '-' e '|'. 
# Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo
# igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para
# valores dentro da faixa de forma elegante.

def valor_por_omissao(valor):
    if valor == '':
        return int(1)
    else:
        return faixa_minima_maxima(int(valor))

def faixa_minima_maxima(valor):
    if valor<1:
        return 1 
    elif valor>20:
        return 20 
    else:
        return valor 

def cria_linha(linha):
    l = '+'
    for x in range(linha):
        l + = '-'
    l += '+'
    print(l)

def cria_coluna(linha, coluna):
    for y in range(coluna):
        c = '|'
        c += ' '*linha
        c += '|'
        print(c)

def desenha_moldura(linha, coluna):
    cria_linha(linha)
    cria_coluna(linha, coluna)
    cria_linha(linha)

linha = input('Diga quantos +-----+, entre 1 e 20: ')
coluna = input('Diga quantos |      |, entre 1 e 20: ')
desenha_moldura(valor_por_omissao(linha), valor_por_omissao(coluna))





# 14. Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição
# e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com 
# números de 1 a 9:
#   8 3 4    
#   1 5 9
#   6 7 2 
# Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima.
# Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado.
# Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3. 


import random 

#j(coluna)
matriz = [[1, 2, 4],
          [4, 5, 6],
          [7, 8, 9]]        #i(linha)
res = False 
def magicsquare():
    global res 
    if matriz[0][0] + matriz[1][0] + matriz[2][0] == matriz[0][1] + matriz[1][1] + matriz[2][1] == matriz [0][2] + matriz[1][2] + matriz[2][2] == matriz[0][0] + matriz[0][1] + matriz[0][2] == matriz[1][0] + matriz[1][1] + matriz[1][2] == matriz[2][0] + matriz[2][1] + matriz[2][2] == matriz[0][0] + matriz [1][1] + matriz[2][2] == matriz[0][2] + matirz[1][1] + matriz[2][0]:
        res = True 
    else:
        res = False 
    return res 

while res == False:
    seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(3):
        for j in range(3):
            z = random.choice(seq)
            matriz[i][j] = z 
            x = seq.index(z)
            seq = seq[:x] + seq[x+1:]
    magicsquare()
print(matriz)

# --------------- Exercícios com Strings ----------------------------

# 1. Tamanho de Strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
# Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo. 
'''
Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.
'''

print('Comapra duas strings')
palavra1 = input('String 1: ')
palavra2 = input('String 2: ')

print('Tanmanho de "%s": %d ' % (palavra1, len(palavra1)))
print('Tamanho de "%s": %d ' % (palavra2, len(palavra2))))

if len(palavra1) == len(palavra2):
    print('As duas strings são de tamanhos iguais')
else:
    print('As duas strings são de tamanhos diferentes')

if palavra1 == palavra2:
    print('As duas strings possuem conteúdo igual')
else:
    print('As duas strings possuem conteúdo diferente')


# 2. Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar seu nome e em seguida
# mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lemnre-se que ao 
# informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

nome  = input('Digite seu nome: ').upper()

print(nome[::-1])

# 3. Nome na vertical. Faça um programa que solicite o nome do usuário e imrpima-o na vertical.
'''
F
U
L
A
N
O
'''

nome = input('Digite seu nome: ')
for n in nome:
    print(n)

# 4. Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.
'''
F
FU
FUL
FULA
FULAN
FULANO
'''

nome = input('Digite seu nome: ')

for i in range(1, len(nome) + 1):
    for y in range(0, i):
        print(nome[y]. end="")
    print('')

# 5. Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.
'''
FULANO
FULAN
FULA
FUL
FU
F
'''

nome = input('Digite seu nome: ')

for i in range(len(nome), 0, -1):
    for y in range(0, 1):
        print(nome[y], end="")
    print('')

# 6. Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima
# a data com o nome do mês por extenso. 
# Data de Nascimento: 29/10/1973
# Você nasceu em 29 de Outubro de 1973. 

data = input('Data de nascimento: ')
nmeses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

dia = int(data[0:2])
mes = meses(int)data[3:5]) - 1
ano = int(data[6:])

print('Você nasceu em %d de %s de %d' % (dia, mes, ano))



# 7. Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco),
# conte:
# a. quantos espaços em branco existem na frase.
# b. quantas vezes aparecem as vogais a, e, i, o, u. 

frase = input('Digite a frase: ')
branco = 0 
vogais = 0 
for f in frase: 
    if f == '':
        branco += 1 
    if f in 'aeiou':
        vogais += 1 

print('Total de espaços em branco: %d' % branco)
print('Total de vogais: %d' % vogais)



# 8. Palíndromo. Um palíndromo é uma sequência de caracteres cuja leitura é idêntica se feita da direita para
# esquerda ou vice-versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação
# são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados.
# Faça um programa que leia uma sequência de caracteres, mostre-a e diga se é um palíndromo ou não. 

palavra = input('Digite a palavra: ')

novaPalavra = ''
for p in palavra:
    if p != ' ':
        novaPalavra += p 

if novaPalavra == novaPalavra[::-1]:
    print('É um palíndromo!')
else:
    print('Não é palíndromo!')

# 9. Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato
# xxx.xxx.xxxx-xx e indique se é um número válido ou inválido através da validação dos dígitos verificadores 
# dos caracteres de formatação. 

def validação(cpf):
    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')
    if (len(cpf) != 11):
        return False 

    # Realize a multiplicação dos 9 primeiros números
    fator = 10 
    soma = 0 
    for i in range(0, 9):
        soma += (int(cpf[i]) * fator)
        fator -= 1 

    # Divide o somatório por 11 e pega o resto 
    resto = soma % 11 

    # Se o resto é menor que 2, então o primeiro dígito verificador é 0,
    # senão diminui o resto do valor 11 
    if (resto < 2):
        digito1 = 0 
    else:
        digito1 = 11 - resto 

    # Agora verifica o segundo digito com os 10 primeiros numeros
    fator = 11 
    soma = 0 
    for i in range(0, 10):
        soma += (int(cpf[i]) * fator)
        fator -= 1 

    # Divide o somatório por 11 e pega o resto
    resto = soma % 11 

    # Se o resto é menor que 2, então o segundo dígito verificador é 0,
    # senão diminui o resto do valor 11 
    if (resto < 2):
        digito2 = 0 
    else:
        digito2 = 11 - resto 

    if (int(cpf[9]) == digito1) and (int(cpf[10])) == digito2):
        return True 
    return False 

cpf = input('Informe o CPF: ')
if(validadeCPF(cpf)):
    print('CPF válido')
else:
    print('CPF INVÁLIDO')


# 10. Número por extenso. Escreva um programa que solciite ao usuário a digitação de um número até 99 e imprima-o 
# por extenso. 


dezenas = ['', '', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
primeira_dezena = ['dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezeesseis', 'dezessete', 'dezoito', 'dezenove']
unidades = ['zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']

numero = int(input('Informe um número: '))
if (numero < 0) or (numero > 99):
    print('O número informado deve estar entre 0 e 99.')
else:
    dezena = numero / 10 
    unidade = numero % 10 

    if (numero >= 20):
        print('%s' % dezenas[int(dezena)], end="")
        if (unidade != 0):
            print(' e %s' % unidades [int(unidade)])
        print('')
    elif (numero >= 10):
        print('%s' % primeira_dezena[iint(unidade)])
    else:
        print('%s' % unidades[int(unidade)])




# 11. Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo de texto
# e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.
'''
Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!
'''

import random 

print('Jogo de Forca')

# Abre o arquivo para leitura 
arquivo = open('palavras-exerc11.txt', 'r')

# Coloca todas as linhas em memória 
palavras = arquivo.readlines()

# fecha o arquivo 
arquivo.close()

palavraEscolhida = palavras[random.randint(0, len(palavras) -1].upper().strip()
tamanhoPalava = len(palavraEscolhida)
palavraAdvinhada = ['_'] * tamanhoPalavra

numTentativas = 0 
erros = 0 

print(' '.join(palavraAdvinhada))
print(palavraEscolhida)
while True:
    p = input('Digite a letra: ')
    cont = 0 
    if p in palavraEscolhida: # letra encontrada
        for pa in palavraEscolhida:
            if pa == p:
                palavraAdivinhada[cont] = p 
            cont += 1 
        if '_' not in ' '.join(palavraAdivinhada):
            print('VocÊ ganhou!')
            break
    else:
        erros += 1 
        if erros >= 6:
            print('Você perdeu, a palavra é %s' % palavraEscolhida)
        else:
            print('Você errou pela %d° ve\. Tente novamente.' % erros)
    print(' '.join(palavraAdivinhada))


# 12. Valida e corrige número de telefone. Faça um programa que leia um número de telefone e corrija o número
# no caso deste conter apenas 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem
# o traço separador. 
'''
Valida e corrige número de telefone
Telefone: 461-0133
Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
Telefone corrigido sem formatação: 34610133
Telefone corrigido com formatação: 3461-0133
'''

print('Valida e corrige número de telefone')
numero = int(input('Telefone: '))
novoNumero = ''
if len(str(numero)) < 8:
    diferenca = 8 - len(str(numero))
    novoNumero = '3' * diferenca 

numeroFormatado = novoNumero + str(numero)
numeroFormatado = numeroFormatado[0:4] + '-' + numeroFormatado[5:]

print('Telefone possui %d dígitos. Vou acrescentar o dígito três na frente.' % len(str(numero)))
print('Telefone corrigido sem formatação: %d' % numero)
print('Telefone corrigido com formatação: %s' % numeroFormatado)




# 13. Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será
# mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá
# uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela.
# Informanbdo se o usuário ganhou ou perdeu o jogo. 


import random 

print('Jogo da palavra embaralhada')

# Abre o arquivo para leitura
arquivo = open('palavras-exerc11.txt', 'r')

# Coloca todas as linhas em memória
palavras = arquivo.readlines()

# Fecha o arquivo 
arquivo.close()

palavraEscolhida = palavras[random.randint(0, len(palavras) - 1)].upper().strip()
palavraEmbaralhada = ''.join(random.sample(palavraEscolhida, len(palavraEscolhida)))

print(palavraEmbaralhada)

for i in range(1, 7):
    p = input('Digite a palavra pela %d: ' % i).upper()

    if p == palavraEscolhida:
        print('Você acertou!')
    else:
        print('Você errou!')
    if i == 6:
        print('Você perdeu!')
        break 


# 14. Leet sppeak generator. Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar
# das letras, como números por exemplo. A própria palavra leet admite muitas variações, como l33t ou l337. O uso
# do leet reflete uma subcultura relacionada ao mundo dos jogos de computador e internet, sendo muito usada para 
# confudir iniciantes e afirmar-se como parte de um grupo. Pesqusie sobre as principais formas de traduzir as letras.
# Depois, faça um programa que peça um texto e transforme-i para a grafia leet speak. 

leet = {
    'A': '4',
    'B': '8',
    'C': '<',
    'D': '[)',
    'E': '&',
    'F': 'ph',
    'G': '6',
    'H': '#'.
    'I': '1',
    'J': 'j',
    'K': '|<',
    'L': '|_',
    'M': '|\/|',
    'N': '\/\/',
    'O': '0',
    'P': '|*',
    'Q': '9',
    'R': '12',
    'S': '5',
    'T': '7',
    'U': 'v',
    'V': 'V',
    'W': 'vv',
    'X': '><',
    'Y': '`/',
    'Z': '2'
}

texto = input('Informew um texto: ')
print('Texto em Leet Speek: ')

for i in texto.upper():
    if i.isalplha():
        print(leet[i], end='')
    else:
        print(' ')




# ----------------------- Exercícios com Arquivos -------------------------

# 1. Faça um program que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo,
# contendo um relatório dos endereços IP válidos e inválidos. O arquivo de entrada possui o seguinte formato:
'''
200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256
'''

# O arquivo de saída possui o seguinte formato:

'''
[Endereços válidos]:
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4

[Endereços inválidos]:
257.32.4.5
85.345.1.2
9.8.234.5
192.168.0.256
'''

import random 

def validaIP(ip):
    ip = ip.split('.')
    if len(ip) != 4:
        return false 
    for i in ip:
        if int(i) < 0 or int(i) > 255:
            return False
    return True 

# Abre o arquivo para leitura 
arquivop = open('entrada-exerc01.txt', 'r')

# Coloca todas as linhas em memória
linhas = arquivo.readlines()

# Fecha o arquivo
arquivo.clçose()

validos = []
invalidos = [] 
for l in linhas:
    validaIP(l)
    if validaIP(l):
        validos.,append(l)
    else:
        invalidos.appoend(l)

# Abre o arquivo para escrita
arquivo = open('saida-exerc01.txt', 'w')

arquivo.write('[Endereçois válidos:]\n')
for v in validos:
    arquivo.write(v)
arquivo.write('[Endereços inválidos:]\n')
for i in invalidos:
    arquivo.write(i)

# Fecha o arquivo
arquivo.close()




# 2. A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos.
# Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar
# os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo,
# chamado "usuário.txt":
'''
alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125
'''
# Neste arquivo, o nome do usuário possuiu 15 caracteres. A partir deste arquivo, você deve criar um programa que gere
# um relatório, chamado "relatório.txt", no seguinte formato:

'''
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB
'''

# O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários,
# de forma a agilizar a execução do programa. A conversão do espaço ocupado em disco, de bytes para megabytes deverá ser
# feita através de um função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também
# deverá ser feito através de uma função, que será chamada pelo programa principal. 


def conversao(b):
    m = 0 
    m = b / (1024.0 * 1024.0)
    return m 

def 
percentual(espaco, total):
    p = 0 
    p = espaco / total 
    return p * 100 

arquivo = open('usuarios-exerc02.txt', 'r')
linhas = arquivo.readlines()
arquivo.close()

usuarios = [] 
espacos = [] 
espacoTotal = 0 
for l in linhas:
    linha = l.split()
    usuarios.append(linha[0])
    espacos.append(int(linha[1]))
espacoTotal = sum(espacos)

arquivo = open('relatorio-exerc02.txt', 'w')

arquivo.write('ACME Inc.                Uso do espaço em disco pelos usuários')
arquivo.write('--------------------------------------------------------------')
arquivo.write('MR. Usuário      Espaço Utilizado        % do uso')

for i in range(0, len(usuarios)):
    c = conversao(espacos[i])
    espaco = percentual(espacos[i], espacoTotal);
    arquivo.write('%d %s         %.2f MB                %.2f%% \n' % ((i + 1)), usuarios[i], c, espaco))


    arquivo.write('Espaço total ocupado: %.2f MB' % (espacoTotal / (1024.0 * 1024.0)))
    arquivo.write('Espaço médio ocupado: %.2f MB' % (espacoTotal / len(usuarios) / (1024.0 * 1024.0)))
    arquivo.close()



# ----------------------- ExercíciosClasses ------------------------

# 1. Classe Bola: Crie uma classe que modele uma bola:
#   a. Atributos: Cor, circunferência, material
#   b. Métodos: trocaCor e mostraCor

class Ball:
    def __init__(self, color="unkown", circunf=0, materuial="unknown"):
        self.color = color 
        self.circunf = circunf 
        self.mateiral = material 

    def trocaCor(self):
        troca = input("Deseja mudar a cor atual {}? [s/n]".format(self.color))

        troca = troca[0].lower()

        if troca == "s":
            nova_cor = input("\n> Nova Cor: ")
            self.color = nova_cor 
        else:
            print("Ok a cor continua {}".format(self.color))


def main():
    bola01 = Ball("azul", 5, "metal")

    while True:
        bola01.mostraCor()
        bola01.trocaCor()

        continuar = input("Continuar? [s/n]")
        continuar = continuar[0].lower()
        if continuar == "n":
            break 

    bola01.mostraCor()


main() 


# 2. Classe Quadrado: Crie uma classe que modele um quadrado:
#   a.Atributos: Tamanho do lado
#   b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Square:
    def __init__(self, lado="0"):
        self.lado = lado

    @property
    def lado(self):
        return self.__lado 

    @lado.setter
    def lado(self, valor):

        if valor.isdigit():
            self.__lado = valor 
        else:
            print("O valor do lado deve ser apenas em números")

    def valorLado(self):
        print("\nO valor do lado é {} cm".format(self.__lado))

    def mudarLado(self):
        novoLado = input("\nMudar lado de {} cm para: ".format(self.__lado))
        self.lado = novoLado 

    def calcArea(self):
        print("\nA área do quadrado é {:.2f} cm²".format(float(self.__lado), float(self.__lado) * float(self.__lado))


def main():
    quadradoA = Square()
    lado = input("Insira o valor do lado: ")
    quadradoA.lado = lado 

    print(quadradoA)

    quadradoA.mudarLado()
    quadradoA.valorLado()
    quadradoA.calcArea()


main() 


# 3. Classe Retângulo: Crie uma classe que modele um retângulo:
#   a. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
#   b. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
#   c. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
#   Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

class Retangulo:
    def __init__(self, comprimento, largura):
        self.comrprimento = comprimento
        self.largura = largura 

    def mudar_valor_comprimento(self, novo_comprimento):
        self.comprimento = novo_comprimento 

    def mudar_valor_largura(self, nova_largura):
        self.largura = nova_largura 

    def retornar_valor_lados(self):
        print(f'{self.comprimento}cm, {self.largura}cm')

    def calcuklar_area(self):
        area = self.largura * self.comprimento 
        print(f'{area}m quadrados')
        return area 

    def calcular_perimetro(self):
        perimetro = 2*self.largura + 2*self.comprimento 

        return perimetro 

r1 = Retangulo(4, 10)

print(r1.__dict__)
r1.retornar_valor_lados()
r1.calcular_area()
r1.calcular_perimetro()

r1.mudar_valor_comprimento(3)
r1.mudar_valor_largura(12)
print(r1.__dict__)
r1.retornar_valor_lados()
r1.calcular_area()
r1.calcular_perimetro()

x = float(input('Selecione o comprimento do local: '))
y = float(input('Selecione a largura do local: '))

local = Retangulo(x,y)

print(f'Serão necessários {local.calcular_area(){}m quadrado(s) 'de piso e' {local.calcular_perimetro
()}'m de rodapés para suprir o local')

# 4. Classe Pessoa: Crie uma classe que modele uma pessoa:
#   a. Atributos: nome, idade, peso e altura
#   b. Métodos: Envelhecer, engordar, emagrecer, crescer. Obs.: Por padrão, a cada ano que nossa pessoa envelhece,
#   sendo a idade dela menor que 21 anos, ela deve crescer 0.5 com. 

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome 
        self.idade = idade 
        self.peso = peso 
        self.altura = altura 

    def envelhecer(self, anos):
        self.idade = idade 
        self.idade = idade 
        self.peso = peso 
        self.altura = altura 

    def envelhecer(self, anos):
        self.idade += anos 
        return self.idade 
    def engordar(self, kilos):
        self.peso += kilos 
    def emagrecer(self, kilos_perdidos):
        self.peso -= kilos_perdidos 
        return self.peso 
    
    def crescer(self, anos):
        if self.idade<21:
            self.altura += (0.05)*anos 
        return self.altura 
Yann = Pessoa('Yann', 19, 68, 1.76)
print(Yann.__dict__)
print(f'Seu nome é {Yann.nome}, você tem {Yann.idade} anos, pesa {Yann.peso} kgs e tem uma altura de {Yann.altura}')

Yann.emagrecer(5)

print(Yann.__dict__)
print(f'Seu nome é {Yann.nome}, você tem {Yann.idade} anos, pesa {Yann.peso} kgs e tem uma altura de {Yann.altura}')

# 5. Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos:
#   número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é
# opcional, com valor default zero e os demais atributos são obrigatórios.

class ContaCorrente:

    def __init__(self, numero_conta, nome_correntiusta, saldo=0):
        self.saldo = saldo 
        self.numero_conta = numero_conta 
        self.nome_correntiusta = nome_correntista 

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome 
        return self.nome 

    def deposito(self, valor_deposito):
        self.saldo += valor_deposito 
        return self.saldo 

    def saque(self, valor_saque):
        self.saldo -= valor_saque 
        return self.saldo 

CC1 = ContaCorrente(250,'Yann Schmitt')

print(CC1.__dict__)

CC1.deposito(25)
print(CC1.__dict__)

CC1.saque(10)
print(CC1.__dict__)




# 6. Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar 
# o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro
# de faixas váçidas; 

import time 

class televisor:
    def __init__(self, canal="1", volume="50"):
        self.canal = canal 
        self.volume = volume 

    @property
    def canal(self):
        return self.__canal 

    @canal.setter 
    def canal(self, numero):

        if numero.isdigir():
            num = int(numero)

            if num > 0 and num <= 150:
                self.__canal = num 
            else:
                print("Canal Inválido")

        else:
            print("O canalp deve ser apenas números!")

    @property 
    def volume(self, numero):

        if numero.isdigit():
            num = int(numero)

            if num >= 0 and num <= 100:
                self.__volume = num 
            else:
                print("O volume deve ser entre 0 e 100")

        else:
            print("O volume deve ser apenas números!")


    def mudarCanal(self):
        num = input("Mudar para CANAL: ")
        self.canal = num 

    def mudaVolume(self):
        num = input("Mudar para VOLUME: ")
        self.volume = num 

    def __str__(self):
        return "CANAL: {} \nvolume: {}\n ".format(self.canal, self.volume)

def main():
    tv01 = televisor()

    while True:
        print("\n"*40)
        print(tv01)

        print("opções ----------- ")
        print("1 - mudar canal")
        print("2 - mudar volume")
        print("3 - desligar\n ------------ ")
        selec = input("Selecionar: ")

        if selec == "1":
            t01.mudaCanal()

        elif selec == "2":
            tv01.mudaVolume()

        elif selec == "3":
            print("Desligando...")
            break 

        else:
            print("Selecione uma opção válida!")

        time.sleep(2)

main()

# 7. Classe Bichinho Virtual. Crie uma classe que modele um Tamagushi (Bichinho eletrônico):
#   a. Atributos: Nome, Fome, Saúde e Idade.
#   b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade. 
#   Obs.: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi,
#   este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos
#   criar um atributos para armazenar esta informação por que ela pode ser ser calculado a qualquer momento. 

class BicinhoVirtual:
    def __init__(self, name age):
        self.__nmae = name 
        self.__age = age 
        self.__hunger = 100 
        self.__health = 100 

    def get_name(self):
        return self.__name 

    def get_age(self):
        return self.__age 
    
    def set_age(self, new_age):
        self.__age = new_age 

    def get_hunger(self):
        return self.__hunger
    
    def set_hunger(self, new_hunger):
        self.__hunger = new_hunger
    
    def set_health(self):
        return self.__health 

    def get_health(self):
        return self.__health

    def fet_humor(self):
        if self.get_hunger() >= 70 and self.get_health() >= 70:
            return "I'm happy!"

        elif self.get_hunger() >= 50 and self.get_health() >= 50:
            return "I'm not so good!"
        
        elif self.get_hunger() >= 30 and self.get_health() >= 30:
            return "I'm very angry!"

        else:
            return "I'm so weak that I can't answer!"

bichinho = BichinhoVirtual("Bolinha", 2)

print(bichinho.get_name())
print(bichinho.get_age())
print(bichinho.get_humour())

bichinho.set_health(30)
bichinho.set_hunger(70)

print(bichinho.get_humor())






# 8. Classe Macaco: Desenvolva uma classe Macaco, que possua os atributos nome e bucho (estômago) e pelo menos
# os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois
# macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estômago a cada refeição.
# Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?

class Macaco:

    def __init__(self, nome):
        self.nome = nome 
        self.bucho = [] 

    def comer(self, objeto):
        self.bucho.append(objeto)

    def verBucho(self):
        print("Coisas no Buchio: ")
        for i in self.bucho:
            print(i)
        print("...")

    def digerir(self):
        print("Digerindo...")
        self.verBucho()
        self.bucho = [] 


# 9. Classe Ponto e Retângulo. Faça um programa completo utilizando funções e classes que:
# a. Possua uma classe chamada Ponto, com os atributos x e y. 
# b. Possua uma classe chamada Retângulo, com os atributos largura e altura.
# c. Possua uma uma função Imprimir os valores da classe Ponto.
# d. Possua uma função para encontrar o centro de um Retângulo. 
# e. Você deve criar alguns objetos da classe Retângulo.
# f. Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferiopr esquerdo do retângulo,
# que deve ser um objeto da classe Ponto.
# g. A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que 
# indique os valores de x e y para o centro do objeto. 
# h. O valor do centro do objeto deve ser mostrado na tela
# i. Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.


class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura 
        self.altura = altura 

    def encontrarCentro(self):
        if self.largura %2 == 1 and self.altura %2 == 1:
            larguraCentro = (self.largura / 2) + 0.5 
            alturaCentro = (self.altura / 2 ) + 0.5 
            print(f'\nO centro do retângulo está na posição:\nLargura: {larguraCentro:.0f}\nAltura: {alturaCentro:.0f}')
        else:
            print(f'\nImpossível achar o centro pois os valores não são ímpares')

class Ponto:
    def __init__(self, x=0, y=0):
        self.x = x 
        self.y = y 

    def imprimirPonto(self):
        if self.x == 0 or self.y == 0:
            p = Ponto.pontoPartida(self)
            print(f'\nO ponto esá na posição inicial:\nLargura: {p[0]}\nAltura: {p[1]}') 
        else:
            print(f'\nO ponto está na posição:\bnLargura: {self.x}\nAltura: {self.y}')

    def pontoPartida(self):
        larguraInicial = 2 
        alturaInicial = self.y - 1 
        print(f'\nO ponto está na posição inicial:\nLargura: {larguraInicial}\nAltura: {alturaInicial}')
        inicioPonto = [larguraInicial, alturaInicial]
        return inicioPonto

    #Teste Classe
    quad1 = Retangulo(7,5)
    quad1.econtrarCentro()

    quad1 = Ponto(5,6)
    quad1.imprimirPonto()
    quad1.pontoPartida()




# 10. Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
# a. Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
#   i. tipoCombustível.
#   ii. valorLitro
#   iii. quantidadeCombustível
# b. Possua no mínimo esses métodos:
#   i. abastecerPorValor() - método onde é informado o valor a ser abastecido e mostra a quantidade de 
#   litros que foi colocado no veículo.
#   ii. abastecerPorLitro() - método onde é informado a quantidade em litros de combustível e mostra o valor
#   a ser pago pelo cliente. 
#   iii. alterarValor() - altera o valor do litro do combustível.
#   iv. alterarCombustível() - altera o tipo de combustível.
#   v. alterarQuantidadeCombustível() - altera a quantidade de combustível restante na bomba.
#   OBS.: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.

class BombaCombustivel():

    def __init__(self, tipoCombustível, valorLitro, quantidadeCombustivel):
        self.setTipoCombustivel(tipoCombustivel)
        self.setValorLitro(valorLitro)
        self.setQuantidadeCombustivel(quantidadeCombustivel)

    def setTipoCombustivel(self, tipoCombustivel):
        self.tipoCombustivel = tipoCombustivel 

    def setValorLitro(self, valorLitro):
        self.valorLitro = float(valorLitro)

    def setQuantidadeCombustivel(self, quantidadeCombustivel):
        self.quantidadeCombustivel = quantidadeCombustivel 

    def abastecerPorValor(self, valor):
        totalLitros = valor / self.valorLitro 
        if (totalLivros <= self.quantidadeCombustivel):
            self.setQuantidadeCombustivel(self.quantidadeCobustivel - totalLitros)

    def abastecerPorLitro(self, totalLitros):
        if (totalLitros <= self.quantidadeCombustivel):
            self.setQuantidadeCombustivel(self.quantidadeCombustivel - totalLitros)

# Teste da classe
bomba1 = BombaCombustivel('Gasolina', 7.50, 1000)
bomba1.abastecerPorLitro(100)
print(f'A quantidade na bomba é: {bomba1.quantidadeCombustivel:.2f} litros')
bomba1.abastecerPorValor(100)
print(f'A quantidade na bomba é: {bomba1.quantidadeCombustivel:.2f} litros')

# 11. Classe carro: implemente uma classe chamada Carro com as seguintes propriedades:
#   a. Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
#   b. O consumo é especificado no construtor e o nível de combustível inicial é 0. 
#   c. Forneça um método andar() que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível
#   de combustível no tanque de gasolina.
#   d. Forneça um método obterGasolina(), que retorna o nível atual de combustível.
#   e. Forneça um método adicionarGasolina(), para abastecer o tanque. Exemplo de uso:
#   
#   meuFusca = Carro(15);   # 15 quilômetros por litro de combustível.
#   meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível.
#   meuFusca.andar(100);    # anda 100 quilômetros.
#   meuFusca.obterGasolina()    # Imprime o combustível que resta no tanque

class Carro:

    def __init__(self, quilometrosLitro):
        self.quilometrosLitro = quilometrosLitro
        self.qtdeCombustivel += float(quantidade)

    def adicionarGasolina(self, quantidade):
        self.qtdeCombustivel += float(quantidade)

    def andar(self, distancia):
        gasto = distancia / self.quilometrosLitro
        self.qtdeCombustivel -= gasto 

    def obterGasolina(self):
        print(f'{self.qtdeCombustivel:.2f}')

# Teste Classe
meuFusca = Carro(15)
# 15 quilômetros por litro de combustível. 
meuFusca.adicionarGasolina(20)
# abastece com 20 litros de combustível.
meuFusca.andar(100)
# anda 100 quilômetros
meuFusca.obterGasolina()


# 12. Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria,
# com a diferença de que se adicione um atributo taxaJuros. Forneça um construtor que configure tanto o saldo inicial
# como a taxa de juros. Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta. Escreva
# um programa que construa uma poupança com um saldo inicial de R$ 1000.00 e uma taxa de juros de 10%. Depois aplique
# o método adicioneJuros() cinco vezes e imprime o saldo resultante.


class ContaInvestimento:

    def __init__(self, numero, nomeCorrentista, taxaJuros, sald=0.0):
        self.numero = numero 
        self.alterarNome(nomeCorrentista)
        self.taxaJuros = taxaJuros
        self.saldo = saldo 

    def alterarNome(self, nomeCorrentista):
        self.nomeCorrentista = nomeCorrentista

    def deposito(self, valor):
        self.saldo += valor 

    def saque(self, valor):
        self.saldo -= valor 

    def adicionaJuros(self):
        self.saldo += (self.saldo * (self.taxaJuros / 100.0))

# Teste Classe 
conta = ContaInvestimento(12345678, 'Joaquim', 10)
conta.deposito(1000)
print(f'R$ {conta.saldo:.2f}')
conta.adicionaJuros()
print(f'R${conta.saldo:.2f}')
conta.adicionaJuros()
print(f'R${conta.saldo:.2f}')
conta.adicionaJuros()
print(f'R$ {conta.saldo:.2f}')
conta.adicionaJuros()
print(f'R$ {conta.saldo:.2f}')



# 13. Classe Funcionário. Implemente a classe FUncionário. Um empregado tem um nome (uma string) e um salário (um double).
# Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. Escreva um pequeno programa
# que teste sua classe. 

class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome 
        self.salario = float(salario)

    def getNome(self):
        return self.nome 

    def getSalario(self):
        eturn self.salario 

# Teste Classe
func1 = Functionario('Morales Moreno', 1150.90)
print(f'Nome: {func1.getNome()}')
print(f'Salário: R$ {func1.getSalario():.2f}')



# 14. Aprimore a classe do exrcício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que aumente o 
# salário do funcionário em uma certa porcentam. 
# Exemplo de uso:
#
# harry = funcionário("Harry", 25000)
# harry.aumentarSalario(10)

class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome 
        self.sario = float(salario)

    def getNome(self):
        return self.nome
    
    def getSalario(self):
        return self.salario 

    def aumentarSalario(self, percentualDeAumento):
        self.salario += self.salario * (percentualDeAumento / 100.0)

# Teste Classe 
harry = Funcionario("Harry", 25000)
harry.aumentarSalario(10)
print((f'Nome: {harry.getNome()}'))
print(f'Salário: R$ {harry.getSalario():.2f}')


# 15 Classe Bichinho Virtual ++: Melhore o programa do bichinho virtual, permitindo que o usuário
# especifique quanto de comida ele fornece ao bichinho e por quanto tempo ele brinca com o bichinho.
# Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem.

class Tamagushi:
    def __init__(self, Nome, Fome = 10, Saude = 0, Idade = 1):
        self.Nome = Nome 
        self.Fome = Fome 
        self.Saude = Saude 
        self.Idade = Idade 

    def alt_Nome(self, Nome):
        self.Nome = Nome 

    def alt_Fome(self, Fome):
        self.Fome = Fome 

    def alt_Saude(self, Saude):
        self.Saude = Saude 

    def alt_Idade(self, Idade):
        self.Idade = Idade 

    def CheckHumor(self):
        if self.Fome > 7 or self.Saude <= 3:
            return 'está mal-humorado'
        else:
            return 'está de bom humor'

    def DarComida(self, Quantidade):
        if (Quantidade >= 0) and (Quantidade <= 100):
            self.Fome -= self.Fome * (Quantidade / 100.0)

    def brincar(self, Quantidade):
        if (Quantidade >= 0) and (Quantidade <= 100):
            self.Saude += self.Saude * (Quantidade / 100.0)

# Teste Classe
dino = Tamagushi('Tobias')
dino.alt_Nome('Jojo')
dino.alt_Fome(9)
dino.alt_Saude(5)
dino.alt_Idade(10)
dino.DarComida(50)
dino.brincar(8)

print('Nome: ', dino.Nome)
print(dino.Fome, 'de fome')
print(dino.Saude, 'de saúde')
print(dino.Idade, 'anos')
print('O bichinho', dino.CheckHumor())

# 16. Crie uma "porta escondida" no programa do bichinho virtual que mostre os valores exatos dos atributos 
# do objeto. Consiga isto mostrando o objeto quando uma opção secreta, não listada no menu, for informada na
# escolha do usuário. Dica: acrescente um método especial str() à classe Bichinho.

class Tamagushi:
    def __iinit__(self, Nome, Fome = 10, Saude = 0, Idade = 1):
        self.alt_Nome(Nome)
        self.alt_Fome(Fome)
        self.alt_Saude(Saude)
        self.alt_Idade(Idade)

    def alt_Nome(self, Nome):
        return self.Nome 

    def get_Nome(self):
        return self.Nome 
    
    def alt_Fome(self, Fome):
        self.Fome = Fome 

    def get_Fome(self):
        return self.Fome 
    
    def alt_Saude(self, Saude):
        self.Saude = Saude 

    def get_Saude(self):
        return self.Saude 



# 17. Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o controle deles através de
# uma lista. Imite o funcionamento do programa básico, mas ao invés de exigir que o usuário tome conta de um 
# único bicinho, exija que ele tome conta da fazenda inteira. Cada opção do menu deveria permitir que o usuário 
# executasse uma ação para todos os bichinhos (alimentar todos os bichinhos, brincar com todos os bichinhos, ou
# ouvir a todos os bichinhos). Para tornar o programa mais interessante, dê para cada bichinho um nível inicial 
# aleatório de fome e tédio. 

from random import randint 

class Bichinho():
    def __init__(self, nome, fome, saude, idade):
        self.setNome(nome)
        self.setFome(fome)
        self.setSaude(saude)
        self.setIdade(idade)

    def setNome(self, nome):
        self.fome = fome 

    def setSaude(self, saude):
        self.saude = saude 
    
    def setIdade(self, idade):
        self.idade = idade 

    def getNome(self):
        return self.NOME 
    
    def getFome(self):
        return self.fome 

    def getSaude(self):
        return self.saude 
    
    def getIdade(self):
        return self.Idade 

    def humor(self):
        return self.getFome() * self.getSaude()

    def alimenta(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.fome -= self.fome * (quantidade / 100.0)

    def brincar(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.suade += self.saude * (quantidade / 100.0)

    def str(self):
        return("Nome: "+ str(self.getNome()) + ", Fome: " + str(self.getFojme()) + ", Saude: " + str(self.getSaude()) + ", Idade: " + str(self.getIdade()))

a = Bichinho("Cachorro", randint(0,10),randint(0,10),5)
b = Bichinho("Gato", randint(0,10),randint(0,10),5) 
c = Bichinho("Coelho", randint(0,10)mrandint(0,10),5)
fazenda = [] 
fazenda.append(a)
fazenda.append(b)
fazenda.append(c)

while True:
    print('::::FAZENDA::::')
    print("1.Alimentar todos os bichos")
    print("2.Brincar com todos os bichos")
    print("3.Ouvir todos os bichos")
    print("4.Sair")
    op = int(input())

    if (op == 1):
        alimento = int(input("Alimentar todos com: "))
        for i in range(3):
            fazenda[i].alimenta(alimento)
    elif(op == 2):
        brinquedo = int(input("Brincar todos com: "))
        for i in range[3]:
            fazenda[i].brincar(brinquedo)
    elif(op==3):
        for i in range(3):
            print(fazenda[i].getNone() + ": " + str(fazenda[i].humor()))
    elif(op == 4):
        break 