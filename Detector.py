import os

def search_words(directory, word_file):
    # read words from file
    with open(word_file) as f:
        words = f.read().splitlines()
    for root, dirs, files in os.walk(directory):
        for file in files:
            with open(os.path.join(root, file), 'r') as f:
                content = f.read()
                for word in words:
                    if word in content:
                        print('Keylogging behavior detected')

search_words('/home/kali','sear.txt')
