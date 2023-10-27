suffixes = ['s', 'es', 'ed', 'ing', 'ly', 'ny']

def stem_word(word):
    
    for suffix in suffixes:
        if word.endswith(suffix):
            word = word[:-len(suffix)]
    return word


def stem_sentence(sentence):
    
    words = sentence.split()
    stemmed_words = [stem_word(word) for word in words]
    stemmed_sentence = ' '.join(stemmed_words)
    return stemmed_sentence

def stem
text = "whats so funny about be a member of a famly groupchat? i am having so much fun with all my allies , I am not to cold hearted to anyone just I am an introvert person that all "
stemmed_sentence = stem_sentence(text)
print(stemmed_sentence)
