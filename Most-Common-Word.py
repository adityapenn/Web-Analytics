def run(path):
    dict_of_words = {}
    input = open(path)
    for line in input:
        words = line.lower().strip().split(' ')
        for word in words:
            if word in dict_of_words.keys():
                dict_of_words[word] += 1
            else:
                dict_of_words[word] = 1
    new_dict = dict((v,k) for k,v in dict_of_words.items())
    print(new_dict[max(dict_of_words.values())].title(), 'is the most frequently occurring word in the given document.')
    for x in dict_of_words:
        print(x)
run('textfile.txt')