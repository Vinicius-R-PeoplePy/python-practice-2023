# como não escrever uma função

def soma(L):
    total=0 
    x = 0 
    while x<5:
        x+=1 
    return total 
L=[1,7,2,9,15]
print(soma(L))
print(soma([7,9,12,3,100,20,4]))

#################################

#cálculo do fatorial 

def fatorial(n):
    fat = 1 
    while n>1:
        fat*=n 
        n-=1
    return fat 

## ou 

def fatorial(n):
    fat=1
    x=1
    while x<=n:
        fat*=x 
        x+=1 
    return fat 

##################################

def pesquisa_lista(lista, elemento):
    try:
        indice = lista.index(elemento)
        return f'O elemento {elemento} foi encontrado no índice {indice}'
    except ValueError:
        return f'O elemento {elemento} não foi encontrado na lista.'
    
minha_lista = [1,2,3,4,5]
resultado = pesquisa_lista(minha_lista,3)
print(resultado)

##################################

def soma(L):
    total = 0 
    for elemento in L: 
        total += elemento 
    return total 

L = [1, 7, 2, 9, 15]
print(soma(L)) # 34
print(soma([7, 9, 12, 3, 100, 20, 4])) # 155 

##################################

L=[5,7,8]
sum(L)
max(L)
min(L)

# Variáveis locais e globais 

# Uma variável global é definida fora de uma função, pode ser vista por todas as funções do módulo e por todos os módulos que importam o módulo que a definiu. 

EMPRESA="Unidos Venceremos Ltda"
def imprime_cabeçalho():
    print(EMPRESA)
    print("-" * len(EMPRESA)) # output: nada

##################################

# Variáveis globais devem ser utilizadas o mínimo possível em seus programas, pois dificultam a leitura e violam o encapsuamento da função. O encapsulamento é comprometido porque a função depende de uma variável externa, ou seja, que não é declarada dentro da função nem recebida como parâmetro. 

# Tente utilizar variáveis globais apenas para configuração e com valores constantes.

a=5
def muda_e_imprime():
    a=7
    print("A dentro da função: %d" % a)
print("a antes de mudar: %d" % a)
muda_e_imprime()
print("a depois de mudar: %d" % a)

##################################

# Se quisermos modificar uma variável global dentro de uam função devemos informar que estamos usando uma variável global antes de inicializá-la, na primeira linha de nossa função.

a=5
def muda_e_imprime():
    global a 
    a = 7 
    print("A dentro da função: %d" % a)
print("a antes de mudar: %d" % a)
muda_e_imprime()
print("a depois de mudar: %d" % a)

##################################

def fatorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fatorial(n-1)

##################################

# função modificada para facilitar o rastreamento

def fatorial(n):
    print("Calculando o fatorial de %d" % n)
    if n==0 or n==1:
        print("Fatorial de %d = 1" % n)
        return 1
    else:
        fat = n*fatorial(n-1)
        print(" fatorial de %d = %d" % (n, fat))
    return fat
fatorial(4)

##################################

def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

##################################

# calcular o maior múltiplo comum (M.M.C.) entre dois números

def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

# Exemplo de uso 

numero1 = 48 
numero2 =  18 
resultado = mdc(numero1, numero2)
print(f"O M.D.C. entre {numero1} e {numero2} é {resultado}")

################################## 

# calcular o menor múltiplo comum (M.M.C.) entre dois números

def mdc(a, b):
    while b != 0:
        a, b = b, a % b 
    return a 

def mmc(a, b):
    return abs(a * b) // mdc(a, b)

numero1 = 48 
numero2 = 18 
resultado = mmc(numero1, numero2)
print(f"O M.M.C. entre {numero1} e {numero2} é {resultado}")

##################################

# calcular Fibonacci

def fibonacci_iterativo(n):
    if n <= 0:
        return "Por favor, forneça um número inteiro positivo para calcular a sequência de Fibonacci"
    elif n == 1:
        return [0]
    elif n == 2: 
        return [0, 1]
    else:
        fibonacci_sequence = [0, 1]
        for i in range(2, n):
            next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_term)
        return fibonacci_sequence

n = 10 
resultado = fibonacci_iterativo(n)
print(f"Os primeiro {n} termos da sequência de Fibonacci são: {resultado}")

##################################

# Validação sem usar função

while True:
    v=int(input("Digite um valor entre 0 e 5: "))
    if v<0 or v>5:
        print("Valor inválido.")
    else:
        break 

