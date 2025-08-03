import math

def exibir_menu():
    print("\n--- Calculadora Científica ---")
    print("  + : Adição")
    print("  - : Subtração")
    print("  * : Multiplicação")
    print("  / : Divisão")
    print("  ^ : Potência (x^y)")
    print("  sqrt : Raiz Quadrada")
    print("  log  : Logaritmo na base 10")
    print("  ln   : Logaritmo natural")
    print("  sen  : Seno")
    print("  cos  : Cosseno")
    print("  tan  : Tangente")
    print("  rad  : Converter para Radianos")
    print("  grau : Converter para Graus")
    print("  pi   : O valor de Pi")
    print("  e    : O valor de Euler")
    print("  sair : Sair da calculadora")

def calcular(operacao, num1=None, num2=None):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 == 0:
            return "Erro: Divisão por zero."
        return num1 / num2
    elif operacao == '^':
        return num1 ** num2
    elif operacao == 'sqrt':
        if num1 < 0:
            return "Erro: Raiz quadrada de número negativo."
        return math.sqrt(num1)
    elif operacao == 'log':
        if num1 <= 0:
            return "Erro: Logaritmo de número não positivo."
        return math.log10(num1)
    elif operacao == 'ln':
        if num1 <= 0:
            return "Erro: Logaritmo natural de número não positivo."
        return math.log(num1)
    elif operacao == 'sen':
        return math.sin(num1)
    elif operacao == 'cos':
        return math.cos(num1)
    elif operacao == 'tan':
        return math.tan(num1)
    elif operacao == 'rad':
        return math.radians(num1)
    elif operacao == 'grau':
        return math.degrees(num1)
    else:
        return "Operação inválida."

def main():
    while True:
        exibir_menu()
        operacao = input("\nDigite a operação desejada: ").lower()

        if operacao == 'sair':
            print("Encerrando a calculadora. Até mais!")
            break
        elif operacao == 'pi':
            print(f"O valor de pi é: {math.pi}")
            continue
        elif operacao == 'e':
            print(f"O valor de e é: {math.e}")
            continue

        if operacao in ['+', '-', '*', '/', '^']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                resultado = calcular(operacao, num1, num2)
                print(f"Resultado: {resultado}")
            except ValueError:
                print("Entrada inválida. Por favor, digite números.")
            except Exception as e:
                print(f"Ocorreu um erro: {e}")
        elif operacao in ['sqrt', 'log', 'ln', 'sen', 'cos', 'tan', 'rad', 'grau']:
            try:
                num1 = float(input("Digite o número: "))
                resultado = calcular(operacao, num1)
                print(f"Resultado: {resultado}")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
            except Exception as e:
                print(f"Ocorreu um erro: {e}")
        else:
            print("Operação inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()

