import random

numero_secreto = random.randrange(1, 101)


def jogar():
    total_de_tentativas = elementar()
    definindo_chutes(total_de_tentativas)

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

#Funções
def elementar():
    print("*******************************************")
    print("**** Bem vindo ao jogo de adivinhação! ****")
    print("*******************************************")
    print("Qual nivel de dificuldade?")
    print("[1] Fácil [2] Médio [3] Difícil")

    nivel = int(input("Escolha o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    return total_de_tentativas


def definindo_chutes(total_de_tentativas):
    pontos = 1000
    for rodada in range(1, total_de_tentativas + 1):
        print("Rodada {0} de {1}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou:", chute_str)
        chute: int = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Atenção: o número digitado deve ser entre 1 e 100!")
            continue

        if chute == numero_secreto:
            resposta = "acertou"
            resultados(resposta, pontos)
            break
        elif chute > numero_secreto:
            resposta = "maior"
            pontos = pontos - chute
            resultados(resposta, pontos)
        else:
            resposta = "menor"
            pontos = pontos - chute
            resultados(resposta, pontos)

    print("Fim do jogo! O número secreto era {}.".format(numero_secreto))

def resultados(resposta, pontos):
    if resposta == "acertou":
        print("Parabéns! Você acertou! Sua pontuação é: {}".format(pontos))
    elif resposta == "maior":
        print("Seu chute foi maior que o número secreto.")
    else:
        print("Seu chute foi menor que o número secreto.")


if (__name__ == "__main__"):
    jogar()