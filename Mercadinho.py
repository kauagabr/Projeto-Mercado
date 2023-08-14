def linboni(cont):
    print('-=' * cont)


def linigl(cont):
    print('=' * cont)


def traço(cont):
    print("-" * cont)


from time import sleep

produto = {
    'alimentos': {
        "Arroz R$ 5,45": 1,
        'Feijão R$ 7,50': 2,
        'Macarrão R$ 3,54': 3,
        'Óleo R$ 9.00': 4,
        'Azeite R$ 32.00': 5,
        'Tempero Pronto R$ 3,50': 6,
        'Maionese R$ 4,50': 7,
        'Molho R$ 2,59': 8,
        'Enlatados R$ 5,10': 9,
        'Atum R$ 8,55': 10,
        'Milho R$ 3,45': 11,
        'Ervilha R$ 2,50': 12,
        'Farinhas R$ 3,55': 13,
        'Café R$ 6,00': 14,
        'Chá R$ 1,25': 15,
        'Leite R$ 8,00': 16,
        'Batata frita R$ 16,00': 17,
        'Pão de queijo R$ 5,00': 18,
        'Pratos prontos R$ 19,00': 19,
        'Lasanha R$ 15,00': 20,
        'Manteiga R$ 8,50': 21,
        'Margarina R$ 4,45': 22,
        'Requeijão R$ 7,30': 23,
        'Queijo R$ 25,50': 24,
        'Presunto R$ 18,00': 25,
        'Mortadela R$ 11,50': 26,
        'Água R$ 1,75': 27,
        'Iogurtes R$ 8,75': 28,
        'Suco R$ 9,99': 29,
        'Refrigerante R$ 6,25': 30,
        'Carne de cabrita R$ 45,00': 31,

    },
    'alimentos1': {
        "Arroz": 1,
        'Feijão': 2,
        'Macarrão': 3,
        'Óleo': 4,
        'Azeite': 5,
        'Tempero': 6,
        'Maionese': 7,
        'Molho': 8,
        'Enlatados': 9,
        'Atum': 10,
        'Milho': 11,
        'Ervilha': 12,
        'Farinhas': 13,
        'Café': 14,
        'Chá': 15,
        'Leite': 16,
        'Batata frita': 17,
        'Pão de queijo': 18,
        'Pratos prontos': 19,
        'Lasanha': 20,
        'Manteiga': 21,
        'Margarina': 22,
        'Requeijão': 23,
        'Queijo': 24,
        'Presunto': 25,
        'Mortadela': 26,
        'Água': 27,
        'Iogurtes': 28,
        'Suco': 29,
        'Refrigerante': 30,
        'Carne de cabrita': 31,

    },
    'valor1': {
        5.45: 1,
        7.50: 2,
        3.54: 3,
        9.00: 4,
        32.00: 5,
        3.50: 6,
        4.50: 7,
        2.59: 8,
        5.10: 9,
        8.55: 10,
        3.45: 11,
        2.50: 12,
        3.55: 13,
        6.00: 14,
        1.25: 15,
        8.00: 16,
        16.00: 17,
        5.00: 18,
        19.00: 19,
        15.00: 20,
        8.50: 21,
        4.45: 22,
        7.30: 23,
        25.50: 24,
        18.00: 25,
        11.50: 26,
        1.75: 27,
        8.75: 28,
        9.99: 29,
        6.25: 30,
        45.00: 31,
    },

}

green = "\033[1;42m"
negr_subli = "\033[1;4m"
negrito = "\033[1m"
final = "\033[m"
red = "\033[1;31m"

linigl(60)
print(f'{green}{"MERCADINHO DO IFPE LTDA":-^60}{final}')
linigl(60)
print(negr_subli, 'Rua Capitão Pedro Ivo, 507, Centro, Palmares - PE', final)
print(negr_subli, 'CNPJ:99.999.999/0001-01', final)
print(negr_subli, 'IE: 999.999.999', final)
print(negr_subli, 'IM: 99.999.999', final)
traço(60)
print(F'{green}{"ALIMENTOS":-^60}{final}')
traço(60)
cont = maior = menor = soma = 0
pma = pme = ""
produtos = dict()
compras = list()

