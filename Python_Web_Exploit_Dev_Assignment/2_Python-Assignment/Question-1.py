# Q.1 Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.

def generate_list_and_tuple(input_string):
    numbers_list = [int(x) for x in input_string.split(',')]
    numbers_tuple = tuple(numbers_list)
    return numbers_list, numbers_tuple

input_string = input("Enter a sequence of comma-separated numbers: ")
numbers_list, numbers_tuple = generate_list_and_tuple(input_string)
print("List:", numbers_list)
print("Tuple:", numbers_tuple)