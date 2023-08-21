'''
8) Desenvolver um programa que apresente todos os valores numéricos inteiros ímpares situados na faixa de 0 a
20. Para saber se o número é ímpar, será necessário verificar essa condição com o comando if. Sendo ímpar,
mostre-o; não sendo, passe para o próximo passo
'''

num = 0
resto = num % 2

while (num <= 20):
    num = num + 1
    if (num % 2 == 0):
        print(f"{num} é um número par")
    else:
        pass
