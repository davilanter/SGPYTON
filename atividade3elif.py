idade = int(input("Digite sua idade: "))
ingreso = input("Digite sim se voce tem ingreso: ")
vip = input("Digite sim se voce tem vip: ")
autorisacao_dos_pais = input("Digite sim se voce tem autorisacao : ")

if idade < 12 :
    print ("você não tem idade. não pode entrar")
elif idade >= 18 and ( ingreso == "sim"or vip == "sim" ):
    print ("pode entrar")
elif idade <  18 and autorisacao_dos_pais == "sim" and (ingreso == "sim" or vip == "sim "):
    print ("pode entrar")
elif  vip == "sim" :
    print ("bem vindo a sala vip")
else :
    print("você não pode entar")
