def adicao(x, y):
    return x + y


def subtracao(x, y):
    return x - y


def multiplicacao(x, y):
    return x * y


def divisao(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    else:
        return x / y


print("\33[33mSelecione a operação:\n")
print("\33[34m1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

escolha = input("\n\33[35mDigite a sua escolha:\33[m \n")

num1 = float(input("\33[32mDigite o primeiro número:\33[m "))
num2 = float(input("\33[36mDigite o segundo número: \33[37m"))

if escolha == '1':
    print("\nResultado:", adicao(num1, num2))
elif escolha == '2':
    print("\nResultado:", subtracao(num1, num2))
elif escolha == '3':
    print("\nResultado:", multiplicacao(num1, num2))
elif escolha == '4':
    print("\nResultado:", divisao(num1, num2))
else:
    print("\nEscolha inválida")
