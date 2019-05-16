def kitolt(c1, c2, sep, field_width):
    l = []
    for x in range(c2, c1, -1):
        l.append(chr(x))
    out = sep.join(l).rjust(field_width, sep)
    return sep.join([out, chr(c1), out[::-1]])





def get_int(prompt, min , max):
    while True:
        try:
            ertek = int(input(prompt))
        except ValueError:
            print("A megadott ertek nem egesz szám!")
            continue

        if ertek < min:
            print("Az ertek kisebb mint a minimum!")
            continue
        elif ertek > max:
            print("Az ertek nagyobb mint a maximum!")
            continue
        else:
            break
    return ertek

n = get_int("Kerem adja meg a betuszonyeg meretet (0 < N < 28):",1,27)

start = ord('a')
end = start + n - 1


#Egy sor szelessege
fw = ( end - start ) * 2 - 1

#felso haromszog
for e in range(end, start, -1):
  print(kitolt(e, end, '-', fw))

#also haromszog
for e in range(start, end + 1):
     print(kitolt(e, end, '-', fw))

