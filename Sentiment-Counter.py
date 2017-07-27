def run(filepath):
    reviews = []
    rev = open(filepath)
    for line in rev:
        line.lower().strip().split('\n')
        reviews.append(line.strip())
    pos = open('positive-words.txt')
    pdict = []
    poswords = []
    pdict1 = dict()
    all = []
    lall = []
    for line in reviews:
        line2 = line.split(' ')
        all += line2
    for now in all:
        lall.append(now.lower())
    positive = open('positive-words.txt')
    for word in positive:
        poswords.append(word.strip())
    for words in lall:
        if words in poswords:
            pdict.append(words)
    print(pdict)
    for letter in pdict:
        if letter in pdict1:
            pdict1[letter] += 1
        if letter not in pdict1:
            pdict1[letter] = 1
    print(pdict1)
run("textfile.txt")
