import random



num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
num3 = random.randint(1, 10)





# 0-9
kolminumero_koodi = "".join(str(random.randint(0, 9)) for _ in range(3))




# 1-6
nelinumeroinen_koodi = "".join(str(random.randint(1, 6)) for _ in range(4))


print("kooodi:" num1, num2, num3)



print("Kolminumeroinen koodi (0–9):", kolminumero_koodi)



print("Nelinumeroinen koodi (1–6):", nelinumeroinen_koodi)