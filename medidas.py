#!/usr/bin/env python

#lista = [1, 2, 1, -5, -141, 33]
def menor_numero(lista_de_numeros):
  menor = lista_de_numeros[0]
  for numero in lista_de_numeros:
    if numero < menor:
      menor = numero
  return menor

print menor_numero(lista)
