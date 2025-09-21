luvut = []

while True:
    syote = input("Anna luku: ")
    if syote == "":
        break
    try:
        luku = float(syote)
        luvut.append(luku)
    except ValueError:
        print("anna numero.")

if luvut:
    print(f"Pienin luku: {min(luvut)}")
    print(f"Suurin luku: {max(luvut)}")
else:
    print("Et antanut lukua.")