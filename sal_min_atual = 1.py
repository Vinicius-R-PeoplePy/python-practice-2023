sal_min_atual = 1.320 
sal_mensal = float(input("Digite o valor do seu salário: "))

múltiplos = sal_mensal // sal_min_atual 

if múltiplos == 0:
    print('SEU SALÁRIO MENSAL É MENOR QUE 1 SALÁRIO MÍNIMO')
elif múltiplos == 1:
    print('SEU SALÁRIO MENSAL EQUIVALE A 1 SALŔIO MÍNIMO')
elif múltiplos == 2:
    print('SEU SALÁRIO MENSAL EQUIVALE A 2 SALÁRIOS MÍNIMOS')
elif múltiplos == 3:
    print('SEU SALÁRIO MENSAL EQUIVALE A 3 SALÁRIOS MÍNIMOS')
elif múltiplos == 4:
    print('SEU SALÁRIO MENSAL EQUIVALE A 4 SALÁRIOS MÍNIMOS')
elif múltiplos == 5:
    print('SEU SALÁRIO MENSAL EQUIVALE A 5 SALÁRIOS MÍNIMOS')
else:
    print('SEU SALÁRIO MENSAL É MAIOR QUE 5 SALÁRIOS MÍNIMOS!')

'''Este código divide o salário mensal pelo salário mínimo atual
usando o operador // e verifica em qual intervalo de múltiplos
o resultado se encontra. Se o resultado for 0, o salário mensal
é menor que um salário mínimo. Se for 1, o salário mensal é igual
a um salário mínimo. E assim por diante, até verificar se o resultado
é maior que 5, indicando que o salário mensal é maior que
cinco salários mínimos.'''