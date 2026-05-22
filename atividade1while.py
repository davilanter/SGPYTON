numeroescolhido =4
numerosecreto = 5
while numerosecreto != numeroescolhido :
    numeroescolhido = int(input("digite seu numero: ")) 
    if numerosecreto < numeroescolhido :
        print("numero secreto e menor")
    elif numerosecreto == numeroescolhido :
        print("parabéns,você acertou")
    else:
        print("numero secreto e maior")
    
