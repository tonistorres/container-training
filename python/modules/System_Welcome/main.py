"""
Usar um módulo
Agora podemos usar o módulo que acabamos de criar, usando a importinstrução:
"""
import module1.mod_welcome as mw

welcome_system = mw.greeting_system(name="Tonis")
print(welcome_system)

welcome_work = mw.greeting_work(name="Alberto")
print(welcome_work)

welcome_product = mw.greeting_product(first_name="Tonis", last_name="Ferreira")
print(welcome_product)
