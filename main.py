from collections import Counter
import fractions
string = "spsc"

c = Counter(string)
counted = c.most_common()

numberline = []

letters = []
for x in string:
    if x not in letters:
        letters.append(x)

for x in letters:
    freq = [item for item in counted if item[0] == x]
    numberline.append((fractions.Fraction(1/(len(string)/freq[0][1])), x))

print(numberline)

numberlineRange = (0, 1)
for letter in string:
    print(letter)
    freq = [item[0] for item in numberline if item[1] == letter][0]
    print(freq)


