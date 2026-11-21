contagem_pontos = 0
#1Pede o nome do jogador
name = input("Qual o seu nome?")

#2Faz 5 perguntas de múltipla escolha (a, b, c) sobre TI.
#Pergunta 1
for i in range(2):
    resposta = input("O que significa CPU? \n a) Central Processing Unit \n b) Computer Personal Unit \n c) Central Program Utility \nR:").lower()
    if resposta == "a":
        print("Voce acertou\n")
        contagem_pontos += 1
        print(f"Voce Tem {contagem_pontos} ponto atualmente\n")
        break
    else:
        print("Voce errou\n")
print("Proxima pergunta \n")

#Pergunta 2
for i in range(2):
    resposta = input("Qual destes dispositivos é de armazenamento? \n a) Placa de vídeo \n b) SSD \n c) Fonte de alimentação \nR:").lower()
    if resposta == "b":
        print("Voce acertou\n")
        contagem_pontos += 1
        print(f"Voce Tem {contagem_pontos} pontos atualmente \n")
        break
    else:
        print("Voce errou\n")
print("Proxima pergunta \n")


#Pergunta 3
for i in range(2):
    resposta = input("Qual protocolo é usado para acessar sites de forma segura? \n a) FTP \n b) SMTP \n c) HTTPS \nR:").lower()
    if resposta == "c":
        print("Voce acertou\n")
        contagem_pontos += 1
        print(f"Voce Tem {contagem_pontos} pontos atualmente \n")
        break
    else:
        print("Voce errou\n")
print("Proxima pergunta \n")

#Pergunta 4
for i in range(2):
    resposta = input("O que a memória RAM faz? \n a) Guarda dados temporários enquanto o computador está em uso \n b) Guarda arquivos permanentemente \n c) Conecta o computador à internet \nR:").lower()
    if resposta == "a":
        print("Voce acertou\n")
        contagem_pontos += 1
        print(f"Voce Tem {contagem_pontos} pontos atualmente \n")
        break
    else:
        print("Voce errou\n")
print("Proxima pergunta \n")

#Pergunta 5
for i in range(2):
    resposta = input("Qual comando do Windows mostra o endereço IP do computador? \n a) ping \n b) ipconfig \n c) format \nR:").lower()
    if resposta == "b":
        print("Voce acertou\n")
        contagem_pontos += 1
        print(f"Voce Tem {contagem_pontos} pontos atualmente \n")
        break
    else:
        print("Voce errou\n")

#5No final mostra a pontuação e uma mensagem:
print(f" {name} Sua pontuacao final nesse teste foi de {contagem_pontos} pontos")
if contagem_pontos <1:
    print(" Boa Sorte na proxima")
elif contagem_pontos <=3:
    print(" Voce esta em processo de aprendizado, parabens")
elif contagem_pontos <=5:
    print(" Parabens, voce demonstra dominio no assunto")
