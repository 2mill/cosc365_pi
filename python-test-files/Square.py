# the squares test code from the No Starch book
squares = [];
for values in range(1,101):
    squares.append(values ** 2)
print("Minimum number")
print(min(squares))
print("Max number")
print(max(squares))
print("Sum of all")
print(sum(squares))