print("Enter two numbers separated by spaces : ")
number1, number2 = map(int, input().split())
print(number1, number2)
print(type(number1))

print("Enter random numbers separated by spaces to make a list : ")
numbers_list = list(map(int, input().split()))
print(numbers_list)

integers_list = list(map(int, [9.7, 8, 7.6, 6, 4.4, 3, 1, 2, 0]))
print(integers_list)

print("Enter a sentence : ")
sentence = list(map(str.upper, input().split()))
print(sentence)
