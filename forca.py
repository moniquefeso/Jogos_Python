import random

def jogar():#Os itens dentro dessa função chamam outras funções e deixam o código mais organizado
    apresentacao()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0



    while(not enforcou and not acertou):
        chute = solicita_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_ganhador()
    else:
        imprime_mensagem_perdedor()





def apresentacao():
    #Introdução
    print("*************************************")
    print("**** Bem vindo ao jogo de forca! ****")
    print("*************************************")

def carrega_palavra_secreta():
    # Elementar
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def solicita_chute():
    chute = input("Digite a letra: ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def imprime_mensagem_ganhador(palavra_secreta):
    return print("Parabéns, você acertou! A palavra secreta é {}".format(palavra_secreta.upper()))
    print("Fim do jogo!")

def imprime_mensagem_perdedor(palavra_secreta):
    return print("Poxa, você não acertou! A palavra secreta é {}".format(palavra_secreta.upper()))
    print("Fim do jogo!")



if(__name__ == "__main__"):#Sempre será no final
    jogar()