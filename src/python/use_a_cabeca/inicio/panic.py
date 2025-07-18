# phrase = "Don't panic!"
# plist = list(phrase)
# print(phrase)
# print(plist)

# for i in range(4):
#     plist.pop()
# print(plist)

# plist.pop(0)
# print(plist)

# plist.remove("'")
# print(plist)

# plist.extend([plist.pop(), plist.pop()])
# print(plist)

# plist.insert(2, plist.pop(3))
# print(plist)

# new_phrase = ''.join(plist)
# print(new_phrase)

#=======================================================#

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

new_phrase = ''.join(plist[1:3])
new_phrase = ''.join([plist[1], plist[2], plist[5], plist[4], plist[3]])
print(plist)
print(new_phrase)

new_phrase = ''.join([plist[1], plist[2], plist[5], plist[7], plist[6], plist[4]])
print(plist)
print(new_phrase)
