# Estructuras de datos

## Metodos
Funcion para un tipo de dato particular

Métodos para trabajar con texto en Python
```variable.strip(): ```
El método strip eliminará todos los caracteres vacíos que pueda contener la variable

```variable.lower():``` 
El método lower convertirá a las letras en minúsculas.

```variable.upper(): ```
El método upper convertirá a las letras en mayúsculas.

```variable.capitalize(): ```
El método capitalize convertirá a la primera letra de la cadena de caracteres en mayúscula.

```variable.replace (‘o’, ‘a’): ```
El método replace remplazará un caracterer por otro. En este caso remplazará todas las ‘o’ por el caracter ‘a’.

```len(variable): ```
Te indica la longitud de la cadena de texto dentro de la variable en ese momento.

Índices:
Se escriben entre corchetes al lado de la variable y son apuntadores numéricos a cada caracter. Por ejemplo, para el nombre Facundo, cuando utilizamos la variable nombre[1], aparece la letra ‘a’, dado que dicha variable tiene almacenada en ese momento la cadena de caracteres ‘Facundo’ donde la ‘a’ es el segundo caracterer.

Aclaración: se comienza a contar caracteres desde el 0 (que es el primer número en informática). Siguiendo el ejemplo, la letra ‘F’ de ‘Facundo’ es el caracter número 0. Por ende, nombre[0], nos devolvería una F.

### :zap: Slice()

Se trabaja con los indices y parentesis (colon) [S:S:S] :point_right: (Stat, Stop, Step)

### Enter point
``` if _name_ == "_main_":```  Se indica a Python el inicio del programa .
## Ejemplo Palindromo
```
def palindromo(palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palindromo")
    else:
        print("No es palindromo")

if __name__ == "__main__":
    run()   
```
## Ciclo While For
Realizar codigo para comporbar que un numero es primo:
```
def run():
    number = int(input("Escribe un numero: "))
    for i in range(2, number+1):
        if number%i == 0:
            if i < number:
                print("No es numero primo")
                break
            else:
                print("Es numero primo")
        else:
            continue
  
if __name__ == "__main__":
    run()
  
```





