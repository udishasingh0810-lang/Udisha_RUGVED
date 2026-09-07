string = input("Enter a string: ")

sorted_string = ''.join(sorted(string))

print("Alphabetically sorted string:", sorted_string)

count = {}

for character in string:
    if character in count:
        count[character] += 1
    else:
        count[character] = 1

print("Character count:")

for character in sorted(count):
    print(character, ":", count[character])