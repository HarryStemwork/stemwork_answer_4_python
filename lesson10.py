abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
front3 = [:3]
end23 = [3:]
subText = end23 + front3
encryptDict = dict(zip(subText,abc))

word = input()
cipher = []
for char in word:
    newChar = encryptDict[char]
    cipher.append(newChar)

cipherText = "".join(cipher)

print(f"Origial Word: {word}")
print(f"Encrypted Word: {cipherText}")
