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
    similar_movies = [] # Create an empty list to store the similar movies
    highest_similarity = 0.8 # Set the similarity threshold
    for movie_to_compare in movies:
        similarity = nlp(movie).similarity(nlp(movie_to_compare))        
        if similarity > highest_similarity:            
            similar_movies.append(movie_to_compare)
    similar_movies.sort(key=lambda x: nlp(x).similarity(nlp(movie)), reverse=True) # Sort the list by similarity    
    return similar_movies[:3] # Return the top 3 similar movies



# Create variable to store the movie description
movie = '''Planet Hulk: Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.'''

# Call the function with the variable movie and print the result in a readable format
next_movie = watch_next(movie)
print("The movies you should watch next are:")
print()
for movie in next_movie:
    print(movie)

