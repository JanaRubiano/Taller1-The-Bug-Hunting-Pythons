# Taller 1. 
### __Desarrollado por: The Bug Hunting Pythons.__
* Integrantes: Jana Rubiano Hurtado, Samuel Villamizar y Ana Maria De Felipe Briñez. 
---

Bienvenidos a este repostorio en el cual explicaremos el desarrollo de códigos en Python para resolver problemas planteados en la clase de programación. 

Comenzaremos con el primer punto

1. **Realice el quiz Python Beginner Quiz (20 preguntas) y adjunte pantallazo con el resultado.**

Para este punto todos los miembros del equipo realizamos el Quiz, discutiendo las posibles respuesta y el porqué de estas. 


(Jana Rubiano)

<img width="708" alt="Screenshot 2023-03-06 184525" src="https://user-images.githubusercontent.com/124604730/223298953-3f1bc4f2-2b37-4843-b152-106a109127ff.png">

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
