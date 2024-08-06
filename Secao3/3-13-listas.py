"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Método úteis: appendd, insert, pop, del, clear, extend, + 

Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)