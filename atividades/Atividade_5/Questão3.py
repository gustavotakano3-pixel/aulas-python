print("Turno de Estudo")
Turno = input("Digite seu Turno de Estudo:")
match Turno:
    case "v"|"V":
        print("Boa Tarde!")
    case "m"|"M":
        print("Bom Dia!")
    case "n"|"N":
        print("Boa Noite!")
    case _:
        print("Turno Inválido!")
        