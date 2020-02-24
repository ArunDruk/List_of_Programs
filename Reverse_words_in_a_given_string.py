####################################################################################################
# Reversing the words in a given string.
####################################################################################################

s = "i like this program very much"
words = s.split(' ')
L = []
for word in words:
    L.insert(0, word)

print("Reversed String:")
#print(L)
print(" ".join(L))