# Word-Search-Solver
## Description:
This is an tkinter app that allows the user to input a text file containing a word search grid and the associated wordbank.
The program then searches for the words within the grid, it then displays the grid with the words within the grid being green,
while other letters are shown as red.
## Challenges Encountered
There where a few different challenges I had to overcome for this project:
### Reversed Words:
The program needs to recognize the reverse of a word so I created a word object which stores the original string, its reverse and a hash for each string (the hashes are for the Rabin-Karp Pattern matching algorithm which the program uses), the program can then match the hash of the text window against the hashes of both orientations of the word allowing it to recognize either orientation within the puzzle, I was originally considering trying to create a hash for the rabin karp algorithm that would create a singular hash value for a string and its reverse. I did decide not to follow through with this idea because I could not come up with an algorithm that would work well and follow the requirements.
### Grid traversal:
given that we will need to move across the grid in different directions i used two technologies combined 