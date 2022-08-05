def divisors(num):
    divisors = [i for i in range(1, num + 1) if num % i == 1]

def run():
    num = int(input("Ingresa un numero: "))
    print(divisors(num))

if __name__ == '__main__':
    run()