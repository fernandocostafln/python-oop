import datetime


class Funcionario:
    numero_empregados = 0
    aumento = 1.04

    def __init__(self, nome, sobrenome, pagamento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.pagamento = pagamento
        self.email = '%s.%s@empresa.com' % (self.nome, self.sobrenome)
        Funcionario.numero_empregados += 1

    def nome_completo(self):
        return '{} {}'.format(self.nome, self.sobrenome)

    def aplicar_aumento(self):
        self.pagamento = self.pagamento * self.aumento

    @classmethod
    def definir_aumento(cls, aumento):
        cls.aumento = aumento

    @classmethod
    def from_csv(cls, csv):
        nome, sobrenome, pagamento = csv.split(';')
        return cls(nome, sobrenome, pagamento)

    @staticmethod
    def tem_grupo_estudos(dia):
        # Segunda é 0, terça é 1...
        if dia.weekday() == 3:
            return True
        return False


class Desenvolvedor(Funcionario):
    aumento = 1.10

    def __init__(self, nome, sobrenome, pagamento, linguagem='PHP'):
        super().__init__(nome, sobrenome, pagamento)
        self.linguagem = linguagem

    # pass


func_1 = Desenvolvedor('Andre', 'Guilhon', 1000, 'Python')
func_2 = Funcionario('Andre', 'Thiesen', 2000)
print(func_1.pagamento)
func_1.aplicar_aumento()
print(func_1.pagamento)
print('-------------------------------')
print(func_2.pagamento)
func_2.aplicar_aumento()
print(func_2.pagamento)
