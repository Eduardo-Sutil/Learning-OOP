class Calculadora():

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

calc = Calculadora()

while True:
    print('[1] ADIÇÃO\n[2] SUBTRAÇÃO\n[3] MULTIPLICAÇÃO\n[4] DIVISÃO\n[5] FECHAR CALCULADORA')

    escolha = int(input('Escolha uma opção:\n'))

    if escolha in (1,2,3,4,5):

        if escolha == 5:
            break

        a = int(input('Digite o primeiro número:\n'))
        b = int(input('Digite o segundo número:\n'))

        if escolha == 1:
            print(f'A soma de {a} por {b} é igual a {calc.add(a, b)}')

        elif escolha == 2:
            print(f'A subtração de {a} por {b} é igual a {calc.sub(a, b)}')

        elif escolha == 3:
            print(f'A multiplicação de {a} por {b} é igual a {calc.mult(a, b)}')

        else:
            print(f'A divisão de {a} por {b} é igual a {calc.div(a, b)}')

    else:
        print('OPERAÇÃO INVALIDA!\nDesligando Calculadora...')
        break
