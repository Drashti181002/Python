# (60)Sample string:
# 'w3resource' Expected output: • {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

s = "w3resource"
char_count2 = {}
for j in s:
    if  j in char_count2:
        char_count2[j] += 1
    else:
        char_count2[j] = 1
print(char_count2)
print