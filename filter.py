def function(number):
    even_numbers_list = [0, 2, 4, 6, 8]
    if number in even_numbers_list:
        return True
    else:
        return False


def int_function(integer):
    if isinstance(integer, int):
        return True
    else:
        return False


numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
filtered_list = list(filter(function, numbers_list))
print(filtered_list)

print("Enter numbers : ")
# integer_list = list(input().split())
filter_list = list(filter(int_function, list(map(int, input().split()))))
print(filter_list)

print("Enter integers : ")
int_filter_list = list(filter(int, list(map(int, input().split()))))
print(int_filter_list)

sample_list = ["fjsd", "dsfklj", 5.9, 0, 87]
filter_sample_list = list(filter(int_function, sample_list))
print(filter_sample_list)
