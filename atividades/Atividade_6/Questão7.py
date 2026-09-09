print("Controle de Orçamento")
orcamento = 500
print("Orçamento total",orcamento)
gasto = int(input("Digite o valor do gasto:"))
while orcamento > 0:
    orcamento -= gasto
    print("orçamento restante",orcamento)
    gasto = int(input("Digite o valor do próximo gasto:"))
