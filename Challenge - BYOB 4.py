# Set up a function to add prefix un to words 
def add_prefix_un (word):
    return 'un' + word

# Set up a function to add prefixes to word group
def make_word_groups (vocab_words):
    return (" : : " + vocab_words[0].join(vocab_words))

# Remove a suffix from a word 
def remove_suffix_ness (word):
    return word[ :-4] if word [-5] != 'i' else word[ :-5] + 'y'

# Extract and transform a word 
def adjective_to_verb (sentence, index):
    return sentence.split()[index].strip(".")+'en'

