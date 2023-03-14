print('-' * 40)
print('-' * 5, 'Pergunta 2 / Questão 2', '-' * 5)
Termo1 = 0
Termo2 = 1
Termo3 = 0
print('-' * 40)
print(' ' * 3, 'Consulta da Sequência de Fibonacci')
print('-' * 40)
Valor = int(input('Digite um número: '))
print(f'{Termo1} {Termo2} ', end='')
while Valor > Termo3:
    Termo3 = Termo1 + Termo2
    Termo1 = Termo2
    Termo2 = Termo3
    print(f' {Termo3} ', end='')
print()
if Valor == 0 or Valor == 1:
    print('O número faz parte da sequência de Fibonacci.')
elif Valor == Termo3:
    print('O número faz parte da sequência de Fibonacci.')
else:
    print('O número digitado não faz parte da sequência de Fibonacci.')