##################################

def verificar_comprimento(paalavra, minchar, maxchar):
    palavra = input("Digite uma palavra: ")
    comprimento = len(palavra)

    if comprimento <= minchar or comprimento >= maxchar:
        return False 
    else:
        return True

comprimento_minimo = 3 
comprimento_maximo = 10
resultado = verificar_comprimento("", comprimento_minimo, comprimento_maximo)
print(resultado)

##################################
'''Escreva uma função que receba uma string e uma lista. A função
deve comparar a string passada com os elementos da lista, também passada como parâmetro. Retorne verdadeiro se a string for encontrada dentro da lista, e falso em caso contrário'''

def verificar_string_na_lista(minha_string, minha_lista):
    return minha_string in minha_lista 

string_exemplo = "python"
lista_exemplo = ["java", "c++", "python", "javascript"]
resultado = verificar_string_na_lista(string_exemplo, lista_exemplo)

if resultado:
    print(f'A string "{string_exemplo}" foi encontrada na lista.')
else:
    print(f'A string "{string_exemplo}" não foi encontrada na lista.')

##################################

# função para imprimir uma barra na tela com parâmetros opcionais

def barra(n=40, caracteres="*"):
    print(caracteres * n)

barra()

##################################

# função soma com parâmetros obrigatórios e opcionais

def soma(a, b, imprime=False):
    s = a + b 
    if imprime:
        print(s)
    return s 

soma(2,3)
soma(3,4, True)

##################################

'''
definição inválida da função soma com parâmetros opcionais antes do obrigatórios

def soma(imprime=True, a, b):
    s = a + b 
    if imprime:
        print(s)
    return s
'''

##################################

# Função retângulo com parâmetros obrigatórios e opcionais

def retângulo(largura, altura, caractere="*"):
    linha = caractere * largura 
    for i in range(altura):
        print(linha)

retângulo(3,4)
retângulo(largura=3, altura=4)
retângulo(altura=4, largura=3)
retângulo(caractere="-", altura=4, largura=3)
##################################

# Funções como parâmetro 

def soma(a,b):
    return a+b
def subtração(a,b):
    return a-b
def imprime(a,b, foper):
    print(foper(a,b))
imprime(5,4, soma)
imprime(10,1, subtração)

##################################

# Configuração de funções com funções 

def imprime_lista(L, fimpressão, fcondição):
    for e in L: 
        if fcondição(e):
            fimpressão(e)
def imprime_elemento(e):
    print("Valor: %d" % e)
def épar(x):
    return x % 2 == 0
def éimpar(x):
    return not épar(x)
L=[1,7,9,2,11,0]
imprime_lista(L, imprime_elemento, épar)
imprime_lista(L, imprime_elemento, éimpar)

##################################

# Empacotamento de parâmetros em uma lista

def soma(a,b):
    print(a+b)
L=[2,3]
soma(*L) #1

'''
Em #1, estamos utilizando o asterisco para indicar que queremos desempacotar a lista L utilizando seus valores como parâmetro para a função soma. No exemplo, L[0] será atribuído a 'a' e L[1] a 'b'. Esse recurso permite armazenar nossos parâmetros em listas e evita construções do tipo somsa(L[0], L[1])
'''

##################################

# Outro exemplo de empacotamento de parâmetros em uma lista

def barra(n=10, c="*"):
    print(c*n)
L=[ [5, "-"], [10, "*"], [5], [6, "."] ]
for e in L:
    barra(*e)




##################################

# Função soma com número indeterminado de parâmetros

def soma(*args):
    s = 0
    for x in args:
        s += x
    return s
soma(1,2)
soma(2)
soma(5,6,7,8)
soma(9,10,20,30,40)

##################################

# Função imprime_maior com número indeterminado de parâmetros

def imprime_maior(mensagem, *numeros):
    maior = None 
    for e in numeros: 
        if maior == None or maior < e:
            maior = e 
    print(mensagem, maior)
imprime_maior("Maior:",5,4,3,1)
imprime_maior("Max:", *[1,7,9])

##################################

# função lambda que recebe um valor e retorna o dobro dele

a=lambda x: x*2
print(a(3))

##################################

# Função lambda que recebe mais de um parâmetro 

aumento=lambda a,b: (a*b/100)
aumento(100, 5)

##################################

def valida_inteiro(mensagem, mínimo, máximo):
    while True:
        try:
            v=int(input(mensagem))
            if v >= mínimo and v <= máximo:
                return v
            else:
                print("Digite um valor entre %d e %d" % (mínimo, máximo))
        except:
            print("Você deve digitar um número inteiro.")

