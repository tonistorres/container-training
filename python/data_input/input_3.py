# escreva um algoritmo que descreva o cadastro de um funcionario


first_name = input("Enter First Name:")
last_name = input("Enter Last Name:")
age = int(input("Enter the Age:"))
cadastro_ativo = True
salario = float(input("Enter employee salary:"))

print("First Name: %s" % first_name)
print("Last Name: %s" % last_name)
print("Age: %d" % age)
print("Active: %r" % cadastro_ativo)
print("Salary: %.2f" % salario)
