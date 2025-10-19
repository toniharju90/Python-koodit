n = int(input("Anna kokonaisluku: "))
if n < 2:
    print(f"{n} ei ole alkuluku.")
else:
    on_alkuluku = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            on_alkuluku = False
            break

    if on_alkuluku:
        print(f"{n} on alkuluku.")
    else:
        print(f"{n} ei ole alkuluku.")