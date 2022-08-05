def run():
    list = []
    count = 1
    while len(list) < 101:
        list.append(count)
        count += 1

    for i in list[1:101]:
        if i < 101:
            number = i*i
            print(number)
        else:
            break

if __name__ == '__main__':
    run()