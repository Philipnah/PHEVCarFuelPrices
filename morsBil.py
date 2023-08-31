# mors bils specs
KMperL = 20
KMperkW = 5

print("Programmet favoriserer benzin lidt!\n")

gasPrice = float(input("Benzin pris (kr/L): "))
elPrice = float(input("El pris (kr/kWh): "))

pricePerKMgas = gasPrice/KMperL
pricePerKMElectric = elPrice/KMperkW

print("\n-----------------------------")
print("Benzin: " + str(pricePerKMgas) + " kr/km")
print("El: " + str(pricePerKMElectric) + " kr/km")
print("-----------------------------\n")