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
        self.pagamento = self.pagamento * 1.04

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


func_1 = 'Andre;Guilhon;1000'
func_2 = 'Andre;Thiesen;2000'
func_3 = 'Diego;Oliveira;2000'

# nome, sobrenome, pagamento = func_1.split(';')
#
# novo_funcionario_1 = Funcionario(nome, sobrenome, pagamento)
#
# nome, sobrenome, pagamento = func_2.split(';')
#
# novo_funcionario_2 = Funcionario(sobrenome=sobrenome, pagamento=pagamento, nome=nome)

novo_funcionario_3 = Funcionario.from_csv(func_3)
print(novo_funcionario_3.nome_completo())
print(Funcionario.tem_grupo_estudos(datetime.datetime.now()))

