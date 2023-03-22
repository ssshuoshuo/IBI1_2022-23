# Initialize the number of rabbits
rabbits = 2
# Initialize the number of generation
generation = 1

# While the number of rabbits is less than 100, calculate the number of rabbits in each generation
while rabbits < 100:
    # The number of rabbits in each generation is twice the number of rabbits in the previous generation
    rabbits = rabbits * 2
    # Increment the number of generation
    generation += 1

# Output the number of generation and the total number of rabbits
print("It takes " + str(generation) + " generations to have at least 100 \
rabbits.")

 
