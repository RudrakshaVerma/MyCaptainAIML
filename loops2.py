def positive_numbers_in_range(input_list):
    positive_numbers = [num for num in input_list if num > 0]
    return positive_numbers

# Input list
list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]

# Output
output_list1 = positive_numbers_in_range(list1)
output_list2 = positive_numbers_in_range(list2)

print("Input: list1 =", list1, "Output:", output_list1)
print("Input: list2 =", list2, "Output:", output_list2)
