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

## 👇: Herencia

_DRY: Don´t repeat yourselft_
Lineas de codigo duplicada. Aplica a toda pieza. 
Reutilización nuevas clases a partir de otras. Clase más general. 
Jerarquía: Padre (Superclase)e hijo (subclases)
Tener una abstracción general con elementos en común.

### 🌠Método Constructor e Instanciar
Dar vida a los objetos en memoria cada lenguaje tiene sus palabras reservadas:
_this or new (Java, JavaScript and PHP) or selft(Python)_

1. Se inicia el constructor, parámetros obligatorios para crear la clase.
2. Se definene éstos parámetros (pasar de manera global a local con **_This_**)
### Ejemplo en Java en la clase Car:
```
package Java;

public class Car {
    Integer id;
    String license;
    Account driver;
    Integer passenger;

    public Car(String license, Account driver) {
        this.license = license;
        this.driver = driver;
    }

    void printDataCar() {
        System.out.println("License: " + license + " Name: " + driver.name);
    }
}
```
Ahora en la Clase Main se llama la clase con new:
```
package Java;

class Main {
    public static void main(String[] args) {
        System.out.println("Hola Mundo");
        Car car = new Car("AMQ235", new Account("Miguel Sanchez", "102388879"));
        car.passenger = 5;
        car.printDataCar();
    }
}
```

### Ejemplo en Python clase Account:

El constructor con __init__ y parametros con _self._:
```
class Account:
    id = int
    name = str
    document = str
    email = str
    password = str

    def __init__(self, name, document):
        self.name = name
        self.document = document
```
EL main se ve así:
```
from car import Car
from account import Account

if __name__ == "__main__":
    print("Hola Mundo")

    car = Car("MPW114", Account("Miguel Sanchez", "1023887888") )
    print(vars(car))
    print(vars(car.driver))
```
### Ejemplo en PHP:
Se utiliza la herencia con _require_once_ el constructor con _ _construct()_
Luego para la herencia se utiliza _parent::_construct()_

```
<?php
require_once("account.php");
class Car {
    public $id;
    public $license;
    public $driver;
    public $passenger;

    public function _construct($license, $driver) {
        $this->license = $license;
        $this->driver = $driver;
    }

    public function printDataCar(){
        echo "Licensi: $this->license Driver: " .$this->driver;
    }

}
```
## Encapsulamiento
Es hacer que los datos sean inviolables, inalterable o hacer que se esconda, cuando se le asigne un Modificador de Acceso.
.
Modificadores de Acceso:

Public: Es el mas permisivos de todos, Accede a todo.
Protected: Podrá ser accedido por la clase, paquetes y subclases.
Default: Permite el acceso a nivel de clses de internas y paquetes (No podremos ver las herencias si ha detener (Osea subclases))
Private: Solo podrá ser modificado dentro de la clase.








