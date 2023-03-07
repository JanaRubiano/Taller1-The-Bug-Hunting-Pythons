# 2. Realice un programa que lea tres números reales y determine cuál es el mayor.
a = float
b = float
c = float
a = float(input("Ingrese un número: "))
b = float(input("Ingrese un número: "))
c = float(input("Ingrese un número: "))

if a < b and a < c:
    primero = a
elif b < a and b < c:
    primero = b
else:
    primero = c

if a > b and a > c:
    tercero = a
elif b > a and b > c:
    tercero = b
else:
    tercero = c
    
if primero < a < tercero:
    segundo = a
elif primero < b < tercero:
    segundo = b
else:
    segundo = c
    
print(primero, segundo, tercero)

# 4. Realice un programa que lea dos números reales y determine si el primero es múltiplo del segundo.
x:float
y:float
x = float(input("Ingrese un número: "))
y = float(input("Ingrese un número: "))

if x%y == 0:
    print(str(x) + " es multiplo de " + str(y))
else:
    print(str(x) + " no es multiplo de " + str(y))

# 6. Escriba un programa que solicite al usuario una letra y determine si es una vocal o una consonante.
letra:str
letra = str(input("Ingrese una letra (minuscula o mayuscula): "))
if letra == "a" or letra == "A":
    print("letra es vocal")
elif letra == "e" or letra == "E":
    print("letra es vocal")
elif letra == "i" or letra == "I":
    print("letra es vocal")
elif letra == "o" or letra == "O":
    print("letra es vocal")
elif letra == "u" or letra == "U":
    print("letra es vocal")
else:
    print("letra es consonante")
# 8. Escriba un programa al que se le ingrese la frecuencia de una onda en hz y
# como salida arroje en que parte del espectro electromagnético se encuentra.
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

# 10. Escriba un programa que dada una distancia retorne los segundos que tardarían: 
distance:float
distance = float(input("Ingrese una distancia en metros: "))
print("La luz tardaría " + str(distance/3e8) + " segundos")
print("El sonido tardaría " + str(distance/343) + " segundos viajando en el aire")
print("bugatti chiron super sport 300+ tardaría " + str(distance/136) + " segundos")
bolt = distance/12.4
print("Bolt tardaría " + str(bolt) + " segundos")
