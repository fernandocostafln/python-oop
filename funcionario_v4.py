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


func_1 = Funcionario(nome='Andre',  pagamento=1000, sobrenome='Guilhon')
func_2 = Funcionario('Andre', 'Thiesen', 2000)
func_3 = Funcionario('Andre', 'Mathias', 200000)

func_1.definir_aumento(1.05)

print(func_1.nome_completo())
