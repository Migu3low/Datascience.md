def run():
    # list = []
    # for i in range(1,101):
    #     if i**2%3 == 0:
    #         continue
    #     else:
    #         list.append(i**2)
    # print(list)

    squares = [i**2 for i in range(1,101) if i % 3 !=0]
    print(squares)

if __name__ == '__main__':
    run()