# Create a dictionary to store the number of students who prefer each movie genre
movie_genres = {'Comedy': 73, 'Action': 42, 'Romance': 38, 'Fantasy': 28, 'Science-fiction': 22,
              'Horror': 19, 'Crime': 18, 'Documentary': 12, 'History': 8, 'War': 7}

import matplotlib.pyplot as plt

#print the dictionary
print(movie_genres)


# Set the labels and sizes for each pie slice
labels = movie_genres.keys()
sizes = movie_genres.values()

# Plot the pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# set same scale
plt.axis('equal')

# Set the title of the plot
plt.title('Favourite Movie Genres of University Students in China')

# Show the plot
plt.show()

# Define the requested genre
requested_genre = 'Comedy'

# Get the number of students who prefer the requested genre from the dictionary
num_students = movie_dict[requested_genre]

# Print the result
print(f"The number of university students who prefer {requested_genre} is: {num_students}")

