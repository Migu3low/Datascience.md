# 🎯  **Why** 

_Analizar, Modelar y Aplicar_
- Programar más rápído
- Encapsulamiento: oculta datos en código
- Abstracción: representar los objetos en código
- Herencia: Clase nueva derivada de otra
- Polimorfismo: mensajes con sintaxis igual a diferentes objetos

# :bucket: **What**

_Programación estructurada_
- Código muy largo
- Si algo falla, todo se rompe
- Difícil mantenimiento

# ▶️ **How**

_Análisis de problemas en forma de objetos_

> 👉 Paradigma: Teoría que suministra la base y modelo para resolver problemas
> - Clases
> - Propiedades
> - Métodos
> - Objetos

# 🐍 **Which**

_Lenguajes_

> - Python: fácil de usar, múltiples usos web, server side, data analysis, ML, .py
> - PHP: Interpretado, Pensado para la web .php
> - Java: Android, Server Side .java
> - JavaScript: interpretado, prototipos OO, pensados para la web .js
> - IDE Visual Studio Code.

## **Diagramas de modelado**

_OMT Object Modeling Techniques (1991)_
- Basado en objetos. Recuadro con atributos y métodos

_UML Unified Modeling Lenguage (1997)_
- Unificar las bases del OMT, modelar clases de usos, interaccionies, estados

## **Objetos**

Modelar problemas e identificar los objetos
- Físicos (User) o conceptuales (Session)
- Propiedades (atributos)
- Comportamientos (acciones)

## **Clase**

_Modelo, molde, módulo 👉 Abstracción _

## ➗**Modularidad**

División en partes más pequeñas.
- Reutilizar
- Evitar colapsos
- Mantenible
- Legibilidad
- Resolución rápida de problemas
- Archivos diferentes

## **Caso de aplicación**

Identificar objetos UBER:

- Celular 
- Punto A y Punto B // Ruta
- Uber X, Uber pool, Uber Black, Uber Van
- Usuario //, Driver
- Precio // card // paypal // cash
- Trip

Plasmarlo en UML:

- Rectangulo: Identidad / Estado / Comportamiento ()
- Java
```
class Person{
   String name = "";
   void walk() {}  
 } 
```
- Python
```
class Person:
   name = ""
   def walk():
     pass
```
- JavaScript
```
Person.prototype.walk = function(){}
```
- PHP
```
class Person{
  $name = "";
  funtion walk(){}
}
```

## Herencia

_DRY: Don´t repeat yourselft_
Lineas de codigo duplicada. Aplica a toda pieza. 
Reutilización nuevas clases a partir de otras. Clase más general. 
Jerarquía: Padre (Superclase)e hijo (subclases)
Tener una abstracción general con elementos en común.








