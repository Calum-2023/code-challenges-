# Create a function to return which movies a user would watch next

import spacy

nlp = spacy.load('en_core_web_md')

# base film to compare other films with
base_move_to_compare = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."

# using a dictionary rather than a list as we need to be able to identify the most recommended movie
movie_list = {
    "Movie a": "When Hiccup discovers Toothless isn't the only Night Fury, he must seek 'The Hidden World', a secret Dragon Utopia before a hired tyrant named Grimmel finds it first.",
    "Movie b": "After the death of Superman, several new people present themselves as possible successors",
    "Movie c": "A darkness swirls at the center of a world-renowned dance company, one that will engulf the artistic director, an ambitious young dancer, and a grieving psychotherapist. Some will succumb to the nightmare. Others will finally wake up.",
    "Movie d": "A humorous take on Sir Arthur Conan Doyle's classic mysteries featuring Sherlock Holmes and Doctor Watson.",
    "Movie e": "A 16-year-old girl and her extended family are left reeling after her calculating grandmother unveils an array of secrets on her deathbed.",
    "Movie f": "In the last moments of World War II, a young German soldier fighting for survival finds a Nazi captain's uniform. Impersonating an officer, the man quickly takes on the monstrous identity of the perpetrators he is trying to escape from.",
    "Movie g": "The world at an end, a dying mother sends her young son on a quest to find the place that grants wishes.",
    "Movie h": "A musician helps a young singer and actress find fame, even as age and alcoholism send his own career into a downward spiral.",
    "Movie i": "Corporate analyst and single mom, Jen, tackles Christmas with a business-like approach until her uncle arrives with a handsome stranger in tow.",
    "Movie j": "Adapted from the bestselling novel by Madeleine St John, Ladies in Black is an alluring and tender-hearted comedy drama about the lives of a group of department store employees in 1959 Sydney."
}

base_film = nlp(base_move_to_compare)

# variables to store movie title and similarity score
highest_similarity = 0.0
recommended_movie = None

# for loop to compare movie list in dictionary with base film
for title, synopsis in movie_list.items():
    similarity = nlp(synopsis).similarity(base_film)
    print(f"{title}: {similarity}")

# loop to check if similarity is higher than the current value in the variable
    if similarity > highest_similarity:
        highest_similarity = similarity
        recommended_movie = title

print(f"Recommended movie: {recommended_movie} (Similarity: {highest_similarity:.2f})")


