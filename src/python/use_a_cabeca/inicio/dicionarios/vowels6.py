vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Digite uma palavra: ")

found = {}

for letter in word:
    if letter in vowels:
        if letter in found:
            found.setdefault(letter, 0)
            found[letter] += 1
        else:
            found[letter] = 1

for k, v in sorted(found.items()):
    print(f"{k} was found {v} time(s).")
