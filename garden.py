#garden 

import spacy

# this is the english language model for spaCy
nlp = spacy.load("en_core_web_sm")

garden_path_sentences = [
    "The complex houses married and single soldiers and their families.", 
    "The horse raced past the barn fell.", 
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi."
    ]

# function to tokenize each sentance in the list and to preform NER
def process_sentence(garden_path_sentences):
    
    doc = nlp(garden_path_sentences)
    processed_entities = []

    for token in doc:
        processed_entities.append((token.text, token.pos_, token.ent_type_))

    return processed_entities

# process each sentence in the list
processed_sentences = []
for sentence in garden_path_sentences:
    processed_entities = process_sentence(sentence)
    processed_sentences.append(processed_entities)

# print results 
for sentence, entities in zip(garden_path_sentences, processed_sentences):
    print("Sentence:", sentence)
    for text, pos, label in entities:
        print(f"\t- {text} ({pos}, {label})")

print(spacy.explain("ADP"))
'''
ADP was explained as adposition. The defenition of this means a word that is used to show 
the relationship between a noun / proboun and another word. I think the clasification is 
correct in the NER as it is used for words such as "in" and "of" in the last sentance. 
it also works in the correct meaning of the word within the garden sentance. 
'''

print(spacy.explain("AUX"))
'''
AUX is explained as auxiliary. The defenition of this means a helping verb. it helps express 
additional information about the main verb, like tense. In the last sentance, this clasification
is correct again because it is helping to difine the present tense. "The cotton clothing is made
of...". "is" was the AUX word that helps the main verb of made define its present tense. 
It could have been "will" or "was" however in the terms of this garden sentance, it works as "is".
'''