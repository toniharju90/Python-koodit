leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

# Muunto
naula_per_leiviska = 20
luoti_per_naula = 32
gramma_per_luoti = 13.3

grammat = (leiviskat* naula_per_leiviska * luoti_per_naula * gramma_per_luoti
           +naulat + luoti_per_naula * gramma_per_luoti
           + naulat * luoti_per_naula * gramma_per_luoti+ luodit * gramma_per_luoti)


kilogrammat = int(grammat // 1000)
jaannos_grammat = grammat % 1000

print( "Massa nykymittojen mukaisesti on:")
print(f"{kilogrammat} kilogrammaa ja {jaannos_grammat:.2f} grammaa")


