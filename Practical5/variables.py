a = -3.19  # Edinburgh longitude
b = -118.24  # Los Angeles longitude
c = 116.39  # Haining longitude

d = abs(a-b)  # Longitude distance between Edinburgh and Los Angel
e = abs(a-c)  # Longitude distance between Edinburgh and Haining

# Compare d and e to determine which distance is greater
if d > e:
    print("Rob travelled further to Los Angeles")
else:
    print("Rob travelled further to Haining")



X = True
Y = False

W = X and Y  # W will have the value False
Z = X or Y  # Z will have the value True

print("The value of W is:", W)  # The value of W is: False
print("The value of Z is:", Z)  # The value of Z is: Ture
