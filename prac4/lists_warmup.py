numbers = ["10", 1, 4, 1, 5, 9, 1]
print(numbers[2:])
if 9 in numbers:
    print("9 is in the list")
else:
    print("9 is not in the list")

# Then use the Python console to see if you were correct.

# numbers[0] - 3
# numbers[-1] - 2
# numbers[3] - 1
# numbers[:-1] - [3, 1, 4, 1, 5, 9]
# numbers[3:4] - [1]
# 5 in numbers - True
# 7 in numbers - False
# "3" in numbers - False
# numbers + [6, 5, 3] - [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]