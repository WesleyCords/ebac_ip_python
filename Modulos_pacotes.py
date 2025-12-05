## IMPORT
import random, math

num = round(random.random(), 2)
print(num)

potencia = math.pow(num, 2)
print(potencia)

## FROM - IMPORT
from time import sleep

for i in range(4):
	sleep(1)
	print(i + 1)

## FROM - IMPORT - AS
from datetime import datetime as dt
print(dt.today())

## Import de modulos proprios
from POO import *

objeto = ArquivoCSV()
