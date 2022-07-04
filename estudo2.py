class User():

    def __init__(self, nome, alimentacao, aluguel, transporte, demais_despesas):
        self.nome = nome
        self.alimentacao = int(alimentacao)
        self.aluguel = int(aluguel)
        self.transporte = int(transporte)
        self.demais_despesas = int(demais_despesas)

    def get_total(self):
        return self.alimentacao + self. aluguel + self.transporte + self.demais_despesas

    def alterar_nome(self, nome_novo):
        self.nome = nome_novo

    def alterar_alimentacao(self, alimentacao_nova):
        self.alimentacao = alimentacao_nova

    def alterar_aluguel(self, transporte_novo):
        self.transporte = transporte_novo

    def alterar_demais_despesas(self, demais_despesas_nova):
        self.demais_despesas = demais_despesas_nova


pessoa1 = User('Eduardo', 400, 1000, 200, 250)

print(pessoa1.alimentacao)

pessoa1.alterar_alimentacao(900)

print(pessoa1.alimentacao)


