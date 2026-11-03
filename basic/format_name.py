string_to_process = "   sMitH, aLeX    "
cleaned_name = string_to_process.strip()
name_parts = cleaned_name.split(",")
last_name = name_parts[0].strip().title()
first_name = name_parts[1].strip().title()
print(first_name + " " + last_name)
