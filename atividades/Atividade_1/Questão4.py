#Nesse código a ordem dos comandos realizados importam muito pois acabam redefinindo os valores por exemplo:
#Na primeira e na Segunda Linha de código A = 8 e B = 4 porém na terceira linha de código os valores são redefinidos onde:
#A = B logo: B = 4 A = B então A = 4 
#Por fim na última linha de código já com os valores alterados e pré definidos o resultado de B = A+5 é igual á : 4 +5 = 9

A = 8
B = 4
A = B
B = A+5
print("Valor de A:",A)
print("Valor de B:",B)