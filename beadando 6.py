print ('Feladat 06!')

def get_int(szoveg,min, max):
    while True:
        try:
            ertek = int(input(szoveg))
        #ha nem számot adunk meg
        except ValueError:
            print("A megadott ertek nem egesz szám!")
            continue

        if ertek < min:
            print("Az ertek nem lehet kisebb mint a minumim érték!")
            continue
        elif ertek > max:
            print("Az ertek nagyobb mint a maximum érték!")
            continue
        else:
            break
    return ertek

def kombi_szamol(lst,max):
    #szamlalo kezdoertekadas
    c = 0
    #beadott szamok novekvo sorba rendezése
    lst.sort()
    for i in range(0,3):
        for j in range(0,3):
            for k in range(0,3):
                v = (lst[i]*100+lst[j]*10+ lst[k])
                if v >= max:
                    return c
                print(v)
                c+=1
    return c

max_ertek = get_int("Kérem adjon meg egy számot (1 < N < 1000):",1, 1000)

lista = [9,0,4]
szamlalo = kombi_szamol(lista,max_ertek)

print("Az osszes kombinacio:", szamlalo)
