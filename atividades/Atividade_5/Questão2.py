print("Classificador de Vogais e Consoantes")
letra = input("Digite uma Letra:")
match letra:
    case "a"|"e"|"i"|"o"|"u":
        print("Você Digitou Uma Vogal!")
    case _:
        print("Não é uma vogal.")
