lista_alfabetica = ["Davi","Gabriel","João","Matheus"]
print("essa e a lista de alunos dessa turma: "+ str(lista_alfabetica))
index = int(input("digite o indice do aluno: "))
if index > len(lista_alfabetica) :
    print("ESCOLHA UM NÚMERO DENTRO DA LISTA SEU ANIMAL!")
elif index < 0 :
    print("ESCOLHA UM NÚMERO SEM SER NEGATIVO SEU ANIMAL!")
else :
    print(lista_alfabetica[index])
