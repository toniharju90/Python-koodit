sukupuoli = input("Anna biologinen sukupuolesi (nainen/mies): ")
hemo = int(input("Anna hemoglobiiniarvosi (g/l): "))

if sukupuoli == "nainen":
    if hemo < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemo <= 175:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")

elif sukupuoli == "mies":
    if hemo < 134:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemo <= 195:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")

else:
    print("Virheellinen sukupuoli.")