nota1 = int(input("Digite sua nota: "))
nota2 =  int(input("Digite sua nota: "))
nota3 = int(input("Digite sua nota: "))
media = (nota1 + nota2 + nota3) / 3

if media < 5 :
    print("que pena,reprovado")
elif media == 10 :
    print("otimo,perfeito")
else:
    print("aorovado")
