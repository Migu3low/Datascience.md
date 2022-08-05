def divisors(num):
    div = [i for i in range(1, num + 1) if num % i == 0]
    return div

def run():
    num = input("Ingresa un numero: ")
    assert num.isnumeric(), "Debes ingresar un número positivo"
    print(divisors(int(num)))

if __name__ == '__main__':
    run()
    