valida_inteiro("Digite um número de 0 a 5:", 0, 5)


##################################
'''
import entrada # salvar código acima como entrada.py 
L=[] 
for x in range(10):
    L.append(entrada.valida_inteiro("Digite um número: ", 0, 20))
print("Soma: %d" % (sum(L)))
'''
'''
Você deve utilizar esse recurso com atenção, pois informar o nome do módulo antes da função é muito útil quando os programsa crescem, servindo de dica para que se saiba que módulo define tal função, facilitando sua localização e evitando o que se chama de conflito de nomes. Dizemos que um conflito de nomes ocorre quando dois ou mais módulos definem funções com nomes idênticos. Nesse caso, utilizar a notação de chamada módulo.função resolve o conflito, pois a combinação do nome do módulo com o nome da função é única, evitando a dúvida de descobrir o módulo que define a função que estamos chamando.

Outra construção que deve ser utilizada com cuidado é from entrada import *. Nesse caso, estaríamos importando todas as definições do módulo entrada, e não apenas a função valida_inteiro. Essa construção é perigosa, porque se dois módulos definerem funções com o mesmo nome, a função utilizada no programa será a do último import. Isso é especialmente difícil de encontrar em programas grandes, e seu uso não é aconselhado.
'''
##################################

# checar http://pt.wikipedia.org/wiki/Distribuição_de_probabilidade

# Gerando números aleatórios

import random 
for x in range(10):
    print(random.randint(1,100))

##################################

import random 
n=random.randint(1,10)
x=int(input("Escolha um número entre 1 e 10: "))
if (x==n):
    print("Você acertou!")
else:
    print("Você errou.")

##################################

import random 
for x in range(10):
    print(random.random())

##################################

import random 
for x in range(10):
    print(random.uniform(15,25))

##################################

import random
print(random.sample(range(1,101), 6))

##################################

import random 
a=list(range(1,11))
random.shuffle(a)
print(a)

##################################

a=5
print(type(a))
b='Olá'
print(type(b))
c=False 
print(type(c))
d=0.5
print(type(d))
f=print
print(type(f))
g=[]
print(type(g))
h={}
print(type(h))
def função():
    pass
print(type(função))

##################################

import types 

def diz_o_tipo(a):
    tipo = type(a)
    if tipo == str:
        return("String")
    elif tipo == list:
        return("Lista")
    elif tipo == dict:
        return("Dicionário")
    elif tipo == int:
        return("Número Inteiro")
    elif tipo == float:
        return("Número decimal")
    elif tipo == types.FunctionType:
        return("Função")
    elif tipo == types.BuiltinFunctionType:
        return("Função interna")
    else:
        return(str(tipo))
print(diz_o_tipo(10))
print(diz_o_tipo(10.5))
print(diz_o_tipo("Alô"))
print(diz_o_tipo([1,2,3]))
print(diz_o_tipo({"a":1, "b":50}))
print(diz_o_tipo(print))
print(diz_o_tipo(None))

##################################

L=[ 2, "Alô", ["!"], { "a":1, "b":2}]
for e in L:
    print(type(e))

##################################

L=["a", ["b", "c", "d"], "e"]
for x in L:
    if type(x) == str:
        print(x)
    else:
        print("Lista:")
        for z in x:
            print(z)

##################################

def imprimir_lista_recursiva(lista, nível=0):
    for elemento in lista:
        if type(elemento) == list:
            imprimir_lista_recursiva(elemento, nível+1)
        else:
            espaços = " " * nível * 2 
            print(f"{espaços}{elemento}")

minha_lista = [1, [2,3,4, [5,6,7]]]
imprimir_lista_recursiva(minha_lista)

'''
Neste exemplo, a função 'imprimir_lista_recursiva' aceita uma lista e um parâmetro opcional 'nível', que representa o nível de aninhamento atual. A função percorre os elementos da lista, e se encontrar outra lista, chama recursivamente a função para imprimir os elementos da lista interna com um nível de indentação maior. Se o elemento não for uma lista, imprime-o com a indentação apropriada.

O exemplo de uso demonstra como chamar a função com a lista fornecida e imprimir os elementos considerado a estrutura aninhada.
'''

##################################

