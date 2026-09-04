print("A Catraca VIP de Eventos (Uso de AND e OR no if)")
idade = int(input("Digite Sua Idade:"))
Organizador = input("Você é um organizador?:")
vip = input("Você possuí o VIP?:")
if idade >= 18 and vip == "1" or Organizador == "1":
    print("Entrada Permitida! Seja bem-vindo(a)") 
else:
    print("Entrada NEGADA! Você não atende aos requisitos")