print('*'*40)

class Banco:
    def __init__(self, nome):
        self.nome = nome 
        self.clientes = [] 
        self.contas = [] 
    def abre_contas(self, conta):
        self.contas.append(conta)
    def lista_contas(self):
        for c in self.contas:
            c.resumo()

from cliente import Cliente
from bancos import Banco 
from contas import Conta 
joão = Cliente("João da Siva", "3241-5599")
maria = Cliente("Maria Silva", "7231-9955")
josé = Cliente("José Vargas", "9721-3040")
contaJM = Conta( [joão, maria], 100)
contaJ = Conta( [josé], 10)
tatu = Banco("Tatú")
tatu.abre_contas(contaJM)
tatu.abre_contas(contaJ)
tatu.lista_contas()



