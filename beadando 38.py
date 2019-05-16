
import sys #a sys.exit = kilepes parancs miatt

# Globalis valtozok
# sorok szama
RowCount = 100
# szekek szama egy sorban
ColCount = 20
# Sorokat tartalmazo lista
# Minden sor egy String, a MoziLst egy String-eket tartalmazo lista
MoziLst = []




#    Egesz szam bekerese
#    Parameterek:
#       prompt:  A kiirando szoveg
#          min:  minimum ertek
#          max   maximum ertek
#   Visszatérési érték:
#    A magadott ertekeknek megfelelo Integer

def get_int(szoveg, min, max):
    while True:
        try:
            ertek = int(input(szoveg))
        except ValueError:
            print("A megadott ertek nem egesz szam!")
            continue

        if ertek < min:
            print("A megadott ertek kisebb mint a minimum!")
            continue
        elif ertek > max:
            print("A megadott ertek nagyobb mint a maximum!")
            continue
        else:
            break
    return ertek


#    Szöveg bekerese
#    Parameterek:
#       prompt:  A kiirando szoveg
#          min:  A szoveg min hossza
#          max:  A szoveg max hossza
#   Visszatérési érték:
#    A magadott ertekeknek megfelelo String

def get_str(szoveg, min=0, max=255):
    while True:
        str = input(szoveg)

        if len(str) < min:
            print("A megadott szoveg hossza kisebb, mint 2 karakter!")
            continue
        elif len(str) > max:
            print("A megadott szoveg hoosza nagyobb, mint 2 karakter!")
            continue
        else:
            break
    return str.upper()


#  Mozi struktura feltoltese ures (XX-XX-XX..) sorokkal

def mozi_init():
  #Egy ures sor
  strRow = "X" * 2 * ColCount
  #Mozi feltoltese ures sorokkal
  for r in range(RowCount):
      MoziLst.append(strRow)


#  Szoveg tordelese 2 hosszu elemekre
#   Parameter:
#       str:  A tordelendo szoveg
#
#  Visszateresi ertek:
#       2 karakter hosszú String-ek listája

def split_by_2(str):
    l = []
    while str:
        l.append(str[:2])
        str = str[2:]
    return l


#  szoveg beirasa adott helyre
#
#    Parameterek:
#         str : a beirando szoveg
#           r : a sor száma
#           c : a szek sorszama

def mozi_beir(str,r,c):
    strrow = MoziLst[r]
    pos = c*2
    strrow = strrow[:pos] + str + strrow[pos+2:]
    MoziLst[r] = strrow


#  Foglaltsag ellenorzese
#   Parameterek:
#        r:   a sor szama
#        c:   a szek szama
#   Visszateresi ertek:
#        True, ha szabad   (XX)
#       False, ha foglalt

def mozi_szabad(r,c):
    # A sor kivalasztasa
    rs = MoziLst[r]
    # a szek sorszama * 2
    pos = c * 2;
    # HA XX, akkor szabad
    if rs[pos:pos+2] == "XX":
        return True;
    return False


#  Foglalas keresese monogram alapjan
#   Parameter:
#            str:  keresendo szoveg
#   Visszateresi ertekek:
#    sor, oszlop pozicio

def mozi_keres(str):
    for r in range(RowCount):
        rs = MoziLst[r]
        pos = rs.find(str)
        if pos != -1:
            return ( r ,int(pos/2))
    return (-1, -1)


#  Mozi struktura megjelenitese

def menu_kiir():
  # szekek sorszamanak kiirasa, elso sor
  firstRow = "  "
  for c in range(1,ColCount+1):
       firstRow += " " +  "{:02d}".format(c)
  print(firstRow)


  for r in range(RowCount):
      s = MoziLst[r]
      strrow = "{:02d}".format(r+1) + "-" + '-'.join(split_by_2(s))
      print(strrow)
  main_menu()


#    Menu Modosit

def menu_modosit():
    print("------- Foglalas Modositasa ------------")
    mg = get_str("Kerem a monogrammot:",2,2)
    row = get_int("Kerem a sor számát:",1,RowCount)
    col = get_int("Kerem a szek számát:",1,ColCount)
    if mozi_szabad(row-1,col-1):
            #Ha az uj hely szabad
            (r,s) = mozi_keres(mg)
            #regi foglalas torlese
            if r != -1:
                mozi_beir("XX", r, s)
            #monogram beirasa az uj helyre
            mozi_beir(mg, row-1, col-1)
            print("A(z) ", mg, " lefoglalva az ", row, ". sor ", col, ". szekre")
    else:
        # Ha az uj hely nem szabad
        print("A hely mar foglalt!")
    main_menu()


#    Menu Foglalas Keresese

def menu_keres():
    print("-------  Foglalas keresese ------------")
    mg = get_str("Kerem a keresendo monogrammot:", 2, 2)
    (r,c) = mozi_keres(mg)
    if r == -1:
        print("Nincs ilyen neven foglalas!")
    else:
        print("A(z) ",r+1,". sor ", c+1, ". szek van foglalva")
    main_menu()


#    Menu Foglalas Torlese

def menu_torol():
    print("-------  Foglalas Torlese ------------")
    mg = get_str("Kerem a torlendo monogrammot:", 2, 2)
    (r,c) = mozi_keres(mg)
    #nem talalhato?
    if r == -1:
        print("Nincs ilyen neven foglalas!")
    else:
        #Ha megvan
        mozi_beir("XX",r,c)
        print("A foglalas torolve!")
    main_menu()


#    Mozi Fomenu


def main_menu():
    print()

    choice = input("""
                      M: Foglalas Modositasa
                      K: Foglalas Keresese
                      T: Foglalas Torlese
                      P: Foglalasok Megjelenitese
                      Q: Kilepes

                      Kerem Valasszon: """)

    if choice == "M" or choice =="m":
        menu_modosit()
    elif choice == "K" or choice =="k":
        menu_keres()
    elif choice== "T" or choice == "t":
        menu_torol()
    elif choice == "P" or choice == "p":
        menu_kiir()
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("Csak a menubol valasszon")
        main_menu()

# Foprogram
mozi_init()
main_menu()



