import random

def Jogar():
    print("********************************")
    print("Bem vindo ao jogo de advinhação!")
    print("********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    rodada = 1

    print("Selecione a dificuldade do jogo:")
    dificuldade = int(input("(1) Fácil (2) Médio (3) Difícil: "))

    if(dificuldade == 1):
        total_de_tentativas = 20
    elif(dificuldade == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    while(rodada <= total_de_tentativas):

        print("Rodada {} de {}".format(rodada, total_de_tentativas))
        palpite = int(input("Digite o número: "))
        print("Seu palpite foi:", palpite)

        acertou = numero_secreto == palpite
        maior = numero_secreto < palpite
        menor = numero_secreto > palpite

        if(acertou):
            print("Você acertou!")
            break
        elif(maior):
            print("O seu palpite foi maior que o número secreto!")
        elif(menor):
            print("O seu palpite foi menor que o número secreto!")

        rodada += 1

if(__name__=="__main__"):
    Jogar()
