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
Given that we will need to move across the grid in different directions I used three objects in tandem to achieve this first I created a point object that is a two dimensional point that has a method called move_point which takes another point and adds the x and y points of parameter point to the x and y of the original point. Next I created the window object which traverses a line of the grid and shows a subset of that line of a certain size at a time. The window object takes a starting point called the head and a point_shift which it will use to determine how it moves across the word grid. I originally planned to create an abstract window class and that would be inherited by all the different directions I would need to traverse, but i realised I was repeating myself too much so I tried another tactic. I then created and enumerator called direction which would store all the directions I would need to traverse and could also return the point shift for that direction which determines how the text window slides across the text line and the head_shift which determines where the next starting point will be after the line has been fully traversed.
### Display:
When I started this project I wanted the display of the solution to show the letter grid with the letters being green if they were part of a found word and red if they were not, but I ran into the problem of trying to color different parts of a line as I was originally planning on having every row be a label in tkinter. I the realized I could make each letter be its own label so I could color it acording to its presence in a word. So I created the letter object which stored the string of the letter it contained and a boolean of whether it was found in a word. The letter has two main methods, one that would set its found boolean to true if it was found as part of a word, and a second method which would generate a label of the letter which colored it red if its found boolean was False and green if its found boolean was true.
## Usage:
* Clone the repository
* Go into the repository then the src folder and run the solver_app.py
* Click the "Select Word Puzzle" button
* Select your desired word search puzzle from the file dialog