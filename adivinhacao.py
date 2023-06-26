import jogos
import random


def play():
    print("********************************")
    print("Bem vindo ao jogo de advinhação!")
    print("********************************")

    secret_number = random.randrange(1, 101)
    total_attempts = 0
    game_turn = 1
    game_score = 1000

    print("Selecione a dificuldade do jogo:")
    level = int(input("(1) Fácil (2) Médio (3) Difícil: "))

    if level == 1:
        total_attempts = 20
    elif level == 2:
        total_attempts = 10
    else:
        total_attempts = 5

    while game_turn <= total_attempts:

        print("Rodada {} de {}".format(game_turn, total_attempts))
        guess = int(input("Digite o número: "))
        print("Seu palpite foi:", guess)

        riddle = secret_number == guess
        bigger = secret_number < guess
        minor = secret_number > guess

        if riddle:
            print("Você acertou!")
            break
        elif bigger:
            print("O seu palpite foi maior que o número secreto!")
            game_score -= abs(secret_number - guess)
        elif minor:
            print("O seu palpite foi menor que o número secreto!")
            game_score -= abs(secret_number - guess)

        game_turn += 1

    print("Your Final Score is: {}".format(game_score))
    jogos.play()


if __name__ == "__main__":
    play()
