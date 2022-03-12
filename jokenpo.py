import random

print("Bem vindo ao JOKENPÔ!!!!")
print("Você jogará contra o computador! Prepare-se!!")

def inicia_jogo():
    print("Opções: [0] => Pedra - [1] => Papel - [2] => Tesoura")
    pergunta = int(input("Insira sua opção:"))
    maquina = random.randint(0,2)
    
    if maquina == 0:
        if pergunta == 0:
            print("Empate! Os dois escolheram PEDRA !")
        elif pergunta == 1:
            print("Você ganhou: PAPEL venceu PEDRA !")
        elif pergunta == 2:
            print("Você perdeu! PEDRA venceu TESOURA !")
        else:
            print("Opção inválida - insira 0, 1 ou 2")
        print("Opção PEDRA escolhida pelo computador !")

                          
    elif maquina == 1:
        if pergunta == 0:
            print("Você perdeu! PAPEL venceu PEDRA")
        elif pergunta == 1:
            print("Empate! Os dois escolheram PAPEL !")
        elif pergunta == 2:
            print("Voce ganhou! TESOURA vence PAPEL ! ")
        else:
            print("Opção inválida - insira 0, 1 ou 2")
        print("Opção PAPEL escolhida pelo computador")
            
    elif maquina == 2:
        if pergunta == 0:
            print("Você ganhou! PEDRA venceu TESOURA!")
        elif pergunta == 1:
            print("Você perdeu! TESOURA venceu PAPEL!")
        elif pergunta == 2:
            print("Empate! Os dois escolheram TESOURA!")
        else:
            print("Opção inválida - insira 0, 1 ou 2")
        print("Opção TESOURA escolhida pelo computador")

    else:
        print("Opção inválida")

inicia_jogo()

    