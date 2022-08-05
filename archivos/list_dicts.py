def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Facundo", "lastname": "Garcia" }

    super_list = [
        {"fistname": "Facundo", "lastname": "Garcia"},
        {"fistname": "Miguel", "lastname": "Sanchez"},
        {"fistname": "Pepe", "lastname": "Rodel"},
        {"firstname": "Susana", "lastname": "Martinez"},
        {"firstname": "Jose", "lastname": "Garcia"}
    ]

    for values in super_list:
        for key, value in values.items():
            print(f'{key} - {value}')


    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, 2, 0, 1, 2],
        "floatings_nums": [1.1 ,4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

if __name__ == '__main__':
    run()