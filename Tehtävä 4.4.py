import random

salainen = random.randint(1, 10)

print("Arvaa kokonaisluku väliltä 1..10!")

while True:
    try:
        arvaus = int(input("Anna arvauksesi: "))
    except ValueError:
        print("Anna kokonaisluku.")
        continue

    if arvaus < salainen:
        print("Liian pieni arvaus.")
    elif arvaus > salainen:
        print("Liian suuri arvaus.")
    else:
        print("Oikein! Voitit pelin.")
        break