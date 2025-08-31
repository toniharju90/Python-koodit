import random



# 0-9
kolminumero_koodi = "".join(str(random.randint(0, 9)) for _ in range(3))




# 1-6
nelinumeroinen_koodi = "".join(str(random.randint(1, 6)) for _ in range(4))






print("Kolminumeroinen koodi (0–9):", kolminumero_koodi)



print("Nelinumeroinen koodi (1–6):", nelinumeroinen_koodi)