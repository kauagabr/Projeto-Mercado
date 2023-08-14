"""Funções úteis para o App Principal"""

from time import sleep

"""Constantes de cores para usar nas impressões"""
GREEN = "\033[1;42m"
GREEN_SIMPLES = "\033[1;32m"
NEG_SUB = "\033[1;4m"
NEGRITO = "\033[1m"
RED = "\033[1;31m"
RESET = "\033[m"


def linha(cont):
    """Imprime uma linha tracejada na tela."""
    print("-" * cont)


def linha_dupla(cont):
    """Imprime uma linha dupla na tela."""
    print("=" * cont)


def produtos():
    """A lista de produtos com dicionários separados
    para os produtos, preços e seus índices"""
    return {'produtos_preços': {
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
            'Refrigerante R$ 6,25': 30},
            'produtos': {
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
            'Refrigerante': 30},
            'preços': {
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
            6.25: 30}
            }


def menu():
    """Imprime o início de um cupom fiscal."""
    from datetime import datetime
    atual = datetime.now()
    linha_dupla(60)
    print(f'{GREEN}{"MERCADO DO IFPE LTDA":-^60}{RESET}')
    linha_dupla(60)
    print(NEG_SUB, "AV. FULANO COLOMBO, 99 - SAVASSI \n"
                   " CEP: 55540-000 - PALMARES - PE \n"
                   " CNPJ:99.999.999/0001-01 \n"
                   " IE: 999.999.999 \n"
                   " IM: 99.999.999", RESET)
    linha(60)
    print(atual.strftime("%d/%m/%Y, %H:%M:%S"), "============================= COD:00001")
    print(f'{NEGRITO}{"CUPOM FISCAL":-^60}{RESET}')


def print_alimento(produto):
    linha_dupla(60)
    print(f'{GREEN}{"ALIMENTOS":-^60}{RESET}')
    linha_dupla(60)
    for itens, numero in produto['produtos_preços'].items():
        print('{}{}{} -> {}{}{}'.format(NEG_SUB, numero, RESET, RED, itens, RESET))


def forma_pagamento(soma):
    """Imprime a forma de pagamento"""
    sleep(2)
    linha(60)
    print(f'{GREEN}{"FORMA DE PAGAMENTO":-^60}{RESET}')
    linha(60)
    print(f'{GREEN_SIMPLES}Valor à pagar R${soma:.2f}{RESET}')
    print(f'{NEGRITO}À VISTA [1]{RESET}')
    print(f'{NEGRITO}CARTÃO 2x SEM JUROS [2]{RESET}')
    print(f'{NEGRITO}CARTÃO 3x SEM JUROS [3]{RESET}')
    print(f'{NEGRITO}CARTÃO 4x COM JUROS COM UM AUMENTO DE 10% DO VALOR TOTAL [4]{RESET}')
    while True:
        forma = int(input(f'{NEGRITO}Forma de pagamento? [1/2/3/4]{RESET}'))
        sleep(2)
        if forma == 1:
            print(f'{GREEN_SIMPLES}Você vai pagar o total de R${soma:.2f} avista.{RESET}')
            break
        elif forma == 2:
            print(f'{GREEN_SIMPLES}Você vai pagar 2 parcelas de R${soma / 2:.2f}{RESET}')
            break
        elif forma == 3:
            print(f'{GREEN_SIMPLES}Você vai pagar 3 parcelas de R${soma / 3:.2f}{RESET}')
            break
        elif forma == 4:
            print(f'{GREEN_SIMPLES}O valor total teve um aumento de R${soma * 0.10:.2f}{RESET}')
            print(f'{GREEN_SIMPLES}Você vai pagar 4 parcelas de R${(((soma * 0.10) + soma) / 4):.2f}{RESET}')
            break
        else:
            print(f'{RED}Forma de pagamento inválida!{RESET}')
            print(f'{RED}Tente novamente!{RESET}')


def formatcpf(cpf):
    vezes = 0
    novo = ""
    for quantidade in range(11):
        numero = cpf[quantidade]
        novo += numero
        vezes += 1
        if quantidade == 8:
            novo += "-"
            vezes -= 3
        if vezes == 3:
            novo += "."
            vezes -= 3
    return novo


def imprime_produto(compras):
    sleep(2)
    linha_dupla(60)
    op = str(input("CPF NO CUPOM FISCAL? [S/N]")).upper().strip()[0]
    if op == 'S':
        cpf = str(input("INFORME O CPF (Somente números): "))
        print(f"CPF: {formatcpf(cpf)}")
        print()
        print(f'{"No.":<4}{"PRODUTO":<8}{"VALOR":^10}{"QUANT":>6}{"TOTAL":>11}')
        for i, a in enumerate(compras):
            print(f'{i + 1:<3} ', end='')
            for v in a.values():
                print(f'{v:<10}', end='')
            print()
        linha_dupla(60)
        sleep(2)
    elif op == 'N':
        print(f'{"No.":<4}{"PRODUTO":<8}{"VALOR":^10}{"QUANT":>6}{"TOTAL":>11}')
        for i, a in enumerate(compras):
            print(f'{i + 1:<3} ', end='')
            for v in a.values():
                print(f'{v:<10}', end='')
            print()
        linha_dupla(60)
        sleep(2)
    else:
        print(f"{RED}Opção Inválida!{RESET}")


def final(compras, soma, pme, menor, pma, maior):
    print(f'\033[1mQuantidade de produtos foi {len(compras)}\033[m')
    print('\033[1mVal. Aprox. dos Tríbutos R${:.2f} (40,00%) Fonte: IBPT\033[m'.format(soma * 0.40))
    print('\033[1mO produto mais barato foi o {} e ele custa R${:.2f}\033[m'.format(pme, menor))
    print('\033[1mO produto mais caro foi o {} e ele custa R${:.2f}\033[m'.format(pma, maior))
    linha_dupla(60)
    sleep(2)
    print(f'{GREEN}{"MUITO OBRIGADO, VOLTE SEMPRE!":-^60}{RESET}')
    linha_dupla(60)
