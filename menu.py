import forca
import adivinhacao

def escolhe_jogo():
    print("******************************************")
    print("****** Bem vindo ao menu de jogos! *******")
    print("************ Escolha seu jogo ************")
    print("******************************************")

    print("[1] Forca [2] Adivinhação")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando Adivinhação")
        adivinhacao.jogar()

#Chegagem de escopo
""" No Python, precisamos definir o módulo que está sendo executado. 
    Nesse menu, se executarmos o código sem a checagem, a execução entrará no primeiro import,
    o que não deveria acontecer, então a checagem permite verificar o 'main' que estamos executando
    e permanecer neste módulo."""
if(__name__ == "__main__"):
    escolhe_jogo()