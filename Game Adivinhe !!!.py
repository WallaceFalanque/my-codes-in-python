import random


class JogoAdivinharNumero:
    def __init__(self, minimo=1, maximo=100, tentativas=5):
        self.minimo = minimo
        self.maximo = maximo
        self.numero_secreto = random.randint(minimo, maximo)
        self.tentativas_restantes = tentativas

    def jogar(self):
        print(f"Bem-vindo ao Jogo de Adivinhar o Número! Você tem {self.tentativas_restantes} tentativas.")
        while self.tentativas_restantes > 0:
            try:
                palpite = int(input(f"Digite um número entre {self.minimo} e {self.maximo}: "))
                if palpite < self.minimo or palpite > self.maximo:
                    print(f"Por favor, digite um número entre {self.minimo} e {self.maximo}.")
                    continue

                if palpite == self.numero_secreto:
                    print("Parabéns! Você adivinhou o número correto!")
                    return
                elif palpite < self.numero_secreto:
                    print("O número secreto é maior.")
                else:
                    print("O número secreto é menor.")

                self.tentativas_restantes -= 1
                print(f"Você tem {self.tentativas_restantes} tentativas restantes.")

            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro.")

        print(f"Suas {self.tentativas} tentativas acabaram. O número secreto era {self.numero_secreto}.")

jogo = JogoAdivinharNumero()
jogo.jogar()
