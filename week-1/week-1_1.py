import random

print(random.random())

s = random.randint(1, 100)
print(s)

def get_n_random_numbers(n=10, min_ = -5, max_ = 5):
    numbers = []
    for i in range(n):
        number.appen(random.randint(min_, max_))
    return numbers
print(get_n_random_numbers())

#histogram
histgram_1 = [
    (-4,1),
    (-3,0),
    (-1,1),
    (0,2),
    (1,1),
    (3,1),
    (6,1),
    (8,1)
]

my_list = [4, -1, -2, 0, 2, -3, 0, -4, -3, 0, -4, -1, 3, -1, -4]

def my_frequency_with_dict(list):
    frequency_dict = {}
    for item in list:
        if(item in frequency_dict):
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    return frequency_dict

print(my_frequency_with_dict(my_list))

def my_frequency_with_list_of_tuples(list_1):
    frequency_list = []
    for i in range(len(list_1)):
        s = False
        for j in range(len(frequency_list)):
            if(list_1[i] == frequency_list[j][0]):
                frequency_list[j][1] += 1
                s = True
        if(s == False):
            frequency_list.append([list_1[i], 1])
    return frequency_list

my_list2 = [2,3,2,5,8,2,4,3,3,2,8,5,2,4,4,4,4,4]
res_1 = my_frequency_with_dict(my_list2)
res_2 = my_frequency_with_list_of_tuples(my_list2)
print(res_1)
print(res_2)