'''
modos de abertura de arquivos

modo            operações

r               leitura

w               escrita, apaga o conteúdo se já existir

a               escrita, mas preserva o conteúdo se já existir

b               modo binário

+               atualização(leitura e escrita)

Os modos podem ser combinados (r+ , w+ , a+, r+b, w+b, a+b)
'''

# abrindo, escrevendo e fechando um arquivo 

arquivo=open("números.txt","w")
for linha in range(1,101):
    arquivo.write("%d\n" % linha)
arquivo.close()

##################################

arquivo=open("números.txt","r")
for linha in arquivo.readlines():
    print(linha)
arquivo.close 

##################################

# Impressão dos parâmetros passados na linha de comando 
import sys
print("Número de parâmetros: %d" % len(sys.argv))
for n, p in enumerate(sys.argv):
    print("Parâmetro %d = %s" % (n, p))

##################################
'''Escreva um programa que receba o nome de um arquivo pela linha
de comando e que imprima todas as linhas desse arquivo.'''

import sys 

def imprimir_linhas_do_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                print(linha, end='')
    except FileNotFoundError:
        print(f"Erro. O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Erro: {e}")

if len(sys.argv) != 2:
    print("Por favor, forneça o nome do arquivo como argumento.")
else:
    nome_do_arquivo = sys.argv[1]
    imprimir_linhas_do_arquivo(nome_do_arquivo)

##################################

'''Modifique o programa do exercício 9.1 para que receba mais dois
parâmetros: a linha de início e a de fim para impressão. O programa deve imprimir apenas as linhas entre esses dois valores (incluindo as linhas de início e fim). '''

import sys 

def imprimir_linhas_do_arquivo(nome_arquivo, linha_inicio, linha_fim):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()

            linha_inicio = max(1, min(linha_inicio, len(linhas)))
            linha_fim = max(linha_inicio, min(linha_fim, len(linhas)))

            for i in range(linha_inicio - 1, linha_fim):
                print(linhas[i], end='')
    except FileNotFoundError:
        print(f"Erro. O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Erro: {e}")

if len(sys.argv)!= 4:
    print("Por favor, forneça o nome do arquivo, a linha de início e a linha de fim como argumentos.")
else:
    nome_do_arquivo = sys.argv[1]
    linha_inicio = int(sys.argv[2])
    linha_fim = int(sys.argv[3])
    imprimir_linhas_do_arquivo(nome_do_arquivo, linha_inicio, linha_fim)

##################################

# Gravação de números pares e ímpares em arquivos diferentes

ímpares=open("ímpares.txt", "w")
pares=open("pares.txt", "w")
for n in range(0,1000):
    if n % 2 == 0:
        pares.write("%d\n" % n)
    else:
        ímpares.write("%d\n" % n)

ímpares.close()

pares.close()

##################################

# Filtragem exclusiva dos múltiplos de 4

múltiplos4=open("múltiplos de 4.txt", "w")
pares=open("pares.txt")
for l in pares.readlines():
    if int(l) % 4 == 0:
        múltiplos4.write(l)
pares.close()
múltiplos4.close()

##################################

'''Crie um programa que leia os arquivos pares.txt e ímpares.txt e que
crie um só arquivo pareseimpares.txt com todas as linhas dos outros dois arquivos,
de forma a preservar a ordem numérica'''

def combinar_arquivos(arquivo_pares, arquivo_impares, arquivo_combinado):
    try:
        with open(arquivo_pares, 'r') as pares, open(arquivos_impares, 'r') as impares, open(arquivo_combinado, 'w') as combinado:

            #Combina as linhas preservando a ordem numérica 
            for linha in sorted(linhas_pares + linhas_impares, key=lambda x: int(x)):
                combinado.write(linha)
        
        print(f"Arquivo '{arquivo_combinado}' criado com sucesso")
    except FileNotFoundError:
        print("Erro: Um dos arquivos não foi encontrado.")
    except Exception as e:
        print(f"Erro: {e}")

arquivo_pares = "pares.txt"
arquivo_impares = "ímpares.txt"
arquivo_combinado = "pareseimpares.txt"

combinar_arquivos(arquivo_pares, arquivo_impares, arquivo_combinado)

##################################

'''Crie um programa que receba o nome de dois arquivos como parâmetros da linha de comando e que gere um arquivo de saída com as linhas do primeiro e do segundo arquivo'''

import sys 

