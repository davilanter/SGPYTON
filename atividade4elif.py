idade = int(input("Digite sua idade: "))
experiencia = input("digite sim se voce tem experiencia: ")
ancendentes_criminais = input("digite sim se voce tem ancendentes_criminais: ")
ensino_superior_completo = input(
    "digite sim se voce tem ensino_superior_completo: ")
indicado = input("digite sim se voce foi indicado: ")
if idade >= 18 and experiencia == "True" and ancendentes_criminais == "False":
    print("contratado")
elif experiencia == "False" and (ensino_superior_completo == "True" or indicado == "True") and ancendentes_criminais == "False":
    print("teremos uma entrevista")
else:
    print("SAI DA MINHA SALA!")
