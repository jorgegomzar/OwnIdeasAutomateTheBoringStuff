notas = []
print("Vamos a calcular la media, pulsa solo ENTER para finalizar")
while(True):
    n = input("Nota: ")
    if(n == ''):
        break
    notas.append(n)

media = 0
for n in notas:
    media = media + float(n)
media = media / len(notas)

print("Nota media = " + str(media))