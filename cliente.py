class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome 
        self.telefone = telefone

joão=Cliente("João da Silva", "777-1234")
maria=Cliente("Maria Silva", "555-4321")
print(joão.nome)
print(joão.telefone)
print(maria.nome)
print(maria.telefone)