def combinar_arquivos(arquivo1, arquivo2, arquivo_saída):
    try:
        with open(arquivo1, 'r') as f1, open(arquivo2, 'r') as f2, open(arquivo_saída, 'w') as saída:
            linhas_arquivo1 = f1.readlines()
            linhas_arquivo2 = f2.readlines()

            # Escreve as linhas do primeiro arquivo
            for linha in linhas_arquivo1:
                saída.write(linha)

        print(f"Arquivo '{arquivo_saída}' criado com sucesso.")
    except FileNotFoundError:
        print("Erro: Um dos arquivos não foi encontrado.")
    except Exception as e:
        print(f"Erro: {e}")

# Verifica se os parâmetros foram fornecidos corretamente 
if len(sys.argv) != 4:
    print("Por favor, forneça o nome dos dois arquivos e o nome do arquivo de saída como argumentos.")
else:
    nome_arquivo1 = sys.argv[1]
    nome_arquivo2 = sys.argv[2]
    nome_arquivo_saída = sys.argv[3]
    combinar_arquivos(nome_arquivo1, nome_arquivo2, nome_arquivo_saída)

# para executar o programa, use o comando:
# python nome_do_programa.py arquivo1.txt arquivo2.txt arquivo_saída.txt

##################################

'''Crie um programa que inverta a ordem das linhas do arquivo pares.
txt. A primeira linha deve conter o maior número; e a última, o menor.'''

def inverter_ordem_linhas(arquivo_entrada, arquivo_saida):
    try:
        with open(arquivo_entrada, 'r') as entrada, open(arquivo_saida, 'w') as saída:
            linhas = entrada.readlines()

            # Inverte a ordem das linhas
            linhas_invertidas = reversed(sorted(linhas, key=lambda x: int(x)))

            # Escreve as linhas invertidas no arquivo de saída
            saida.writelines(linhas_invertidas)

        print(f"Arquivo '{arquivo_saida}' criado com as linhas invertidas.")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_entrada}' não foi encontrado.")
    except Exception as e:
        print(f"Erro: {e}")

arquivo_pares = "pares.txt"
arquivo_saida_invertido = "pares_invertido.txt"

inverter_ordem_linhas(arquivo_pares, arquivo_saida_invertido)

##################################

# Processamento de um arquivo 

LARGURA=79
entrada=open("python\estudos\entrada.txt")
for linha in entrada.readlines():
    if linha[0]==";":
        continue
    elif linha[0]==">":
        print(linha[1:].rjust(LARGURA))
    elif linha[0]=="*":
        print(linha[1:].center(LARGURA))
    else:
        print(linha)
entrada.close 

''' Modifique o programa da listagem 9.6 para imprimir 40 vezes o símbolo de = se este for o primeiro caractere da linha. Adicione também a opção para parar de imprimir até que se pressione a tecla Enter cada vez que uma linha iniciar com . como primeiro caractere.'''

LARGURA = 79
entrada = open("python\estudos\entrada.txt")

for linha in entrada.readlines():
    if linha[0] == ";":
        continue
    elif linha[0] == ">":
        print(linha[1:].rjust(LARGURA))
    elif linha[0] == "*":
        print(linha[1:].center(LARGURA))
    elif linha[0] == "=":
        print("=" * 40)
    elif linha[0] == ".":
        input("Pressione Enter para continuar...")
    else:
        print(linha.strip())

entrada.close()

##################################

'''Crie um programa que leia um arquivo-texto e gere um arquivo de
saída paginado. Cada linha não deve conter mais de 76 caracteres. Cada página terá no máximo 60 linhas. Adicione na última linha de cada página o número da página atual e o nome do arquivo original.'''

def paginar_arquivo(entrada, saida):
    LARGURA_MAXIMA = 76
    LINHAS_POR_PAGINA = 60 

    with open(entrada, 'r') as arquivo_entrada, open(saida, 'w') as arquivo_saida:
        linhas = arquivo_entrada.readlines()
        total_linhas = len(linhas)
        num_paginas = 1 

        for i in range(0, total_linhas, LINHAS_POR_PAGINA):
            pagina = linhas[i:i + LINHAS_POR_PAGINA]

            for linha in pagina:
                # Garante que cada linha não tenha mais de 76 caracteres
                linha = linha.strip()[:LARGURA_MAXIMA]
                arquivo_saida.write(linha + '\n')

            # Adiciona a última linha da página com o número da página e o nome do arquivo 
            info_pagina = f"--- Página {num_pagina} - {entrada} ---\n"
            arquivo_saida.write(info_pagina)

            num_pagina +=1 

