def search4vowels():
    """Display any vowels found in an asked for word."""
    vowels = set('aeiou')
    word = input("Enter a word: ")
    found = vowels.intersection(set(word))
    for vowel in found:
        print(f"{vowel}")

search4vowels()
