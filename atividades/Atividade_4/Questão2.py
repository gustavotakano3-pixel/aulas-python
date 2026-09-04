print ("radar de velocidade")
velocidade = int(input("Digite a velocidade atual do carro em km/h:"))
vel_max = 80
if velocidade > vel_max:
    print("Você foi multado!")
else:
     print("Você está dentro do limite de velocidade,Boa viagem!")