import helper
import random


def play():
    print_welcome_message()
    secret_word = generate_secret_word()

    word_letters = ["_" for letter in secret_word]
    print(word_letters)

    wrong_guesses = set()

    riddle = False
    hang = False
    error_limit = 0

    desenha_forca(error_limit)

    while not riddle and not hang:

        guess = ask_for_a_guess()

        if guess in secret_word:
            handle_correct_guess(guess, secret_word, word_letters)
        else:
            error_limit += 1

        if guess not in secret_word:
            wrong_guesses.add(guess)

        update_screen(error_limit)

        hang = error_limit == 7
        riddle = "_" not in word_letters

        print("Tentativas Erradas {}".format(sorted(list(wrong_guesses))))
        print("Palavra Secreta {}".format(word_letters))

    if riddle:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(secret_word)


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 0):
        print (" |            ")
        print (" |            ")
        print (" |            ")
        print (" |            ")

    if(erros == 1):
        print (" |      (_)   ")
        print (" |            ")
        print (" |            ")
        print (" |            ")

    if(erros == 2):
        print (" |      (_)   ")
        print (" |      \     ")
        print (" |            ")
        print (" |            ")

    if(erros == 3):
        print (" |      (_)   ")
        print (" |      \|    ")
        print (" |            ")
        print (" |            ")

    if(erros == 4):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |            ")
        print (" |            ")

    if(erros == 5):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |            ")

    if(erros == 6):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      /     ")

    if (erros == 7):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def update_screen(error_limit):
    helper.cls()
    desenha_forca(error_limit)


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def handle_correct_guess(guess, secret_word, word_letters):
    index = 0
    for letter in secret_word:
        if guess == letter:
            word_letters[index] = letter
        index += 1


def ask_for_a_guess():
    return input("Qual letra deseja chutar? ").strip().upper()


def print_welcome_message():
    print("********************************")
    print("Bem vindo ao jogo de forca!")
    print("********************************")


def generate_secret_word():
    words_list = []
    words_file = open("palavras.txt", "r")

    for line in words_file:
        words_list.append(line.strip().upper())

    words_file.close()
    return words_list[random.randrange(0, len(words_list))]


if __name__ == "__main__":
    play()