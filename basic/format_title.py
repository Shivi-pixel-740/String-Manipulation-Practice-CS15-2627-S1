string_to_process = "t H e , T a L e :: O f , T w O :: c I t I e S"

parts = string_to_process.replace(",", "|").replace("::", "|").split("|")

formatted_words = []

for word in parts:
    formatted_words.append(word.replace(" ", "").title())

formatted_title = " ".join(formatted_words)

print(formatted_title)