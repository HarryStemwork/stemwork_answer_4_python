abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
front3 = abc[:3]
end23 = abc[3:]
subText = end23 + front3

word = input()
for char in word:
    print(subText[abc.index(char.upper())], end="")
