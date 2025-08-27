# def search4vowels(word):
#     """Display any vowels found in a supplied word."""
#     vowels = set('aeiou')
#     found = vowels.intersection(set(word))
#     for vowel in found:
#         print(f"{vowel}")

# def search4vowels(word):
#     """Display any vowels found in a supplied word."""
#     vowels = set('aeiou')
#     found = vowels.intersection(set(word))

#     return bool(found)

# def search4vowels(word):
#     """Display any vowels found in a supplied word."""
#     vowels = set('aeiou')
#     found = vowels.intersection(set(word))
#     return found

# def search4vowels(word:str) -> set:
#     """Return any vowels found in a supplied word."""
#     vowels = set('aeiou')
#     return vowels.intersection(set(word))


def search4vowels(phrase: str) -> set:
    """Return any vowels found in a supplied phrase."""
    vowels = set("aeiou")
    return vowels.intersection(set(phrase.lower()))


def search4letters(phrase: str, letters: str = "aeiou") -> set:
    return set(letters).intersection(set(phrase.lower()))

# if __name__ == "__main__":
#     print(search4letters("Hello World", "aeiou"))
#     print(search4letters("Paulo ama", "Susana"))

#print(search4vowels("Hello World"))
#print(search4vowels("Paulo ama Susana"))
