import random

try:
    N = int(input("Kuinka monta pistettä arvotaan? "))
except ValueError:
    print("Syötä kokonaisluku.")
    raise SystemExit(1)

if N <= 0:
    print("Pisteiden määrän tulee olla positiivinen kokonaisluku.")
    raise SystemExit(1)

n = 0

for _ in range(N):
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)
    if x*x + y*y < 1.0:
        n += 1

pi_likiarvo = 4 * n / N
print(f"Piin likiarvo (N = {N}): {pi_likiarvo}")