import math

def perimetro_quadrato(lato):
    return 4 * lato

def perimetro_rettangolo(base, altezza):
    return 2 * (base + altezza)

def perimetro_cerchio(raggio):
    return 2 * math.pi * raggio

def calcola_perimetro():
    scelta = input("Scegli una figura tra queste (quadrato, rettangolo, cerchio): ")
    
    if scelta == "quadrato":
        lato = float(input("Inserire il lato del quadrato: "))
        print("Il perimetro del quadrato è:", perimetro_quadrato(lato))
    elif scelta == "rettangolo":
        base = float(input("Inserire la base del rettangolo: "))
        altezza = float(input("Inserire l'altezza del rettangolo: "))
        print("Il perimetro del rettangolo è:", perimetro_rettangolo(base, altezza))
    elif scelta == "cerchio":
        raggio = float(input("Inserisci il raggio del cerchio: "))
        print("Il perimetro del cerchio è:", perimetro_cerchio(raggio))
    else:
        print("Scelta inesistente")

calcola_perimetro()
