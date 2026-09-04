print("Formulário")
nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
plano = (input("Tem plano de Saúde? dite 1 para sim e 0 para não:"))
possui_plano = plano == "1"
fui_aceito = possui_plano
print("Seu nome é:",nome,"Você tem:",idade,"Anos","Tem plano?:",possui_plano,"Você foi aceito?:",fui_aceito)