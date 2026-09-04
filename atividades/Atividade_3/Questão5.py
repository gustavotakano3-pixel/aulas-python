print("Sistema de Desconto")
valor_compra = float(input("Digite o valor da compra:"))
cartão = int(input("Tem cartão? 1 para sim 0 para não:"))

desconto = valor_compra >= 200
desconto2 = cartão == 1

frete_gratis = desconto or desconto2

print("Você ganhou frete grátis !",frete_gratis)