"""
Calculadora em Python
"""


def imprime_opcoes():
    print('***********Calculadora em Python***********\n*****Escolha uma das seguintes opções:*****\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n9 - Sair')


adicao = lambda parcela1, parcela2: parcela1 + parcela2

subtracao = lambda minuendo, subtraendo: minuendo - subtraendo

multiplicacao = lambda multiplicando, multiplicador: multiplicando * multiplicador

divisao = lambda dividendo, divisor: dividendo / divisor


def executa(opcao):
    if opcao == 9:
        print('Até logo!')
    if opcao == 1:
        parcela1 = float(input('Digite a primeira parcela: '))
        parcela2 = float(input('Digite a segunda parcela: '))
        print(adicao(parcela1, parcela2))
    elif opcao == 2:
        minuendo = float(input('Digite o minuendo: '))
        subtraendo = float(input('Digite o subtraendo: '))
        print(subtracao(minuendo, subtraendo))
    elif opcao == 3:
        multiplicando = float(input('Digite o multiplicando: '))
        multiplicador = float(input('Digite o multiplicador: '))
        print(multiplicacao(multiplicando, multiplicador))
    elif opcao == 4:
        dividendo = float(input('Digite o dividendo: '))
        divisor = float(input('Digite o divisor: '))
        print(divisao(dividendo, divisor))
    else:
        print('Opção inválida! ')


def solicita_opcao(opcao):
    opcao = opcao
    while opcao != 9:
        opcao = (int(input('Digite a opção desejada: ')))
        if opcao == 9:
            print('Até logo!')
        else:
            executa(opcao)


def main():
    imprime_opcoes()
    opcao = 0
    solicita_opcao(opcao)


main()
