# Programmed by Erika Jane T. Reyes
# BSCOE 2-2
# Data Structures and Algorithms
# Seatwork 1

nickname = "EJ"
print_E = [[" " for e in range(7)] for j in range(7)]
print_J = [[" " for e in range(7)] for j in range(7)]

# Letter E
for row in range(7):
    for column in range(7):
        if column == 0 or(row == 0 or row == 3 or row == 6) and column > 0:
            print_E[row][column]= "*"

# Letter J
for row in range(7):
    for column in range(7):
        if column == 3 or (row == 0) or (row == 6 and column < 4):
            print_J[row][column]= "*"

for e in range(7):
    for j in range(7):
        print(print_E[e][j], end="")
    print(end= "  ")
    for j in range(7):
        print(print_J[e][j], end="")
    print()