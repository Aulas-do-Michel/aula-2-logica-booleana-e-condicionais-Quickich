"""
#### Exercício 1

Receba um número inteiro de um usuário. Se ele for par, imprima "Par". Se não, imprima "Ímpar".

Exemplo:

Digite um número:
10

Par
--------
Digite um número:
1

Ímpar

Dica: Lembre do comando de resto da divisão inteira!
"""


numero = float(input("Digite um número:"))

if numero / 2 % 0:
  print("O número é par")
else:
  print("O número é ímpar")
  
