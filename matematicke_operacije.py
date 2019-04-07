while True:
    try:
        broj = int(input("Unesi pozitivan broj: "))
        brojac = 0
    except ValueError:
        print("Pogreška! Nisi unio broj!")
        continue
    else:
        if broj > 0:
            print("Početna vrijednost: " + str(broj))
            break
        else:
            print("Pogreška! Unio si broj manji od 1!")

while broj >= 1:
    brojac += 1
    if broj == 2:
        broj = int(broj / 2)
        print("Krajnja vrijednost: " + str(broj) + ", broj koraka: " + str(brojac))
        break
    elif broj == 1:
        brojac -= 1
        print("Krajnja vrijednost: " + str(broj) + ", broj koraka: " + str(brojac))
        break
    elif broj % 2 == 0:
        broj = int(broj / 2)
        print("Slijedeća vrijednost: " + str(broj))
    else:
        broj = int(broj)* 3 + 1
        print("Slijedeća vrijednost: " + str(broj))