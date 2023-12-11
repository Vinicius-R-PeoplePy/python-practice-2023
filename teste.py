from cliente import Cliente
from contas import Conta, ContaEspecial #1
joão=Cliente("João da Silva", "777-1234")
maria=Cliente("Maria da Silva", "777-4321")
conta1=Conta([joão], 1, 1000)
conta2=ContaEspecial([maria, joão], 2, 500, 1000) #2
conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
conta2.saque(1500)
conta1.extrato()
conta2.extrato()
'''
Em #1 adicionamos o nome da classe ContaEspecial ao import. Dessa forma, poderemos utilizar a nova classe em nossos testes. Já em #2 criamos um objeto ContaEspecial. Veja que, praticamente, não mudamos nada, exceto o nome da classe, que agora é ContaEspecial, e não Conta. Um detalhe importante para o teste é que adicionamos um parâmetro ao construtor, no caso 1000, como o valor de limite. Execute esse programa de teste e observe que, para a conta 2, obtivemos um saldo negativo.

Utilizando herança, modificamos muito pouco nosso programa, mantendo a funcionalidade anterior e adicionando novos recursos. O interessante de tudo isso é que foi possível reutilizar os métodos que já havíamos definido na classe Conta. Isso permitiu que a definição da classe ContaEspecial fosse bem menor, pois lá especificamos apenas o comportamento que é diferente.

Quando você utilizar herança, tente criar classes nas quais o comportamento e características comuns fiquem na superclasse. Dessa forma, você poderá definir subclasses enxutas. Outra vantagem de utilizar herança é que, se mudarmos algo na superclasse, essas mudanças serão também usadas pelas subclasses. Um exemplo seria nmodificarmos o método do extrato, ao modificarmos o método Conta.extrato, estaremos também modificando o extrato de ContaEspecial, pois as duas classes compartilham o mesmo método. 

É importante notar que, ao utilizarmos herança, as subclasses devem poder substituir suas superclasses, sem perda de funcionalidade e sem gerar erros nos programas. O importante é que você conheça esse novo recurso e comece a utilizá-lo nos programas. Lembre-se de que você não é obrigado a definir uma hierarquia de classes em todos os seus programas. Com o tempo, a necessidade de utilizar herança ficará mais clara. 
'''