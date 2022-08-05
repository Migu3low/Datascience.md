from __future__ import division


def divisors(num):
    div = list([i for i in range(1, num + 1) if num % i == 0])
    return div

def run():
    num = int(input("Ingresa un numero: "))
    print(divisors(num))

if __name__ == '__main__':
    run()