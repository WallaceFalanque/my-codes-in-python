import random


class JogoPedraPapelTesoura:
    def __init__(self):
        self.opcoes = ['Pedra', 'Papel', 'Tesoura']

    def jogar(self):
        while True:
            escolha_usuario = self.obter_escolha_usuario()
            if escolha_usuario == '4':
                print("Obrigado por jogar!")
                break

            if escolha_usuario not in ['1', '2', '3']:
                print("Escolha inválida. Por favor, escolha uma opção válida.")
                continue

            escolha_computador = random.choice(self.opcoes)

            print(f"Você escolheu: {self.opcoes[int(escolha_usuario) - 1]}")
            print(f"O computador escolheu: {escolha_computador}")

            resultado = self.determinar_vencedor(int(escolha_usuario), escolha_computador)
            if resultado == 'empate':
                print("Empate!")
            elif resultado == 'usuario':
                print("Você ganhou!")
            else:
                print("Você perdeu!")

    def obter_escolha_usuario(self):
        print("Escolha sua jogada: ")
        print("1. Pedra")
        print("2. Papel")
        print("3. Tesoura")
        print("4. Sair do jogo")
        return input("Digite o número da sua escolha: ")

    def determinar_vencedor(self, escolha_usuario, escolha_computador):
        if self.opcoes[escolha_usuario - 1] == escolha_computador:
            return 'empate'
        elif (self.opcoes[escolha_usuario - 1] == 'Pedra' and escolha_computador == 'Tesoura') or \
                (self.opcoes[escolha_usuario - 1] == 'Papel' and escolha_computador == 'Pedra') or \
                (self.opcoes[escolha_usuario - 1] == 'Tesoura' and escolha_computador == 'Papel'):
            return 'usuario'
        else:
            return 'computador'

jogo = JogoPedraPapelTesoura()
jogo.jogar()
