import os
os.system('cls')

# Entrada

p = int(input('\nInforme o seu peso...: ')) # p = peso
a = float(input('Informe a sua altura.: ')) # a = altura

# Processamento

i = p / (a*a) # i = imc
i = round(i, 2) # limita o número de casas decimais após a vírgula

# Saida

if(i < 16):
    print('Seu IMC é ' + str(i) + ' e você está abaixo do peso.\n')
elif(i < 25):
    print('Seu IMC é ' + str(i) + ' e você está com o peso ideal.\n')
elif(i < 30):
    print('Seu IMC é ' + str(i) + ' e você está acima do peso.\n')
elif(i < 35):
    print('Seu IMC é ' + str(i) + ' e você está com obesidade grau 1.\n')
elif(i < 40):
    print('Seu IMC é ' + str(i) + ' e você está com obesidade grau 2.\n')
else:
    print('Seu IMC é ' + i + ' e você está com obesidade grau 3.\n')
