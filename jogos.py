import adivinhacao
import forca
import helper


print("**************************************")
print("Bem vindo ao menu de seleção de jogos!")
print("**************************************")
print( "(1) Jogo de Adivinhação")
print( "(2) Jogo da Forca")
print("**************************************")

selected_game = int(input("Digite o número do jogo desejado: "))

helper.cls()

if selected_game == 1:
    adivinhacao.play()
else:
    forca.play()




