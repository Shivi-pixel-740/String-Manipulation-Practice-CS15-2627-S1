string_to_process = "eggs,cheese,milk,bread,cereal"
items = string_to_process.split(",")
uppercase_items = []

for item in items:
    uppercase_items.append(item.upper())
    formatted_list = " | ".join(uppercase_items)

    print(formatted_list)

# Expected Output: "EGGS | CHEESE | MILK | BREAD | CEREAL"