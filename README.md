# Taller 1
### __Desarrollado por: The Bug Hunting Pythons.__
* Integrantes: Jana Rubiano Hurtado, Samuel Villamizar y Ana Maria De Felipe Briñez. 
---

Bienvenidos a este repostorio en el cual explicaremos el desarrollo de códigos en Python para resolver problemas planteados en la clase de programación. 

Comenzaremos con el primer punto. 

1. **Realice el quiz Python Beginner Quiz (20 preguntas) y adjunte pantallazo con el resultado.**

Para este punto todos los miembros del equipo realizamos el Quiz. 

* Jana Rubiano Hurtado. 

<img width="708" alt="Screenshot 2023-03-06 184525" src="https://user-images.githubusercontent.com/124604730/223298953-3f1bc4f2-2b37-4843-b152-106a109127ff.png">

* Ana Maria De Felipe Briñez.

[![Taller-1-Quiz.jpg](https://i.postimg.cc/6qKLws6M/Taller-1-Quiz.jpg)](https://postimg.cc/N9Nr7zHX)

* Samuel Villamizar.

![Captura de pantalla 2023-03-02 222953](https://user-images.githubusercontent.com/124604126/224580950-9e159f7e-963c-4f96-96ec-525d1a84eb6b.png)


---

Ahora bien, continuaremos con el siguiente punto. 

2. **Realice un programa que lea tres números reales y determine cuál es el mayor.** 

¿Qué quiere decir esto? Que debemos desarrollar un código que cuando el usuario ingrese 3 números reales, este mediante los simbolos mayor que (>) y menor que(<), permita determinar cual número es mayor. 

¿Bueno y ahora por donde se empieza? Para comenzar nombraremos las variables que permitirán el desarrollo del código y usando "input()", dejaremos al usuario ingresar el valor númerico que este desee. Y con "int" y "float" estableceremos el tipo de número, es decir, si un número entero (con "int") o un número real (con "float"). 

```python
# Ejemplo. 
# a, b y c: Es una variable y representa un número real cualquiera. (Decisión del usuario). 

a: float = (input("Ingrese número: "))
b: float = (input("Ingrese número: "))
c: float = (input("Ingrese número: "))
```

Lo siguiente es establecer las comparciones. 

Ya solo queda indicar que número es mayor que otro con los simbolos mencionados anteriormente (>, <). 

```python
# Ejemplo. 

if a > b and a > c # And es un condicional que hace verdadera una afirmación si se cumplen 2 condiciones.
                  # En este caso estariamos condicionando a que "a" debe ser mayor que "b" y "c". para que se cumpla el if. 
                   # y si se cumple la condición, mediante el código "print()" nos enseñara lo que decidamos poner dentro de este. 
                  
if a > b and a > c
  print(str(a) + " Es el número mayor") # "str()" es un código que hace que en el "print()" se muestre que representa la varible. 
```
Y hacemos lo mismo sucesivamente para los demás casos. **(Revisar archivo adjunto: puntos pares taller 1.py)**



--- 

Avanzando con el desarrollo del taller continuamos con el punto 3. 

3. **Realice un programa que lea un número enteros y determine si es par o impar.**

Para el desarrollo de este punto básicamente necesitaremos que el usuario pueda ingresar sus valores numéricos enteros (explicado anteriormente) y mediante los operadores aritméticos estableceremos una relación entre los números pares e impares. 

Sabemos que los pares son aquellos números que son divisibles por 2, es decir, al dividirlos por 2, no dejan residuo, por lo que el operador aritmético modulo “%”, nos permitirá el desarrollo del código.  ¿Cómo haremos esto? Muy sencillo, estableceremos la siguiente operación. 

```python
a % 2 == 0   # Si se cumple esta condición, entonces "a" será un número par, si no es así, será un impar. 
```
Para este punto, adjuntaremos un diagrama que ilustre el proceso. 

[![Taller-1-punto-3.png](https://i.postimg.cc/8P45t22T/Taller-1-punto-3.png)](https://postimg.cc/F7fNKBF6)


Y bien, eso es todo por este lado. **(Revisar archivos adjunto: TAller impares. ipynb)**

---

El siguiente punto del taller, es el numeral 4 que consiste en lo siguiente. 

4. **Realice un programa que lea dos números reales y determine si el primero es múltiplo del segundo.**

Este punto cuenta con cierta similitud al punto anterior, pues básicamente utilizaremos la misma operación aritmética “%”, solo que esta vez, será entre 2 números que ingrese el usuario, ya que, nos piden conocer el múltiplo de un número y para saber el múltiplo de un número, solo debemos dividir al número entre el múltiplo y el residuo de esta operación debe ser cero. 

¿Y cómo desarrollaremos al código? Solo tendremos que establecer 2 variables, pedir al usuario que por medio del código “input” ingrese su número y operaremos esas variables. 

El siguiente diagrama ilustrara el proceso. **(Revisar archivo adjunto: puntos pares taller 1.py).**

[![Taller-1-punto-4.png](https://i.postimg.cc/jjZm1Xsw/Taller-1-punto-4.png)](https://postimg.cc/sBGTQ5Gs)

---

Ahora bien, continuaremos con el siguiente punto. 

5. **Realice un programa que lea tres números reales y determine si la suma de los dos primeros es mayor, menor o igual que el tercer número.** 

¿Qué quiere decir esto? Que debemos desarrollar un código que presente la operación aritmética de la suma “+”.  Donde pediremos al usuario ingresar 3 números. Después de esto, sumaremos 2 de los números y lo comparemos con el tercer número. 

```python
# Ejemplo

a = float(input("Ingrese el primer numero: ")) 
b = float(input("Ingrese el segundo numero: ")) 
c = float(input("Ingrese el tercer numero: ")) 
if a + b < c :
    print (a,"mas", b,"es menor que", c)
```

Y hacemos lo mismo sucesivamente para los demás casos. **(Revisar archivos adjunto: TAller impares. ipynb).**

---

Avanzando con el taller, el siguiente es el punto 6 el cual consiste en lo siguiente. 

6. **Escriba un programa que solicite al usuario una letra y determine si es una vocal o una consonante.**

Esta parte del taller varia un poco, pues ya no estamos utilizando números, sino para este caso utilizaremos letras y desarrollaremos un código que reconozca las vocales y las consonantes. 

¿Pero cómo lo haremos? Para esto, usaremos “str” y lo demás lo continuaremos como ya lo conocemos. 

```python
# Ejemplo

letra = str(input("Ingrese una letra (minuscula o mayuscula): "))  # Este código permitirá ingresar al usuario una letra. 
if letra == "a" or letra == "A": # Esto funciona tal como ya lo hemos visto, es decir, si el usario ingresa la letra a, el programa imprimira "letra es vocal"
    print("letra es vocal")
```
Y continuamos desarrollando el código de esta manera hasta completar todas las vocales. Y finalizamos con "else". 

```python
else:
    print("letra es consonante") # "Else hará que las demás letras que no sean vocales, impriman lo siguiente: "letra es consonante"
```

**(Revisar archivo adjunto: puntos pares taller 1.py)**

---

El siguiente punto del taller, es el numeral 7. 

7. **Escriba un programa que pida 5 números reales y calcule las siguientes operaciones:** 
* El promedio. 
* La mediana.
* El promedio multiplicativo. 
* Ordenar los números de forma ascendente. 
* Ordenar los números de forma descendente. 
* La potencia del mayor número elevado al menor número. 
* La raíz cúbica del menor número.

El siguiente punto es bastante extenso ya que tendremos que hacer varias comparaciones para llevar a cabo el código con éxito.  

Comenzaremos con el primer subpunto, calcular el promedio de los 5 números que ingrese el usuario. Para ello utilizaremos 2 operaciones aritméticas: suma y división y estableceremos el código de la siguiente manera. 

```python
f = a + b + c + d + e
g = f/5    # Recordemos que el promedio es la suma de todos los datos divido en el total de datos. 
print ("Media:",g)
```
Avanzaremos a los siguientes subpuntos, pues estos tienen en común un factor importante: el orden de los números. Para este tendremos que organizar los valores mediante los símbolos (> y <), esto nos permitirá ir desarrollándolos.

```Python
# Ejemplo. 
if a < b and a < c and a < d and a < e: 
  primertermino = a
elif b < a and b < c and b < d and b < e :
  primertermino = b
elif c < b and c < a and c < d and c < e :
    primertermino = c
elif d < b and d < c and d < a and d < e :
    primertermino = d
else :
    primertermino = e
```
Esto organizará los números, no obstante, el proceso es bastante largo pues necesitaremos definir cual número es el número mayor, que número le sigue, etc… (Nada más en el ejemplo apenas estamos definiendo el primer término, faltarían los demás con un proceso igual) 

Una vez ya tengamos todos los términos definidos, podremos imprimir los demás subpuntos. 
* Como calcular la mediana. 
```Python
print ("Mediana:",tercertermino) # Sabemos que la mediana consiste en organizar los términos y tomar el del medio. 
```
*  Promedio multiplicativo. 

```Python
h = (a*b*c*d*e)**0.2  # Consiste en multiplicar entre si todos los números y sacar la raíz. 
print ("Promedio Multiplicativo:",h)
```
* Ordenar los números de forma ascendente y ordenar los números de forma descendente
```Python
print (primertermino,"-",segundotermino,"-",tercertermino,"-",cuartotermino,"-",ultimotermino)
```
* La potencia del mayor número elevado al menor número y la raíz cúbica del menor número al primero. 
```Python
print (ultimotermino**primertermino)
print (primertermino**(1/3))
```
Como se puede evidenciar la importancia del código de este punto radica en que sepamos definir mediante los símbolos (< y >) cual número es mayor, que le sigue, etc… **(Revisar archivos adjunto: TAller impares. ipynb).** 

--- 

Ahora bien, continuaremos con el siguiente punto. 

8. **Escriba un programa al que se le ingrese la frecuencia de una onda en hz y como salida arroje en que parte del espectro electromagnético se encuentra.**

Para resolver el siguiente problema mediante un código necesitamos conocer en que espectro electromagnético se encuentran ciertos intervalos de ondas de frecuencia en Hz. Para ello, simplemente necesitaremos usar los símbolos (< y >) y definir los intervalos. 

```Python
if 1 <= f < 10**8:   # f, será la frecuencia en Hz que ingresará el usuario. 
  print("Ondas de radio")
elif 10**8 <= f <10**12  # "Elif" Permite que si no se cumple la condición previamente dada, pase a comprobar una nueva condición. 
  print("Microondas")
```

Y continuaremos haciendo lo mismo con los demás intervalos y su ubicación en el espectro electromagnético. **(Revisar archivo adjunto: puntos pares taller 1.py)**

---

El siguiente punto del taller, es el numeral 9. 

9. **Escriba un programa que reciba el nombre en minúsculas de un país de America y retorne la ciudad capital, si el país no pertenece al continente debe arrojar país no identificado.**

Para desarrollar el siguiente punto usaremos “lang”, mediante este podremos definir frases o palabras y demás que permitan que Python nos imprima un cometario cuando utilicemos dicha frase. 

```Python
lang = input("Escriba el nombre de un país de America (en minusculas) ")

if lang == "canadá" or lang == "canada":
  print("La capital de Canadá es Otawwa")
elif lang ==  "estados unidos" or lang == "usa": # 
  print("La capital de USA es Washington DC")
```
Y haremos lo mismo con los demás países de America. Para cerrar dicho código utilizaremos "else", este nos ayudara a que cuando alguien inserte un termino que no hayamos establecido con el "lang", arroje el siguiente cometario: 

```Python
else:
  print("País no identificado")
```
**(Revisar archivos adjunto: TAller impares. ipynb).** 

--- 

Finalmente, explicaremos el último punto del taller. 

10. **Escriba un programa que dada una distancia calcule:**
* El tiempo que le tomaría a la luz recorrer la distancia.
* El tiempo que le tomaría al sonido (en el aire) recorrer la distancia.
* El tiempo que le tomaría al vehículo comercial más veloz recorrer la distancia.
* El tiempo que le tomaría a Bolt recorrer la distancia.

Este como todos los puntos anteriores, pediremos al usuario ingresar un valor numérico, en este caso que el valor numérico corresponda a una distancia.  Y usaremos la fórmula para determinar el tiempo que tardaría en recorrer x objeto la distancia dada por el usuario a x velocidad (dada por los subpuntos). 

```Python
distance: float= float(input("Ingrese una distancia en metros: "))
print("La luz tardaría " + str(distance/3e8) + " segundos")  
# En esta parte el código “str(distance/3e8)” es la fórmula para calcular el tiempo: Tiempo= Distancia/Velocidad y el “3e8” equivale a la velocidad de la luz en km/s 
```
**(Revisar archivo adjunto: puntos pares taller 1.py)**

---

Y bien esto es todo por el momento. Recuerda dejar tu estrella a los mejores pythoneros cazadores de bugs. 
