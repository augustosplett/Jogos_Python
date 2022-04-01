import helper


def play():
    print("********************************")
    print("Bem vindo ao jogo de forca!")
    print("********************************")

    secret_word = "banana".strip().upper()

    word_letters = []
    for letter in secret_word:
        word_letters.append("_")
    print(word_letters)

    wrong_guesses = set()

    riddle = False
    hang = False
    error_limit = 0

    while not riddle and not hang:

        guess = input("Qual letra deseja chutar? ").strip().upper()

        index = 0
        for letter in secret_word:
            if guess == letter:
                word_letters[index] = letter
            else:
                error_limit += 1

            if guess not in secret_word:
                wrong_guesses.add(guess)

            index += 1

        hang = error_limit == 6
        riddle = "_" not in word_letters

        helper.cls()

        print("Jogando...")
        print("Tentativas Erradas {}".format(wrong_guesses))
        print("Palavra Secreta {}".format(word_letters))

    if riddle:
        print("Fim do Jogo, você ganhou!")
    else:
        print("Fim do Jogo, você perdeu!")


if __name__ == "__main__":
    play()