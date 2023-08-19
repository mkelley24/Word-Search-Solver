import random

def create_file():
    file_name: str = input("Enter Filename: ")
    width: int = int(input("Enter Width: "))
    height: int = int(input("Enter Height: "))
    ASCII_DIFFERENCE: int = 65
    puzzle_file = open(file_name, "w")
    for _ in range(height):
        for _ in range(width):
            puzzle_file.write(chr(ASCII_DIFFERENCE + random.randint(0, 25)))
        puzzle_file.write("\n")
    puzzle_file.close()

create_file()