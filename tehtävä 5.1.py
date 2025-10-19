import random
while True:
    try:
        n = int(input("Kuinka monta arpakuutiota haluat heittää? "))
        if n < 0:
            print("Anna nollaa tai suurempi kokonaisluku.")
            continue
        break
    except ValueError:
        print("Anna kokonaisluku, esim. 3.")
summa = 0
for _ in range(n):
    summa += random.randint(1, 6)

print(f"Silmälukujen summa on {summa}.")