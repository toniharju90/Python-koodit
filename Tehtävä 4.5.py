oikeatunnus = "python"
oikeasalasana = "rules"

yritykset = 0
max_yritykset = 5

while yritykset < max_yritykset:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
    yritykset += 1

    if tunnus == oikeatunnus and salasana == oikeasalasana:
        print("Tervetuloa")
        break
    else:
        print("Virheellinen käyttäjätunnus tai salasana.")

if yritykset == max_yritykset and not (tunnus == OIKA_TUNNUS and salasana == OIKA_SALASANA):
    print("Pääsy evätty")