entrada = "python\estudos\entrada.txt"
saida = "python\estudos\entrada.txt"
paginar_arquivo(entrada, saida)

##################################

'''Modifique o programa anterior para também receber o número de
caracteres por linha e o número de páginas por folha pela linha de comando.'''

import sys

def paginar_arquivo(entrada, saida, largura_maxima, linhas_por_pagina):
    with open(entrada, 'r') as arquivo_entrada, open(saida, 'w') as arquivo_saida:
        linhas = arquivo_entrada.readlines()
        total_linhas = len(linhas)
        num_paginas = 1

        for i in range(0, total_linhas, linhas_por_pagina):
            pagina = linhas[i:i + linhas_por_pagina]

            for linha in pagina:
                # Garante que cada linha não tenha mais de 76 caracteres
                linha = linha.strip()[:largura_maxima]
                arquivo_saida.write(linha + '\n')
            
            info_pagina = f"--- Página {num_pagina} - {entrada} ---\n"
            arquivo_saida.write(info_pagina)

            num_pagina +=1

if len(sys.argv)!= 5:
    print("Por favor, forneça o nome do arquivo de entrada, o nome do arquivo de saída, o número de caracteres por linha e o número de páginas por folha pela linha de comando.")
else:
    arquivo_entrada = sys.argv[1]
    arquivo_saida = sys.argv[2]
    largura_maxima = int(sys.argv[3])
    linhas_por_pagina = int(sys.argv[4])
    paginar_arquivo(arquivo_entrada, arquivo_saida, largura_maxima, linhas_por_pagina)

# python nome_do_programa.py arquivo_entrada.txt arquivo_paginado.txt 76 60

##################################

def imprimir_nomes_arquivos(lista_arquivos):
    for arquivo in lista_arquivos:
        print(arquivo)

lista_arquivos = ["arquivo1.txt","arquivo2.txt", "arquivo3.txt"]
imprimir_nomes_arquivos(lista_arquivos)

##################################

def combinar_arquivos(lista_arquivos, arquivo_saida):
    try:
        with open(arquivo_saida, 'w') as saida:
            for arquivo in lista_arquivos:
                with open(arquivo, 'r') as entrada:
                    linhas = entrada.readlines()
                    saida.writelines(linhas)
        
        print(f"Arquivo '{arquivo_saida}' criado com sucesso.")
    except FileNotFoundError:
        print("Erro: Um dos arquivos não foi encontrado.")
    except Exception as e:
        print(f"Erro: {e}")

# Exemplo de uso 
lista_arquivos = ["python\estudos\\arquivo1.txt", "python\estudos\\arquivo2.txt", "python\estudos\\arquivo3.txt"]
arquivo_saida = "arquivo_combinado.txt"

combinar_arquivos(lista_arquivos, arquivo_saida)

##################################

'''Crie um programa que leia um arquivo e crie um dicionário onde
cada chave é uma palavra e cada valor é o número de ocorrências no arquivo.'''

def contar_ocorrencias_palavras(arquivo):
    try:
        with open(arquivo, 'r') as f:
            conteudo = f.read()

            # Remover caracteres especiais e quebrar o texto em palavras
            palavras = conteudo.lower().split()

            # Criar um dicionário para contar as ocorrências de cada palavra
            contagem_palavras = {}
            for palavra in palavras:
                palavra = palavra.strip('.,?!".;:')
                contagem_palavras[palavra] = contagem_palavras.get(palavra, 0)

        return contagem_palavras 
    
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
        return None 
    except Exception as e:
        print(f"Erro: {e}")
        return None 

nome_arquivo = "python\estudos\exemplo.txt"
resultado = contar_ocorrencias_palavras(nome_arquivo)

if resultado is not None:
    for palavra, ocorrencias in resultado.items():
        print(f"{palavra}: {ocorrencias} ocorrência(s)")

##################################

def contar_ocorrencias_palavras(arquivo):
    try:
        with open(arquivo, 'r') as f:
            conteudo = f.readlines()

            # Criar um dicionário para contar as ocorrências de cada palavra
            contagem_palavras = {}

            for linha_numero, linha in enumerate(conteudo, start=1):
                palavras = linha.lower().split()
                for coluna_numero, palavra_original in enumerate(palavras, start=1):
                    palavra = palavra_original.strip('.,?!".;:')
                    chave = (palavra, linha_numero, coluna_numero)

                    if chave in contagem_palavras:
                        contagem_palavras[chave][0] += 1
                    else:
                        contagem_palavras[chave] = [1]

            return contagem_palavras

    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
        return None
    except Exception as e:
        print(f"Erro: {e}")
        return None

