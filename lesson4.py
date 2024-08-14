
song = """Old MacDonald had a farm,
E I E I O
And on that farm he had a cow,
E I E I O
With a moo moo here and a moo moo there,
Here a moo, there a moo, everywhere a moo moo.
Old MacDonald had a farm,
E I E I O
Old MacDonald had a farm,
E I E I O
And on that farm he had a duck,
E I E I O
With a quack quack here and a quack quack there,
Here a quack, there a quack, everywhere a quack quack.
Old MacDonald had a farm,
E I E I O
Old MacDonald had a farm,
E I E I O
And on that farm he had a horse,
E I E I O
With a neigh neigh here and a neigh neigh there,
Here a neigh, there a neigh, everywhere a neigh neigh.
Old MacDonald had a farm,
E I E I O
Old MacDonald had a farm,
E I E I O
And on that farm he had a pig,
E I E I O
With an oink oink here and an oink oink there,
Here an oink, there an oink, everywhere an oink oink.
Old MacDonald had a farm,
E I E I O
Old MacDonald had a farm,
E I E I O"""

split_word = song.split()
word_count = len(split_word)
word_input = input("Enter a word: ")
check_word = 0
for word in split_word:
    if word == word_input:
        check_word += 1
#or
check_word = len([word for word in split_word if word == word_input])

print(f"Song list: {split_word}")
print(f"Word count: {word_count}")
print(f"{word_input} have repeated {check_word} time")
