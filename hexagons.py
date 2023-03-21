# Define a function to compute the nth hexagon number
def hexagon_number(n):
    # The formula for the nth hexagon number is H(n) = n(2n-1), where n is the index
    return n * (2 * n - 1)

# Use a loop to compute and print the first five hexagon numbers.
for i in range(1, 6):
    # Compute the ith hexagon number
    hex_num = hexagon_number(i)
    # Print the result
    print("Hexagon number", i, "is", hex_num)

