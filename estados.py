class Estado:
    def __init__(self, nome, sigla):
        self.nome = nome 
        self.sigla = sigla 
        self.cidades = [] 

    def adiciona_cidade(self, cidade):
        cidade.estado = self 
        self.cidades.append(cidade)

    def populacao(self):
        return sum([c.populacao for c in self.cidades])
    
class Cidade:
    def __init__(self, nome, populacao):
        self.nome = nome 
        self.populacao = populacao 
        self.estado = None 

    def __str__(self):
        return f"Cidade (nome={self.nome}, populacao={self.populacao}, estado={self.estado})"
    
am = Estado("Amazonas", "AM")
am.adiciona_cidade(Cidade("Manaus", 1861838))
am.adiciona_cidade(Cidade("Parintins", 103828))
am.adiciona_cidade(Cidade("Itacoatiara", 89064))

sp = Estado("São Paulo", "SP")
sp.adiciona_cidade(Cidade("Guarulhos", 1244518))
sp.adiciona_cidade(Cidade("Campinas", 1098630))

rj = Estado("Rio de Janeiro", "RJ")
rj.adiciona_cidade(Cidade("Rio de Janeiro", 6390290))
rj.adiciona_cidade(Cidade("São Gonçalo", 1016128))
rj.adiciona_cidade(Cidade("Duque de Caxias", 867067))


for estado in [am, sp, rj]:
    print(f"Estado: {estado.nome} Sigla: {estado.sigla}")
    for cidade in estado.cidades:
        print(f"Cidade: {cidade.nome} População: {cidade.populacao}")
    print(f"População do Estado: {estado.populacao()}\n")