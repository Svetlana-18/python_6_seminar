# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Use comprehension.
# in
# 9

# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

# in
# 10

# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]


from random import sample


def element_search(num):
    my_list = sample(range(num * 3), num)
    print(my_list)
    return [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]


number = (int(input('введите длину списка: ')))
res = element_search(number)
print(res)


# my_list = [15, 2, 3, 1, 7, 5, 4, 10]
# my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
# print(f'Исходный список {my_list}')
# print(f'Новый список {my_new_list}')
