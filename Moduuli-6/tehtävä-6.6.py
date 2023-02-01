import math

def pizza_hinta(halkaisija, hinta):
    sade = halkaisija / 2
    pintaAla = math.pi * (sade ** 2)
    return hinta / pintaAla

def main():
    pizza1_halkaisija = float(input("Anna ensimmäisen pizzan halkaisija (cm): "))
    pizza1_hinta = float(input("Anna ensimmäisen pizzan hinta (€): "))
    pizza2_halkaisija = float(input("Anna toisen pizzan halkaisija (cm): "))
    pizza2_hinta = float(input("Anna toisen pizzan hinta (€): "))

    pizza1_hinta = pizza_hinta(pizza1_halkaisija, pizza1_hinta)
    pizza2_hinta = pizza_hinta(pizza2_halkaisija, pizza2_hinta)

    if pizza1_hinta < pizza2_hinta:
        print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
    elif pizza2_hinta < pizza1_hinta:
        print("Toinen pizza antaa paremman vastineen rahalle.")
    else:
        print("Molemmat pizzat antavat yhtä hyvän vastineen rahalle.")

main()