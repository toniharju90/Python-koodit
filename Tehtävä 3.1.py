pituus = int(input("Anna kuhan pituus sentteinä: "))

alamitta = 37

if pituus < alamitta:
    puuttuu = alamitta - pituus
    print(f"Kuha on alamittainen, laske se takaisin järveen.")
    print(f"Se on {puuttuu} cm liian lyhyt.")
else:
    print("Kuha on tarpeeksi pitkä, voit pitää.")