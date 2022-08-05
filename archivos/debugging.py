def divisors(num):
    div = [i for i in range(1, num + 1) if num % i == 0]
    return div

def run():
    try:
        num = int(input("Ingresa un numero: "))
        if num <= 0:
            raise ValueError("Ingresar número positivo")
        return print(divisors(num))
    except ValueError as negativo: 
        print(negativo)

if __name__ == '__main__':
    run()
    