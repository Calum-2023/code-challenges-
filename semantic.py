import spacy
from itertools import product

nlp = spacy.load('en_core_web_md')

word_1 = nlp("cat")
word_2 = nlp("monkey")
word_3 = nlp("banana")

print(word_1.similarity(word_2))
print(word_3.similarity(word_2))
print(word_3.similarity(word_1))

# it is interesting that the two words with the most similarities are the most different words
# in terms of format such as number of letters however they are the most similar as both are 
# animals. This shows that the process is picking up what the animals are and that they are 
# different to the 3rd food item

tokens = nlp('cat apple money banana')
token_pairs = product(tokens, repeat=2)

sentance_to_compare = "Why is my cat on the car"

sentences = [
    "Where did my dog go",
    "Hello, there is my car",
    "Ive lost my car in my car",
    "Id like my board back",
    "I will name my dog Diana"
    ]

model_sentence = nlp(sentance_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + "-" + str(similarity))