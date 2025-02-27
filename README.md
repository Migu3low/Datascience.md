
# ***:+1: Python***
(Learning path)

### ***Operadores matematicos***
Suma Resta Multiplicacion Division Potenciacion Residuo
**Precedencia de operadores**
PEMDAS Parentesis Exponentes Multiplicacion Division Adicion Sustraccion
> Hallar raiz cuadrada  9 ** 0.5  

``` 
import math 
math.sqrt(9) 
```

Imagen de guia [lista de comandos](https://static.platzi.com/media/user_upload/referencia_python-08967f82-4367-4e5c-b532-da74f02bada5.jpg)

### ***Variables***
Reglas en el uso de identificadores de variable
No pueden empezar con un número.
Deben estar en minúsculas
Para separar las palabras usamos el guion bajo: _
Estas reglas son aplicadas al lenguaje Python, en otros lenguajes puede haber otras reglas.

### ***Tipos de datos***
- Texto str String "" 
- Flotantes que son decimales
- Enteros Int Integer
- Booleanos True False
> Convertir los tipos de datos: int() str() float() abs() bool() 

### ***Operadores logicos y de comparacion***
Conversor de monedas
Aplicacion de condicionales
```
edad = int(input("Escribe tu edad: "))
if edad > 17:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```
Ctrl + K + C - Comenta todo el código seleccionado.
Ctrl + K + U - Descomenta todo el código seleccionado.
Para emoji Inicio + .

## Creación de ambiente Virtual:

`python3 -m venv nombre_venv`

- Usualmente el nombre del ambiente virtual es venv.

Activación del ambiente virtual:

- Windows:

`.\venv\Scripts\activate`

- Unix o MacOS:

`source venv/bin/activate`

Desactivar el ambiente virtual:

`deactivate`

Crear un alias en linux/mac:

`alias nombre-alias="comando"`

`alias avenv=“source venv/bin/activate”``
