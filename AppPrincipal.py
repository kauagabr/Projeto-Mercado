import Uteis
from time import sleep

"""Constantes de cores para usar nas impressões"""
GREEN = "\033[1;42m"
GREEN_SIMPLES = "\033[1;32m"
NEG_SUB = "\033[1;4m"
NEGRITO = "\033[1m"
RED = "\033[1;31m"
RESET = "\033[m"

cont = maior = menor = soma = 0
pma = pme = ""
produtos = dict()
compras = list()
produto = Uteis.produtos()

Uteis.menu()
Uteis.print_alimento(produto)
print()

while True:
    print(f"{NEGRITO}1 - CADASTRAR UM NOVO PRODUTO{RESET}")
    print(f"{NEGRITO}2 - REALIZAR UMA VENDA{RESET}")
    op = int(input("Escolha uma opção: "))
    if op == 1:
        nome = str(input("Nome do novo produto: "))
        valor = float(input("Preço do novo produto: "))
        if produto['produtos'].get(nome):
            print(f"{RED}Já existe esse produto{RESET}")
            print(f"{RED}Tente novamente{RESET}")
        else:
            produto['produtos'][nome] = len(produto['produtos']) + 1
            produto['preços'][valor] = len(produto['preços']) + 1
            nome_preco = str(nome + ' R$ ' + str(f'{valor:.2f}'))
            produto['produtos_preços'][nome_preco] = len(produto['produtos_preços']) + 1
            print()
            print(f"{GREEN_SIMPLES}Aguarde...{RESET}")
            sleep(4)
            Uteis.print_alimento(produto)
    elif op == 2:
        break
    else:
        print(f"{RED}Opção Inválida!{RESET}")
#  O(22n)
while True:
    while True:
        p = int(input(f'{NEGRITO}Digite o código do produto do cliente: {RESET}'))
        if p in produto['produtos'].values():
            produtos.clear()
            produtos['item'] = list(produto['produtos'])[p - 1]
            produtos['valor'] = float(list(produto['preços'])[p - 1])
            produtos['quantidade'] = float(input(f'{NEGRITO}Quantos {produtos["item"]} você quer comprar? {RESET}'))
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
                rest = str(input(f'{NEGRITO}Quer continuar? [S/N]{RESET}')).upper().strip()[0]
                if rest in 'SN':
                    break
                print(f"{RED}ERRO! Responda apenas S ou N.{RESET}")
            if rest == 'N':
                break
        else:
            print(f"{RED}Opção Inválida!{RESET}")
    Uteis.forma_pagamento(soma)
    break
# O(38n³)
Uteis.imprime_produto(compras)
Uteis.final(compras, soma, pme, menor, pma, maior)
# O(2)


