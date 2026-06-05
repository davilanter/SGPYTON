import random

maximo = int(input("vamos adivinhar de 1 até que numero? "))
chances = int(input("vamos ter quantas chances de acertar? "))
numerosecreto = random.randint(1,maximo)
numeroescolhido = 0

while numerosecreto != numeroescolhido and chances != 0 :

    numeroescolhido = int(input("digite seu numero: ")) 

    if numerosecreto < numeroescolhido :
        print("numero secreto e menor")
        chances = chances -1
    elif numerosecreto == numeroescolhido :
        print("parabéns,você acertou")
    else:
        print("numero secreto e maior")
        chances = chances -1
    
    if chances == 0 :
        print("infelizmente suas chances acabaram ")
