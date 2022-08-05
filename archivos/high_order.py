my_list = [1, 2, 4, 5, 8, 9, 10, 11, 13]

odd = list(filter(lambda x: x%2 != 0, my_list))

# square = [i**2 for i in my_list]

square = list(map(lambda x: x**2, my_list)) 

print(square)
print(odd)

