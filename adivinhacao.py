import random

#Introdução
def jogar():
    print("*******************************************")
    print("***** Bem vindo ao jogo de adivinhação! *****")
    print("*******************************************")


    #Elementar
    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000
    print("Qual nivel de dificuldade?")
    print("[1] Fácil [2] Médio [3] Difícil")

    nivel = int(input("Escolha o nível: "))

    if (nivel ==1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    #Retornos com while
    """
    rodada = 1
    while(rodada <= total_de_tentativas):
        print("Rodada {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite seu número: ")
        print("Você digitou:", chute_str)
        chute = int(chute_str)
    
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto
    
        if(acertou):
            print("Você acertou, parabéns!")
        else:
            if(maior):
                print("Você errou :( seu chute foi maior do que o número secreto")
            elif(menor):
                print("Você errou :( seu chute foi menor do que o número secreto")
        rodada = rodada +1
    print("Fim do jogo!")
    """


    #Retornos com for
    for rodada in range(1, total_de_tentativas + 1):
        print("Rodada {0} de {1}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou:", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Atenção: o número digitado deve ser entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Você acertou, parabéns! Sua pontuação foi {}".format(pontos))
            break
        else:
            if(maior):
                print("Você errou :( seu chute foi maior do que o número secreto")
            elif(menor):
                print("Você errou :( seu chute foi menor do que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo! O número secreto era {}.".format(numero_secreto))

if(__name__ == "__main__"):
    jogar()