# ESTUDOS DIVERSOS - PROGRAMAÇÃO 



# Aula 019 mundo 3 
#093 Crie um programa que gerencie o aproveitamento de um jogador de futebol
# O programa vai ler o nome do jogador e quantas partidas jogou. Depois
# vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
# será guardado em um dicionário, incluindo o total de gols feitos durante
# o campeonato. 



jogador = dict()
partidas = list()
jogador('nome') = str(input('Nome do Jogador: '))
tot = int(('Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(f'  Quantos gols na partida {c}? '))
jogador("gols") = partidas[:]
jogador["total"] = sum(partidas)
print(jogador)
print(partidas)
for k, v in jogador.items():
    print(f'O campo{k} tem o valor {v}')
print('<=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols')


'''
format()
=> formats the given string into a nicer output in Python. 

lower()
=> returns a string with all uppercase characters 
converted to lowercase characthers 

upper()
=> returns a string with all lowercase characters converted
to uppercase.

join()
=> returns a string concatenated with th elements of an iterable

split()
=> breaks the string mat the separator and returns a list of strings.

find()
=> returnsthe index of the first ocurrence of the substring (if found)

replace()
=> returns a copy of the string where all occurrences of a substring
are replaced with another substring. 
'''

'''

ESCAPE SEQUENCES

Some of the commonly used:

* \\ - backslash 
* \n - line feed (moving one line forward)
* \' - single quote 
* \" - double quote
* \t - horizontal tab 
* \v vertical tab

print("hello world!\veeeee\vooooo")'''

''' 
SETS 

my_set = {1, 2, 1, 3, 1, 2, 3}
print(my_set)       #Output: {1, 2, 3}

# passing a list to the set() function to create a set:

my_set = set([1, 4, 1])
print(my_set) # Output: {1, 4}

We can add a single element using nthe add() method
and multiple elements using the update()
method. The update() method can take tuples,
lists, strings or other sets as its argument.

my_set = {1, 3}
print(my_set) # Output: {1, 3}

my_set.add(2)
print(my_set) # Output : {1, 2, 3}

my_set.update([4, 5, 6])
print(my_set) # Output: {1, 2, 3, 4, 5, 6}

REMOVING ELEMENTS FROM A SET

To remove elements from a set, we can either use
remove() or discard() method.

The only difference between the two is that,
while using discard(), if the item does not exist in the set,
it remains unchanged. But remove() will raise an error
in such conditions. 
'''

'''my_set = {1, 3, 4, 6, 6}

my_set.discard(4)
print(my_set)       # Output: {1, 3, 5, 6}

my_set.remove(6)
print(my_set)       # Output: {1, 3, 5}

#trying to remove 2 which doesn't exist:
my_set.discard(2)
print(my_set)       # Output: {1, 3, 5}

my_set.remove(2)    # Error

pop() and clear() methods

The pop() method removes a random element from 
a set and returns it.

print(my_set)   # Output: {'c', 'a'}
print(returned_value)   # Output: 'b'

my_set = {1, 2, 3}

my_set.clear()      # empty set
print(my_set)       # Output: set() '''

'''
SET UNION

The union of two sets A and B is a set of all 
elements from both sets.

It is performed using | operator. Some can be accomplished 
using the union() method.

A = {1, 2, 3}
B = {2, 3, 4, 5}

result = A | B 
print(result)       # {1, 2, 3, 4, 5}

result = B.union(A)
print(result)       # {1, 2, 3, 4, 5}

'''

'''
SET INTERSECTION

The intersection of two sets A and B is a set of all 
elements that are common in both sets.

It is performed using & operator. Some can 
be accomplished using the method intersection().

A = {1, 2, 3}
B = {2, 3, 4, 5}

result = A & B 
print(result)       # {2, 3}

result = B.intersection(A)
print(result)       # {2, 3}

SET DIFFERENCE

The difference of set B from A is a set of
elements that are only in A but not in B. 

It is performed by A - B. Same can be
accomplished using the difference() method.

A = {1, 2, 3}
B = {2, 3, 4, 5}

result = A - B 
print(result)       # Output: {1}

result = A.difference(B)
print(result)       # Output: {1}

result = B - A 
print(result)       # Output: {4, 5}

SET SYMMETRIC DIFFERENCE

The symmetric difference of two sets A 
and B of elements in both A and B except
those that are common in both. 

It is performed by ^ operator. Same can be
accomplished using the symmetric_difference() method.

A = {1, 2, 3}
B = {2, 3, 4, 5}

result = A ^ B  
print(result)       # Output: {1, 4, 5}

result = symmetric_difference(B)
print(result)       # Output: {1, 4, 5}

PYTHON SET METHODS:

add() - to add a single element to a set
update() - to add multiple elements to a set
remove() - to remove an element from a set 
discard() - to remove an element from a set
pop() - to remove and return an arbitrary element from a set
clear() - to remove all elements from a set 
union() - returns union of two sets
intersection() - returns intersection of two sets 
difference() - returns difference of two sets
symmetric_difference() - returns symmetric difference of two sets'''



'''




