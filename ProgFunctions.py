from functools import reduce
from random import random

def retorno(juros: float):
	return lambda investimento: (
		investimento * (1 + juros)
	)

def calcula_investimento(anos: int, valor: float, qtt_juros: float):
	valor_final = valor
	juros = retorno(qtt_juros)
	for ano in range(1, anos + 1):
		valor_final = juros(valor_final)
	valor_final = round(valor_final, 2)
	print(valor_final)

calcula_investimento(10, 1000, 0.05)
calcula_investimento(6, 4000, 0.07)
calcula_investimento(20, 500, 0.11)

impares = [1, 3, 5, 7]

def maior_entre(primeiro: int, ultimo: int):
	return primeiro if primeiro >= ultimo else ultimo

soma = reduce(lambda x, y: x + y, impares)
print(soma)
pares = [2, 4, 6, 8]

numero_ao_cubo = map(lambda p, i: p - i, pares, impares)
numeros = []
for num in numero_ao_cubo:
	numeros.append(num)
print(numeros)

numeros = list(range(5))
primos = filter(lambda n: (n % n == 0 if n != 0 else False) & (n / 1 == n), numeros)
for primo in primos:
	print(primo)

nume = [round(100 * random()) for _ in range(5)]
maior_numero = reduce(lambda primeiro, segundo: primeiro if primeiro >= segundo else segundo, nume)
print(maior_numero)

numeros = [2,3,4,5, 11]
quadrado_diferencas = reduce(lambda a, b: a**2 - 2 *a *b + b**2, numeros)
print(quadrado_diferencas)

ab = [2,4,6,8]
sub = 1
ba = list(map(lambda x: x - sub, ab))
print(ba)
## Desafio para amanhã