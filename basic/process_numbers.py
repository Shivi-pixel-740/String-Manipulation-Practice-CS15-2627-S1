string_to_process = "  18,27,35,20  "
cleaned_numbers = string_to_process.strip()
number_parts = cleaned_numbers.split(",")
numbers = []

for number in number_parts:
    numbers.append(int(number))
    total = sum(numbers)
    average = total / len(numbers)
    print("Total:", total)
    print("Average:", average)

# Expected Output:
# "Total: 100"
# "Average: 25.0"