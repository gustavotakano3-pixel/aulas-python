#Fábrica de caixas de Maçãs
print("Bem-Vindo")

total_macas_caixa= 12

macas_colhidas =int(input("digite a quantidade de maçãs:" ))

total_caixas = macas_colhidas // total_macas_caixa

print("Seu total de caixas foi:",total_caixas)

total_de_maçãs_nas_caixas =total_macas_caixa * total_caixas

print("seu total de maçãs nas caixas foi:",total_de_maçãs_nas_caixas)

sobras = macas_colhidas - total_de_maçãs_nas_caixas

print("Sobras:",sobras,"maçãs")




