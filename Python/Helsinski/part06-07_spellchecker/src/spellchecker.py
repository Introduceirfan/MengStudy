# write your solution here
teks_benar = []
with open("wordlist.txt") as new_file:
    for line in new_file:
        teks_benar.append(line.strip().lower())


input_text = str(input("Write text: "))
list_text = input_text.split()

result = []
for text in list_text:
    if text.lower() in teks_benar:
        result.append(text)
    else:
        result.append(f"*{text}*")

print(" ".join(result))