for itemm, numero in produto['alimentos'].items():
    print('{}{}{} -> {}{}{}'.format(negr_subli, numero, final, red, itemm, final))
while True:
    while True:
        produtos.clear()
        p = int(input(f'{negrito}Digite o número do produto que você quer: {final}'))
        produtos['item'] = list(produto['alimentos1'])[p - 1]
        produtos['valor'] = float(list(produto['valor1'])[p - 1])
        produtos['quantidade'] = float(input(f'{negrito}Quantos {produtos["item"]} você quer comprar? {final}'))
        produtos['total'] = round(produtos['quantidade'] * produtos['valor'], 2)
        soma += produtos['total']
        if cont == 0:
            maior = menor = produtos['valor']
            pma = pme = produtos['item']
        else:
            if maior < produtos['valor']:
                maior = produtos['valor']
                pma = produtos['item']

            if menor > produtos['valor']:
                menor = produtos['valor']
                pme = produtos['item']

        produtos['valor'] = str(produtos['valor'])
        produtos['quantidade'] = str(produtos['quantidade'])
        produtos['total'] = str(produtos['total'])

        produtos['valor'] = 'R$' + produtos['valor']
        produtos['quantidade'] = 'x' + produtos['quantidade']
        produtos['total'] = 'R$' + produtos['total']

        cont += 1
        compras.append(produtos.copy())
        while True:
            rest = str(input(f'{negrito}Quer continuar? [S/N]{final}')).upper().strip()[0]
            if rest in 'SN':
                break
            print(negrito, 'ERRO! Responda apenas S ou N.', final)
        if rest == 'N':
            break
    sleep(2)
    linboni(32)
    print(f'{green}{"FORMA DE PAGAMENTO":-^64}{final}')
    linboni(32)
    print('{}Valor a pagar R${:.2f}{}'.format(negrito, soma, final))
    print(f'{negrito}AVISTA [1]{final}')
    print(f'{negrito}CARTÃO 2x SEM JUROS [2]{final}')
    print(f'{negrito}CARTÃO 3x SEM JUROS [3]{final}')
    print(f'{negrito}CARTÃO 4x COM JUROS COM UM AUMENTO DE 10% DO VALOR TOTAL [4]{final}')
    forma = int(input(f'{negrito}Forma de pagamento? [1/2/3/4]{final}'))
    sleep(2)
    if forma == 1:
        print('\033[1mVocê vai pagar o total de R${:.2f} avista.\033[m'.format(soma))
        break
    elif forma == 2:
        print('\033[1mVocê vai pagar 2 parcelas de R${:.2f}\033[m'.format(soma / 2))
        break
    elif forma == 3:
        print('\033[1mVocê vai pagar 3 parcelas de R${:.2f}\033[m'.format(soma / 3))
        break
    elif forma == 4:
        aumentoo = soma * 0.10
        print('\033[1mO valor total tevi um aumento de R${:.2f}.\033[m'.format(aumentoo))
        print('\033[1mVocê vai pagar 4 parcelas de R${:.2f}\033[m'.format((((soma * 0.10) + soma) / 4)))
        break
    else:
        print('\033[1mForma de pagamento inválida!\033[m')
        print('\033[1mTente novamente!\033[m')
sleep(2)
linigl(60)
print(f'{"No.":<4}{"PRODUTO":<8}{"VALOR":^10}{"QUANT":>6}{"TOTAL":>11}')
for i, a in enumerate(compras):
    print(f'{i + 1:<3} ', end='')
    for v in a.values():
        print(f'{v:<10}', end='')
    print()
linigl(60)
sleep(2)
imposto = soma * 0.40
print(f'\033[1mQuantidade de produtos foi {len(compras)}\033[m')
print('\033[1mVal. Aprox. dos Tríbutos R${:.2f} (40,00%) Fonte: IBPT\033[m'.format(imposto))
print('\033[1mO produto mais barato foi o {} e ele custa R${:.2f}\033[m'.format(pme, menor))
print('\033[1mO produto mais caro foi o {} e ele custa R${:.2f}\033[m'.format(pma, maior))
linboni(32)
sleep(2)
print(f'\033[1;42m{"MUITO OBRIGADO, VOLTE SEMPRE!":-^64}\033[m')
linboni(32)
