NUM_COUNT = 100

words = [""]*100
words[3] = "Fizz"
words[5] = "Buzz"

for x in range(1, NUM_COUNT+1):
    out, word = "", ""
    for n in range(1, len(words)):
        if x%n == 0:
            word += words[n]
    print(f"{str(x).ljust(len(str(NUM_COUNT)), ' ')}: {word}")
