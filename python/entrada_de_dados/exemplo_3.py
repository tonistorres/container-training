# escreva um algoritmo que descreva o cadastro de um funcionario


first_name = input("Digite o Primeiro Nome:")
last_name = input("Digite o Ultimo Nome:")
age = int(input("Digite a idade:"))
cadastro_ativo = True
salario = float(input("Digite o Salario do Funcionario:"))

print("First Name: %s" % first_name)
print("Last Name: %s" % last_name)
print("Age: %d" % age)
print("Ativo: %r" % cadastro_ativo)
print("Salário: %.2f" % salario)
