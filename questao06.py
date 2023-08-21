'''
6) Desenvolver um programa que leia um número n qualquer menor ou igual a 50 e apresente o valor obtido da
multiplicação sucessiva de n por 3 enquanto o produto for menor que 250. (n x 3; n x 3 x 3; n x 3 x 3 x 3 etc...).
'''

n = int(input("Insira um número menor ou igual a 50: "))

if ( n <= 50):
    pass
while (n <= 250):
    print(n * 3)
    n = n * 3

else:
    print("O número inserido não é menor ou igual a 50")