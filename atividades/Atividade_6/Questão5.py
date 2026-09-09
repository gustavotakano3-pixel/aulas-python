print("Tabuada Simples")

tabuada = int(input("Digite a tabuada que você quer ver:"))

contador = 1

while contador <= 10:
    resultado = tabuada * contador
    print(tabuada, "x", contador, "=", resultado)
    contador += 1

