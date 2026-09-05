print("Estações do Ano")
meses = int(input("Digite um mês do ano:"))
match meses:
    case 12|1|2:
        print("Verão")
    case 3|4|5:
        print("Outono")
    case 6|7|8:
        print("Inverno")
    case 9|10|11:
        print("Primavera")
    case _:
        print("Mês Inválido!")