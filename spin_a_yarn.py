words = []
for i in range(1, 11):
    data = str(input("Enter some adjectives preposition or nouns: "))
    words.append(data)
a = words[0]
b = words[1]
c = words[2]
d = words[3]
e = words[4]
f = words[5]
g = words[6]
h = words[7]
i = words[8]
j = words[9]

story = "Doris’ balcony " + a + " toward the sea. She is in a high rise looking down at birds.\n" \
        " Gulls " +b+ " and " +c+ " north to the next resort. All that’s left now are " +d+ " on \n" \
        "the "+e+". They scavenge through the purpling decorative cabbage. She hasn’t seen a \n" \
        "pelican yet, just the same birds she came here to get away from. They look like\n " +f+ \
        " cataracts in a kale eyeball. She sees a buried "+g+ " with "+h+ " for pectorals. He struggles\n" \
        " to emerge from beneath the sodden "+i+ " sand, beaten down by so many "+j+ " dog walkers.\n" \
        " He has his eye on her."
print(story)
