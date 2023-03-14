import json
from time import sleep

with open("dados.json") as meu_json:
    dados = json.load(meu_json)


print('-' * 7, 'Faturamento Diário', '-' * 7)
print('-' * 35)
cont = maior = menor = media = total = 0

for dia in dados:
    valor = dia['valor']
    if valor > 0:
        if valor > maior:
            maior = valor
        if valor < menor or menor == 0:
            menor = valor
        total += valor
        cont += 1

media_mensal = total / cont if cont > 0 else 0
acima_media = 0

for dia in dados:
    valor = dia['valor']
    if valor > media_mensal:
        acima_media += 1

print('Analisando os dados...Por favor aguarde.')
sleep(1)
print(f'O maior valor de faturamento: {maior}')
sleep(1)
print(f'O menor valor de faturamento: {menor}')
sleep(1)
print(f'O número de dias com faturamento acima da média: {acima_media}')