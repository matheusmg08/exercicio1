"""
Faça um programa que gere números inteiros aleatórios entre 1 e 10 e calcule a soma desses números, até que seja gerado um número que foi informado pelo usuário anteriormente.
---Dica 1: antes de mais nada , peça para o usuário digitar um número entre 1 e 10 e guarde o valor em num
----Dica 2: use a função randint(inicio,fim) do módulo random para gerar um número aleatório entre 1 e 10
"""
import random #biblioteca útil para trabalhar com valores aleatórios
soma = 0 #inicializar a variável soma
print ("="*30)
num_sorte=int(input('Digite o número da sorte: '))
while num_sorte < 1 or num_sorte > 10:
    print('Número inválido , digite um valor entre 1 e 10! ')
    num_sorte=int(input('Digite o número da sorte'))
print("="*30)

sorteado = random.randint(1,10)
while sorteado != num_sorte:
    soma = soma + sorteado
    print(f'soma parcial = {soma}, sorteado {sorteado}')
    sorteado = random.randint(1,10)
print(f'A soma final foi de {soma}')