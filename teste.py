#programa distancia

origem = input("Cidade de origem: ")
destino = input("Cidade de destino: ")
distancia = float(input("Qual a distância em km? "))
velocidade = float(input("Quantos hm/h irá viajar? "))
tempo = distancia/velocidade*60
print(f" levará {tempo}h de {origem} à {destino}")