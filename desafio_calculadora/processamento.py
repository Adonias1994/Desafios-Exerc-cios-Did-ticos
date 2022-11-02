# Processamento de Back End
v1 = int(input('\nValor 1: '))
o = input('Escolha uma operação matemática (+, -, *, /, p para potência): ')
v2 = int(input('Valor 2: '))
if o == '+':
    print('O resultado é:', v1 + v2, '\n')
elif o == '-':
    print('O resultado é:', v1 - v2, '\n')
elif o == '*':
    print('O resultado é:', v1 * v2, '\n')
elif o == '/':
    print('O resultado é:', v1 // v2, '\n')
elif o == 'p':
    print('O resultado é:', v1 ** v2, '\n')
else:
    print('Você digitou um valor inválido.\n')