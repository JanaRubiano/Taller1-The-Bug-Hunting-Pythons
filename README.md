# Taller 1. 
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



---

Ahora bien, continuaremos con el siguiente punto. 

2. **Realice un programa que lea tres números reales y determine cuál es el mayor.** 

¿Qué quiere decir esto? Que debemos desarrollar un código que cuando el usuario ingrese 3 números reales, este mediante los simbolos mayor que (>) y menor que(<), permita determinar cual número es mayor. 

¿Bueno y ahora por donde se empieza? Para comenzar nombraremos las variables que permitirán el desarrollo del código y usando "input()", dejaremos al usuario ingresar el valor númerico que este desee. Y con "int" y "float" estableceremos el tipo de número, es decir, si un número entero (con "int") o un número real (con "float"). 

```pseudocodigo
Ejemplo. 
# a, b y c: Es una variable y representa un número real cualquiera. (Decisión del usuario). 
a: float = (input("Ingrese número: "))
b: float = (input("Ingrese número: "))
c: float = (input("Ingrese número: "))
```

Perfecto, lo siguiente es establecer las comparciones. 

Ya solo queda indicar que número es mayor que otro con los simbolos mencionados anteriormente (>, <). 

```pseudocodigo
Ejemplo. 
if a > b and a > c # And es un condicional que hace verdadera una afirmación si se cumplen 2 condiciones.
                  En este caso estariamos condicionando a que "a" debe ser mayor que "b" y "c". para que se cumpla el if. 
                  y si se cumple la condición, mediante el código "print()" nos enseñara lo que decidamos poner dentro de este. 
                  
if a > b and a > c
  print(str(a) + " Es el número mayor") # "str()" es un código que hace que en el "print()" se muestre que representa la varible. 
```
Y hacemos lo mismo sucesivamente para los demás casos. Adjuntaremos el archivo del desarrollo. 

--- 

Avanzando con el desarrollo del taller continuamos con el punto 3. 

3. **Realice un programa que lea un número enteros y determine si es par o impar.**

Para el desarrollo de este punto básicamente necesitaremos que el usuario pueda ingresar sus valores numéricos enteros (explicado anteriormente) y mediante los operadores aritméticos estableceremos una relación entre los números pares e impares. 

Sabemos que los pares son aquellos números que son divisibles por 2, es decir, al dividirlos por 2, no dejan residuo, por lo que el operador aritmético modulo “%”, nos permitirá el desarrollo del código.  ¿Cómo haremos esto? Muy sencillo, estableceremos la siguiente operación. 

```pseudocodigo
a % 2 == 0   #Si se cumple esta condición, entonces a será un número par, si no es así, será un impar. 
```
