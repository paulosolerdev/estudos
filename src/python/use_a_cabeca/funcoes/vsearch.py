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

def search4vowels(word):
    """Display any vowels found in a supplied word."""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    return found

print(search4vowels('Soler'))
print(search4vowels('Sky'))
print(search4vowels('Why'))