nome_arquivo = "python\estudos\exemplo.txt"
resultado = contar_ocorrencias_palavras(nome_arquivo)

if resultado is not None:
    for chave, ocorrencias in resultado.items():
        palavra, linha, coluna = chave
        print(f"{palavra}: {ocorrencias[0]} ocorrência(s) na linha {linha}, coluna {coluna}")


'''
Neste exemplo, a chave do dicionário é uma tupla '(palavra, linha, coluna)', onde 'palavra' é a palavra encontrada, 'linha' é o número da linha e 'coluna' é o número da coluna. O valor associado a cada chave é uma lista que armazena o número de ocorrências da palavra. O exemplo de uso demostra como chamar a função com um arquivo de exemplo e imprimir o resultado, incluindo a linha e a coluna de cada ocorrência. Certifique-se de substituir '"exemplo.txt"' pelo nome real do seu arquivo.'''


########################################

'''Crie um programa que imprima as linhas de um arquivo. Esse programa deve receber três parâmetros pela linha de comando: o nome do arquivo, a linha inicial e a última linha a imprimir.'''

import sys 

def imprimir_linhas(arquivo, linha_inicial, ultima_linha):
    try:
        with open(arquivo, 'r') as f:
            linhas = f.readlines()

            # Garante que os números de linha estejam dentro dos limites do arquivo
            linha_inicial = max(1, min(linha_inicial, len(linha)))
            linha_final = max(linha_inicial, min(linha_final, len(linhas)))

            # Imprime as linhas no intervalo especificado 
            for i in range(linha_inicial - 1, linha_final):
                print(linhas[i].strip())

    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Erro: {e}")

if len(sys.argv)!= 4:
    print("Por favor, forneça o nome do arquivo, a linha inicial e a última linha a imprimir.")
else:
    nome_arquivo = sys.argv[1]
    linha_inicial = int(sys.argv[2])
    linha_final = int(sys.argv[3])

    imprimir_linhas(nome_arquivo, linha_inicial, linha_final)

# Para executar, utilize o seguinte comando:

# python nome_do_programa.py nome_do_arquivo.txt linha_inicial linha_final

########################################

'''Crie um programa que leia um arquivo-texto e elimine os espaços repetidos entre as palavras e no fim das linhas. O arquivo de saída também não deve ter mais de uma linha em branco repetida.'''

'''import sys

if len(sys.argv) != 3:
    print("\nUso: e09-14.py entrada saida\n\n\n")
    sys.exit(1)

entrada = sys.argv[1]
saida = sys.argv[2]

arquivo = open(entrada, "r", encoding="utf-8")
arq_saida = open(saida, "w", encoding="utf-8")
branco = 0 

for linha in arquivo:
    # Elimina espaços à direita
    # Substitua por strip se também
    # quiser eliminar espaços à esquerda
    linha = linha.rstrip()
    linha = linha.replace("  ", "") #elimina espaços repetidos
    if linha == "":
        branco += 1 # Conta linhas em branco
    else:
        branco = 0 
    if branco < 2:
        arq_saida.write(linha+"\n")

arquivo.close
arq_saida.close()'''

###########################################

'''Altere o programa da listagem 7.5, o jogo da forca. Utilize um arquivo em que uma palavra seja gravada a cada linha. Use um editor de textos para gerar o arquivo. Ao iniciar o programa, utilize esse arquivo para carregar a lista de palavras. Experimente também perguntar o nome do jogador e gerar um arquivo com o número de acertos dos cinco melhores.'''

############################################

# Controle de uma agenda de telefones

