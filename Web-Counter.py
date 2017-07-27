"""This program retrieves text from a URL, and a word of the user's choice. The program then returns the frequency of occurrence of this word in the URL's text."""

import re
import requests

def run(url, word1):

    new_url = requests.get(url, "headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}")
    freq={}
    total = []
    new_text = new_url.text
    new_sentences = new_text.split(".")

    for sentence in new_sentences:

        newsentence = sentence.lower().strip()
        wordlist = re.sub("[^a-z]", " ", newsentence)
        words = wordlist.split(' ')
        for word in words:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
    print("The word", "\'", word1, "\'", "occurs", freq[word1], "times.")

run("http://tedlappas.com/wp-content/uploads/2016/09/textfile.txt", 'the')
