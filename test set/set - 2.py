# Q-1 – Write a Python program to input a sentence and a positive integer from the user. Perform the following tasks:
sentence = input("Enter a sentence: ")
number = input("Enter a positive integer: ")

words = sentence.split()
# 1.	Display all the words in the sentence which contain exactly 3 vowels.
print("\nWords containing exactly 3 vowels:")

for word in words:
    vowel_count = 0

    for ch in word.lower():
        if ch in "aeiou":
            vowel_count += 1

    if vowel_count == 3:
        print(word)
# 2.	Display the word(s) having the maximum number of distinct characters.
max_distinct = 0

for word in words:
    distinct_count = len(set(word.lower()))

    if distinct_count > max_distinct:
        max_distinct = distinct_count

print("\nMaximum distinct character count:", max_distinct)
print("Words having maximum distinct characters:")

for word in words:
    distinct_count = len(set(word.lower()))

    if distinct_count == max_distinct:
        print(word)
# 3.	Find the difference between the largest and smallest digit of the given number.
largest_digit = max(number)
smallest_digit = min(number)

difference = int(largest_digit) - int(smallest_digit)

print("\nDifference:", difference)
# 4.	Check whether the sum of the first and last digit of the number is equal to the sum of all the remaining digits.
first_digit = int(number[0])
last_digit = int(number[-1])

first_last_sum = first_digit + last_digit

remaining_sum = 0

for digit in number[1:-1]:
    remaining_sum += int(digit)

print("First + Last:", first_last_sum)
print("Remaining digits sum:", remaining_sum)

if first_last_sum == remaining_sum:
    print("Result: Equal")
else:
    print("Result: Not Equal")

# Q-2 –Write a Python program to input n positive integers from the user and store them in a list. Perform the following tasks:
n = int(input("Enter number of integers: "))

numbers = []

for i in range(n):
    number = input("Enter positive integer: ")
    numbers.append(number)
# 1.	Create a dictionary where:
# o	Key → Number
# o	Value → Number of even digits present in it
even_digit_dict = {}

for number in numbers:
    even_count = 0

    for digit in number:
        if int(digit) % 2 == 0:
            even_count += 1

    even_digit_dict[int(number)] = even_count

print("\nEven Digit Dictionary:")
print(even_digit_dict)
# 2.	Create a tuple containing all numbers whose first digit is equal to the last digit.
same_first_last = []

for number in numbers:
    if number[0] == number[-1]:
        same_first_last.append(int(number))

same_tuple = tuple(same_first_last)

print("\nNumbers with same first and last digit:")
print(same_tuple)
# 3.	Create a set containing all the even digits occurring in the given numbers.
even_digits = set()

for number in numbers:
    for digit in number:
        if int(digit) % 2 == 0:
            even_digits.add(int(digit))

print("\nSet of even digits:")
print(even_digits)
# 4.	Display the numbers whose digit sum is greater than the average digit sum of all the numbers.
digit_sums = []

for number in numbers:
    total = 0

    for digit in number:
        total += int(digit)

    digit_sums.append(total)

average_sum = sum(digit_sums) / len(digit_sums)

print("\nAverage digit sum:", average_sum)
print("Numbers greater than average digit sum:")

for i in range(len(numbers)):
    if digit_sums[i] > average_sum:
        print(numbers[i])
# 5.	Find and display the number(s) containing the maximum number of distinct digits.
max_distinct = 0

for number in numbers:
    distinct_count = len(set(number))

    if distinct_count > max_distinct:
        max_distinct = distinct_count

print("\nMaximum distinct digit count:", max_distinct)
print("Numbers with maximum distinct digits:")

for number in numbers:
    distinct_count = len(set(number))

    if distinct_count == max_distinct:
        print(number)

# Q-3 Write a Python program to accept details of n vehicles and create a dictionary in the following format:
vehicles = {
    101: ["Swift", "Car", 1800, "Available"],
    102: ["Activa", "Scooter", 700, "Rented"],
    103: ["Creta", "Car", 2500, "Available"],
    104: ["Bullet", "Bike", 1200, "Available"]
}
# Where:
# Key → Vehicle ID
# Value → [Vehicle Name, Vehicle Type, Rent per Day, Status]
# Perform the following tasks:
# 1.	Create a new dictionary where Vehicle ID is the key and value is a tuple containing:
# (Vehicle Name, Rent for 5 Days)
rent_dict = {}

for vehicle_id, details in vehicles.items():
    vehicle_name = details[0]
    rent_per_day = details[2]

    rent_for_5_days = rent_per_day * 5

    rent_dict[vehicle_id] = (
        vehicle_name,
        rent_for_5_days
    )

print("Rent Dictionary:")
print(rent_dict)
# 2.	Create a set containing all the different vehicle types.
vehicle_types = set()

for details in vehicles.values():
    vehicle_type = details[1]
    vehicle_types.add(vehicle_type)

print("\nDifferent Vehicle Types:")
print(vehicle_types)
# 3.	Display all vehicles which are "Available" and have rent less than ₹2000 per day.
print("\nAvailable vehicles with rent less than 2000:")

for vehicle_id, details in vehicles.items():
    vehicle_name = details[0]
    rent_per_day = details[2]
    status = details[3]

    if status == "Available" and rent_per_day < 2000:
        print(vehicle_id, vehicle_name, rent_per_day)
# 4.	Find and display the available vehicle having the highest rent per day.
highest_rent = 0
highest_vehicle = ""

for vehicle_id, details in vehicles.items():
    vehicle_name = details[0]
    rent_per_day = details[2]
    status = details[3]

    if status == "Available":
        if rent_per_day > highest_rent:
            highest_rent = rent_per_day
            highest_vehicle = vehicle_name

print("\nAvailable vehicle with highest rent:")
print(highest_vehicle, highest_rent)
# 5.	Count and display the number of vehicles that are "Available" and "Rented".
available_count = 0
rented_count = 0

for details in vehicles.values():
    status = details[3]

    if status == "Available":
        available_count += 1

    elif status == "Rented":
        rented_count += 1

print("\nAvailable vehicles:", available_count)
print("Rented vehicles:", rented_count)