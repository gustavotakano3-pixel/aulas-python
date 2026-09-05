print("Calculadora Básica de Dois Números")
num1 = int(input("Digite um número Real:"))
num2 = int(input("Digite outro número Real:"))
operador = (input("Digite um Operador Aritimético:"))

match operador:
    case "+":
        print(num1+num2)
    case "-":
        print(num1-num2)
    case "*":
        print(num1*num2)
    case "/":
        print(num1/num2)
    case _:
        print("Operação Inválida!")

