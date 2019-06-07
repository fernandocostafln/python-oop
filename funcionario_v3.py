class Funcionario:
    aumento = 1.04

    def __init__(self, nome, sobrenome, pagamento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.pagamento = pagamento
        self.email = '%s.%s@empresa.com' % (self.nome, self.sobrenome)

    def nome_completo(self):
        return '{} {}'.format(self.nome, self.sobrenome)

    def aplicar_aumento(self):
        self.pagamento = self.pagamento * self.aumento


func_1 = Funcionario('Andre', 'Guilhon', 1000)
func_2 = Funcionario('Andre', 'Thiesen', 2000)

print(func_1.pagamento)
func_1.aplicar_aumento()
print(func_1.pagamento)

print(func_2.pagamento)
func_2.aplicar_aumento()
print(func_2.pagamento)
