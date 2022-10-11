"""
Máscara	Tipo de Dado	Descrição
%d  ou %i	Int (inteiro)	Exibe um valor inteiro.
%f	Float ou double	Exibe um valor decimal.
%ld	Long Int	Exibe um número inteiro longo.
%e ou %E	Float e double	Exibe um número exponencial (número científico).
%c	Char (caractere)	Exibe um caractere.
%o	Int	Exibe um número inteiro em formato octal.
%x ou %X	Int	Exibe um número inteiro no formato hexadecimal.
%s	Char	Exibe uma cadeia de caracteres (string).
%r	Boolean	Exibe true ou false (verdadeiro ou falso).
"""
# https://www.google.com/search?q=python+mascara+de+formata%C3%A7%C3%A3o&oq=python+mascara+de+formata%C3%A7%C3%A3o&aqs=chrome..69i57j33i160.6822j0j7&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:3a831866,vid:0o4VtdMhQN4,st:0

codigo = 10
salario = 1500
nome = "tonis torres"
ativo = True


print("meu nome é %s" % nome)
print("Código: %d" % codigo)
print("Salario %.2f" % salario)
print("Situação do cadastro %r" % ativo)
