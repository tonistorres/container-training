"""
Caracteres de escape
Outros caracteres de escape usados ​​em Python:

Code	Result	Try it
\'	Single Quote
\\	Backslash
\n	New Line
\r	Carriage Return
\t	Tab
\b	Backspace
\f	Form Feed
\ooo	Octal value
\xhh	Hex value

"""
# https://www.w3schools.com/python/python_strings_escape.asp

txt = 'It\'s alright.'
print(txt)

txt2 = "This will insert one \\ (backslash)."
print(txt2)

txt3 = "Hello\nWorld!"
print(txt3)

txt4 = "Hello\rWorld!"
print(txt4)

txt5 = "Hello\tWorld!"
print(txt5)

#This example erases one character (backspace):
txt6 = "Hello \bWorld!"
print(txt6)