'''agenda = [] 

def pede_nome():
    return input("Nome: ")

def pede_telefone():
    return input("Telefone: ")

def mostra_dados(nome, telefone):
    print("Nome: %s Telefone: %s" % (nome, telefone))

def pede_nome_arquivo():
    return input("Nome do arquivo: ")

def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None 

def novo():
    global agenda 
    nome = pede_nome()
    telefone = pede_telefone()
    agenda.append([nome, telefone])

def apaga():
    global agenda 
    nome = pede_nome()
    p = pesquisa(nome)
    if p is not None:
        del agenda[p]
    else:
        print("Nome não encontrado.")

def altera():
    p = pesquisa(pede_nome())
    if p is not None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        print("Encontrado:")
        mostra_dados(nome, telefone)
        nome = pede_nome()
        telefone = pede_telefone()
        agenda[p] = [nome, telefone]
    else:
        print("Nome não encontrado.")

def lista():
    print("\nAgenda\n\n-------")
    for e in agenda:
        mostra_dados(e[0], e[1])
    print("-------\n")

def lê():
    global agenda
    nome_arquivo = pede_nome_arquivo()
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            agenda = [] 
            for l in arquivo.readlines():
                nome, telefone = l.strip().split("#")
                agenda.append([nome, telefone])
        print("\nAgenda carregada do arquivo {}.".format(nome_arquivo))
    except FileNotFoundError:
        print("Arquivo não encontrado:", nome_arquivo)
    except Exception as e:
        print("Ocorreu um erro ao ler o arquivo:", e)

def grava():
    nome_arquivo = pede_nome_arquivo()
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            for e in agenda:
                arquivo.write("%s#%s\n" % (e[0], e[1]))
        print("\nAgenda gravada no arquivo {}.".format(nome_arquivo))
    except Exception as e:
        print("Ocorreu um erro ao gravar o arquivo:", e)

def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print("Valor inválido, favor digitar entre %d e %d" % (inicio, fim))

def menu():
    print("""
    1 - Novo 
    2 - Altera
    3 - Apaga
    4 - Lista 
    5 - Grava
    6 - Lê

    0 - Sai
    """)
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 6)

while True:
    opção = menu()
    if opção == 0:
        break
    elif opção == 1:
        novo()
    elif opção == 2:
        altera()
    elif opção == 3:
        apaga()
    elif opção == 4:
        lista()
    elif opção == 5:
        grava()
    elif opção == 6:
        lê()'''

#### por alguma razão o programa não está lendo o arquivo gerado... 

############################################


'''Altere o Programa 7.2, o jogo da forca. Utilize um arquivo em que uma palavra seja gravada a cada linha. Use um editor de textos para gerar o arquivo. Ao iniciar o programa, utilize esse arquivo para carregar (ler) a lista de palavras. Experimente também perguntar o nome do jogador e gerar um arquivo com o número de acertos dos cinco melhores.'''


palavras = []
placar = {} 


def carrega_palavras():
    arquivo = open("python\estudos\palavras.txt", "r", encoding="utf-8")
    for palavra in arquivo.readlines():
        palavra = palavra.strip().lower()
        if palavra != "":
            palavras.append(palavra)
    arquivo.close()


def carrega_placar():
    arquivo = open("python\estudos\placar.txt", "r", encoding="utf-8")
    for linha in arquivo.readlines():
        linha = linha.strip()
        if linha != "":
            usuario, contador = linha.split(";")
            placar[usuario] = int(contador)
    arquivo.close()


def salva_placar():
    arquivo = open("placar.txt", "w", encoding="utf=8")
    for usuario in placar.keys():
        arquivo.write("{usuario};{placar[usuario]\n}")
    arquivo.close()


def atualize_placar(nome):
    if nome in placar:
        placar[nome] += 1
    else:
        placar[nome] = 1
    salva_placar()


def exibe_placar():
    placar_ordenado = [] 
    for usuario, score in placar.items():
        placar_ordenado.append([usuario, score])
    placar_ordenado.sort(key=lambda score: score[1])
    print("\nMelhores jogadores por número de acertos:")
    placar_ordenado.reverse()
    for up in placar_ordenado:
        print(f"{up[0]:30s} {up[1]:10d}")


carrega_palavras()
carrega_placar()

import random

palavra = palavras[random.randint(0, len(palavras) -1)]

digitadas = [] 
acertos = [] 
erros = 0 
while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)
    if senha == palavra:
        print("Você acertou!")
        nome = input("Digite seu nome: ")
        atualize_placar(nome)
        break 
    tentativa = input("\nDigite uma letra:").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue 
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
    print("X==:==\nX  :  ")
    print("X  O  " if erros >= 1 else "X")
    linha2 = ""
    if erros == 2:
        linha2 = "  |  "
    elif erros == 3:
        linha2 = "  \|  "
    elif erros == 4:
        linha2 = "  \|/  "
    print(f"X{linha2}")
    linha3 = ""
    if erros == 5:
        linha3 += r" /  "
    elif erros == 6:
        linha3 += r" / \ "
    print(f"X{linha3}")
    print("X\n============")
    if erros == 6:
        print("Enforcado!")
        break 

exibe_placar()

###############################


    














