'''
A classe Conta é definida recebendo clientes, número e saldo em seu construtor (__init__), onde em clientes esperamos uma lista de objetos da classe Cliente, número é uma string com o número da conta, e saldo é um parâmetro opcional, tendo zero (0) como padrão. A listagem também apresenta os métodos resumo, saque e depósito. O método resumo exibe na tela o número da conta corrente e seu saldo; saque permite retirar dinheiro da conta corrente, verificando se essa operação é possível (self.saldo >= valor); depósito simplesmente adiciona o valor solicitado ao saldo da conta corrente.
'''

'''class Conta:
    def __init__(self, clientes, número, saldp = 0):
        self.saldo = saldo 
        self.clientes = clientes 
        self.número = número 
    def resumo(self):
        print("CC Número: %s Saldo: %10.2f" % (self.número, self.saldo))
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor 
    def deposito(self, valor):
        self.sado += valor 

print(conta.resumo())
print(conta.saque(1000))
print(conta.resumo())
print(conta.saque(50))
print(conta.resumo())
print(conta.depósito(200))
print(conta.resumo())'''

####################################

# Conta com registro de operações e extrato

print('*'*40)


class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.saldo = 0 
        self.clientes = clientes 
        self.numero = numero 
        self.operacoes = []  # Corrected the attribute name
        self.deposito(saldo)

    def resumo(self):
        print(f"CC N° {self.numero} Saldo: {self.saldo:10.2f}")

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor 
            self.operacoes.append(["SAQUE", valor])
        else:
            print("Saldo insuficiente!")

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["DEPÓSITO", valor])

    def extrato(self):
        print(f"Extrato CC N° {self.numero}\n")
        for o in self.operacoes:
            print(f"{o[0]:10s} {o[1]:10.2f}")
        print(f"\n      Saldo: {self.saldo:10.2f}\n")


class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo=0, limite=0):
        Conta.__init__(self, clientes, numero, saldo)
        self.limite = limite 

    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor 
            self.operacoes.append(["SAQUE", valor])
        else:
            Conta.saque(self, valor)

# Testando Cliente e Contas

from cliente import Cliente 
from contas import Conta 

joao = Cliente("João da Silva", "777-1234")
maria = Cliente("Maria da Silva", "555-4321")

conta1 = Conta([joao], 1, 1000)
conta2 = Conta([maria, joao], 2, 500)
conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
conta2.saque(250)
conta1.extrato()
conta2.extrato()

#######################

'''Altere o programa de forma que a mensagem saldo insuficiente
seja exibida caso haja tentativa de sacar mais dinheiro
que o saldo disponível.'''


print('*'*40)


class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.saldo = 0 
        self.clientes = clientes 
        self.numero = numero 
        self.operacoes = [] 
        self.deposito(saldo)

    def resumo(self):
        print(f"CC N° {self.numero} Saldo: {self.saldo:10.2f}")

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor 
            self.operacoes.append(["SAQUE", valor])
        else:
            print("Saldo insuficiente!")

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["DEPÓSITO", valor])

    def extrato(self):
        print("Extrato CC N° {}\n".format(self.numero))
        for o in self.operacoes:
            print(f"{o[0]:10s} {o[1]:10.2f}")
        print("\n       Saldo: {:10.2f}\n".format(self.saldo))


class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo=0, limite=0):
        Conta.__init__(self, clientes, numero, saldo)
        self.limite = limite 

    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor 
            self.operacoes.append(["SAQUE", valor])
        else:
            Conta.saque(self, valor)


##################

print('*'*40)


class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome 
        self.telefone = telefone 

class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.saldo = 0 
        self.clientes = clientes 
        self.numero = numero 
        self.operacoes = [] 
        self.deposito(saldo)

    def resumo(self):
        print(f"CC N° {self.numero} Saldo: {self.saldo:10.2f}\n")
        for cliente in self.clientes:
            print(f"Nome: {cliente.nome}\nTelefone: {cliente.telefone}\n")

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor 
            self.operacoes.append(["SAQUE", valor])
        else:
            print("Saldo insuficiente!")

    def deposito(self, valor):
        self.saldo += valor 
        self.operacoes.append(["DEPÓSITO", valor])

    def extrato(self):
        print(f"Extrato CC N° {self.numero}\n")
        for o in self.operacoes:
            print(f"{o[0]:10s} {o[1]:10.2f}")
        print(f"\n      Saldo: {self.saldo:10.2f}\n")


maria = Cliente("Maria", "1234-3321")
joão = Cliente("João", "5554-3322")

conta = Conta([maria, joão], 1234, 5000)
conta.resumo() 


'''Crie uma nova conta, agora tendo João e José como clientes e saldo igual a 500'''


print('*'*40)

class CLiente:
    def __init__(self, nome, telefone):
        self.nome = nome 
        self.telefone = telefone 

class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.saldo = 0 
        self.clientes = clientes 
        self.numero = numero 
        self.operacoes = [] 
        self.deposito(saldo)

    def resumo(self):
        print(f"CC N° {self.numero} Saldo: {self.saldo:10.2f}\n")
        for cliente in self.clientes:
            print(f"Nome: {cliente.nome}\nTelefone: {cliente.telefone}\n")

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor 
            self.operacoes.append(["SAQUE", valor])
        else:
            print("Saldo insuficiente!")

    def deposito(self, valor):
        self.saldo += valor 
        self.operacoes.append(["DEPÓSITO", valor])
    
    def extrato(self):
        print(f"Extrato CC N° {self.numero}\n")
        for o in self.operacoes:
            print(f"{o[0]:10s} {o[1]:10.2f}")

joão = Cliente("João", "5554-3322")
josé = Cliente("José", "1243-3321")

conta = Conta([joão, josé], 2341, 500)
conta.resumo()