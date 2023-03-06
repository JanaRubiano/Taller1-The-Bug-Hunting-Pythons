f:float
f = float(input("Ingrese una frecuencia en hz: "))
if f < 0:
    print("Frecuencia invalida, frecuancia negativa")
elif  1 <= f < 10**8:
    print("Ondas de Radio")
elif 10**8 <= f < 10**12:
    print("Microondas")
elif 10**12 <= f < 10**15:
    print("Infrarrojo")
elif 10**15 <= f < 10**16 :
    print("Luz visible")
elif 10**16 <= f < 10**18:
    print("Ultravioleta")
elif 10**18 <= f < 10**20:
    print("Rayos X")
elif 10**20 <= f < 10**24:
    print("Radición Gamma")
else:
    print("Frecuancia invalida, fuera de rango")