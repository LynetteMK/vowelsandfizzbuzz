#A dictionary containing numbers ranging from 1to 15 and their squares.
print("Hello. this is a dictionary containing numbers from 1 to 15 and their squares")
squares = dict()

for value in range(1,16):
    squares[value]=value**2

print(squares)

input()