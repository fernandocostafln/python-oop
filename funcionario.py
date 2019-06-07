class Funcionario:
    pass


func_1 = Funcionario()
func_2 = Funcionario()

print(func_1)
print(func_2)

func_1.nome = 'Andre'
func_1.sobrenome = 'Guilhon'
func_1.email = 'Andre.Guilhon@empresa.com.br'
func_1.pagamento = 1000

func_2.nome = 'Andre'
func_2.sobrenome = 'Thiesen'
func_2.email = 'Andre.Thiesen@empresa.com.br'
func_2.pagamento = 2000

print(func_1.email)
print(func_2.email)
