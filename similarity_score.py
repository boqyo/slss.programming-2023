# Comparing Similarity Scores
# Author: shaun
# November 8 2023

# Calculate similarity scores between two people

# Create two lists that represent the movies
# that people like
shauns_favorite_movies = [
    "The Matrix",
    "Infinity War", 
    "The Empire Strikes Back",
    "Infernal Affairs",
    "Rouge One"
]
bens_favorite_movies = [
    "Guardians of the Galaxy: Volume 3",
    "Spider-man",
    "The Matrix",
    "Infinity War",
    "The Empire Strikes Back"
]
# Initialize a similarity score
similarity_score = 0

# Iterate through all movies in first list
for movie in shauns_favorite_movies:
    # If that item is in the second list
    if movie in bens_favorite_movies:
        # Increase similarity score by 1
        similarity_score += 1


# Display results
print(f"Shaun and Ben have a similarity score of {similarity_score}")