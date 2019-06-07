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

    @property
    def nome_completo(self):
        return '{} {}'.format(self.nome, self.sobrenome)

    # Definição de setter deve ser feita na forma de um decorator (@qualquercoisa), cujo nome é @propriedade.setter.
    # Por exemplo, para criar um setter para o nome, poderia usar @nome.setter como decorator.
    @nome_completo.setter
    def nome_completo(self, nome_completo):
        nome, sobrenome = nome_completo.split(' ')
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = '%s.%s@empresa.com' % (self.nome, self.sobrenome)

    def aplicar_aumento(self):
        self.pagamento = self.pagamento * 1.04

    @classmethod
    def definir_aumento(cls, aumento):
        cls.aumento = aumento

    # @classmethod
    # def from_csv(cls, csv):
    #     nome, sobrenome, pagamento = csv.split(';')
    #     return cls(nome, sobrenome, pagamento)

    @staticmethod
    def tem_grupo_estudos(dia):
        # Segunda é 0, terça é 1...
        if dia.weekday() == 3:
            return True
        return False


class Desenvolvedor(Funcionario):
    aumento = 1.10

    def __init__(self, nome, sobrenome, pagamento, linguagem):
        super().__init__(nome, sobrenome, pagamento)
        self.linguagem = linguagem

    pass


class Chefe(Funcionario):

    def __init__(self, nome, sobrenome, pagamento, funcionarios=None):
        super().__init__(nome, sobrenome, pagamento)
        if funcionarios is None:
            self.funcionarios = []
        else:
            self.funcionarios = funcionarios

    def adicionar_funcionario(self, funcionario):
        if funcionario not in self.funcionarios:
            self.funcionarios.append(funcionario)

    def remove_funcionario(self, funcionario):
        if funcionario in self.funcionarios:
            self.funcionarios.remove(funcionario)

    def print_empregados(self):
        for funcionario in self.funcionarios:
            print('--->', funcionario.nome_completo)


func_1 = Desenvolvedor('Andre', 'Guilhon', 1000, 'python')
func_2 = Desenvolvedor('Andre', 'Thiesen', 2000, 'ecma')
func_3 = Funcionario('Fernando', 'Costa', 2000)

chefe_1 = Chefe('Richard', 'Vieira', 10000, [func_1])
# print(chefe_1.funcionarios[0].nome)
chefe_1.adicionar_funcionario(func_2)
chefe_1.adicionar_funcionario(func_3)
chefe_1.adicionar_funcionario(func_1)

func_1.nome_completo = 'João Mendes'
print(func_1.nome)
chefe_1.remove_funcionario(func_3)
chefe_1.print_empregados()
