from time import sleep
print('-' * 7, 'Invertendo Strings', '-' * 7)
print('-' * 35)
txt = 'Target Sistemas'
print(f'Vou inverter o texto "Target Sistemas"...')
sleep(0.5)
print(f'{txt[::-1]}')
sleep(0.5)
print('Legal né? Agora é sua vez...')
print('-' * 35)
sleep(0.5)
user = str(input('Digite uma frase para ser invertida: '))
print('Estou invertendo sua frase...Por favor aguarde!')
print('-' * 35)
sleep(1)
print(f'{user[::-1]}')
print('Espero ter ajudado...Volte Sempre!')