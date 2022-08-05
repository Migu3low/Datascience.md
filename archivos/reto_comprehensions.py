def run():

    # list = [i for i in range(1,100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    # print(list)

    # dict ={}
    # for key in range(1,101):
    #     if key % 3 != 0:
    #         dict[key] = key**3
    
    
    dict = {i: round(i**0.5,2) for i in range(1,1001)}
    
    print(dict)

if __name__ == '__main__':
    run()