from os import system
from time import sleep

def limpar():
    system("cls")

def main():
    limpar()
    palavra = input("Digite a palavra chave: ")
    erro_maximo = int(input("Digite o número máximo de erros: "))
    limpar()
    palavra_secreta = list(palavra)
    letras_descobertas = []
    erros = 0

    print("\n***** Jogo da Forca*****\n")

    for i in range(0, len(palavra_secreta)):
        letras_descobertas.append("_")
    acertou = False

    while acertou == False:
        letra = str(input("Digite a letra: "))

        for item in range(0, len(palavra_secreta)):
            if letra == palavra_secreta[item]:
                letras_descobertas[item] = letra
            limpar()
            print(letras_descobertas[item], end = ' ')
        acertou = True

        if letra not in palavra_secreta:
            erros += 1

        if erros == erro_maximo:
            print("\n\nVocê foi enforcado!\n")
            print("Deseja tentar mais uma vez?")
            op = input("(S) para sim e (N) para não\n").upper()

            if op == 'S':
                main()

            else:
                limpar()
                print("Obrigado por jogar")
                sleep(1)
                break

        print(f"\n\nNúmero de erros: {erros}\n")

        for letras in range(0, len(letras_descobertas)):
            if letras_descobertas[letras] == "_":
                acertou = False
                
    if erros < erro_maximo:
        print("\n\nVocê escapou da forca!\n")

main()