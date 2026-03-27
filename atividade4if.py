facas = 10
balas_de_armas = 10
dano_facas = 67
dano_balas_de_armas = 61
vida_do_inimigo = 100
vida_do_heroi = 99
print("começou a luta CLT")

vida_do_inimigo -= facas * dano_facas
if vida_do_inimigo < 1 :
    print("o inimigo foi de atacante do Vasco")
else:
    print("o calvo não morreu")
    
vida_do_heroi -= balas_de_armas  * dano_balas_de_armas 

if vida_do_heroi < 1 :
    print("F")
else:
    print("eu não desisto facil...")
