lista = []
sv = 0
while True:
    unos = input("unesite broj ili rijec \"Done\" ako ste zavrsili: ")
    if(unos == "Done"):
        break
    try:
        unos = int(unos)
        lista.append(unos)
        sv += unos
    except:
        print("Nije broj ni Done")

sv = sv/len(lista)
print("Min: "+str(min(lista)))
print("Max: "+str(max(lista)))
print("Duljina liste: " + str(len(lista)))
print("Srednja vrijednost: " + str(sv))
lista.sort()
print(lista)