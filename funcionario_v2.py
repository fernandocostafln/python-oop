class Funcionario:
    def __init__(self, nome, sobrenome, pagamento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.pagamento = pagamento
        self.email = '%s.%s@empresa.com.br' % (self.nome, self.sobrenome)

    def nome_completo(self):
        return '{} {}'.format(self.nome, self.sobrenome)


func_1 = Funcionario('Andre', 'Guilhon', 1000)
func_2 = Funcionario('Andre', 'Thiesen', 2000)

# print(func_1.email)
# print(func_2.email)
# print('{} {}'.format(func_1.nome, func_1.sobrenome))
#
# print(func_1.nome_completo())
# print(func_2.nome_completo())
print(Funcionario.nome_completo(func_1))
