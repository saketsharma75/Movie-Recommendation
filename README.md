# README

## Description

This code reads in a list of movies and creates a function to recommend which movies a user should watch next based on a given movie description. The function uses Spacy's similarity score to calculate the similarity between the given movie description and each movie in the list, and returns a list of the most similar movies.

## Getting started

To use this code, you will need to have Spacy and its 'en_core_web_md' language library installed. You will also need to have a text file named 'movies.txt' in the same directory as the code file. A sample file is provided in this repository.

## Usage

To recommend the next movie to watch based on a given movie description, call the 'watch_next' function and pass in the movie description as a string. The function will return a list of the most similar movies. For example:

movie = '''Planet Hulk: Will he save their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.'''

next_movie = watch_next(movie)

for movie in next_movie:

  print(movie)
  
## Disclaimer

This code is for educational purposes only. The movie descriptions used in this code were obtained from IMDb and are used solely for demonstration purposes.
