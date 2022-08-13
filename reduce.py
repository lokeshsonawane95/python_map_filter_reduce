from functools import reduce

numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Addition of numbers_list : {}".format(reduce(lambda x, y: x + y, numbers_list)))

print("Greatest number is : {}".format(reduce(lambda x, y: x if x > y else y, numbers_list)))

print("Smallest number is : {}".format(reduce(lambda x, y: x if x < y else y, numbers_list)))
