#Import spacy and load the language library
import spacy
nlp = spacy.load('en_core_web_md')
# Read in the movies.txt file.
with open("movies.txt") as f:
    movies = f.readlines()

'''create a function to return which movies a user would watch
next if they have watched Planet Hulk with the description “Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.”'''
def watch_next(movie):
    # create an empty list to store the movies with the highest similarity scores
    similar_movies = []
    # create a variable to store the highest similarity score
    highest_similarity = 0
    # create a variable to store the highest similarity score
    for movie_to_compare in movies:
        # calculate the similarity between the movie description and the movie to compare
        similarity = nlp(movie).similarity(nlp(movie_to_compare))
        # if the similarity is higher than the highest similarity score
        if similarity > highest_similarity:
            # set the highest similarity score to the new similarity score
            highest_similarity = similarity
            # add the movie to the list of similar movies
            similar_movies.append(movie_to_compare)
    # return the list of similar movies
    return similar_movies


# Create variable to store the movie description
movie = '''Planet Hulk: Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.'''

# Call the function with the variable movie and print the result in a readable format
next_movie = watch_next(movie)
print()
print("The movies you should watch next are:")
print()
for movie in next_movie:
    print(movie)

