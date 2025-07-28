vowels = {'a', 'e', 'e', 'i', 'o', 'u', 'u'}
#print(vowels)

vowels2 = set('aeiou')
#print(vowels2)

word = 'hello'

u = vowels.union(set(word))

print(vowels)
print(u)
