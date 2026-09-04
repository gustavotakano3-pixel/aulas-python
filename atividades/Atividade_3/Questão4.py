print("Boletin Escolar")
nota1 = float(input("Digite sua primeira nota:"))
nota2 = float(input("Digite sua segunda nota:"))
frequencia = float(input("Digite a frequência (%):"))

frequencia = max(0, min(100,frequencia))

media = (nota1 + nota2) / 2

aprovado = media >= 6.0 and frequencia >= 75

print("Média:", media)
print(aprovado)

