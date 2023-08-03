Mudança = ['coisas', 'mais coisas', 'caixotes', 'mais e mais coisas', 'cansaço do escambau'] 
Mudança_feita = False 
Trabalho = input("A mudança foi feita? [s/n]")
if Mudança_feita == False:
	for coisas in Mudança:
		print(f'Mudança está em andamento…')	
Trabalho = input("A mudança foi feita? [s/n]")
if Trabalho in 'SIMsimSs':
    Mudança_feita == True
    print("Descansar…")
if Trabalho in 'NAONÃOnaonãonn':
	Mudança_feita = False 
	Trabalho = input("A mudança foi feita? [s/n]")
	
	
    