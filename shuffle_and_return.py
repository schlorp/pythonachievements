import random

def randomwoord(woord):
    return ''.join(random.sample(woord, len(woord)))

print(randomwoord("groote"))

print(randomwoord("rode"))

print(randomwoord("aap"))
