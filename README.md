# Project: Python Chess Program

--------------------------------------------
## Project Objective

Objective for this project was to answer the question: given a board state that the user enters, with 1 white figure and up to 16 black figures, which black figures can the white figure take?

**Criteria:**
- The program should first ask the user to input a chess piece and where it is on the board. This will be the white piece. The user should be informed that they can choose between two pieces of your choice (e.g. pawn and rook). The choice should be made by writing the piece and the coordinates in a predefined format in the console, e.g.: knight a5
- Once the user successfully adds the white piece, the user is asked to enter the black pieces, one by one, in the same format as the white piece. They need to add at least 1 black piece or 16 at most. Once at least one black piece has been added, the user can write “done” instead of the coordinates to add no more pieces.
- You can assume that the user will input either “done” or the correct format for adding a piece (“piece coordinates”). You can also assume that coordinates will always be entered as where letters are a-h and digits are 1-8, e.g. a1, d4, h8. You should not assume anything else about the inputs, however (hint: there are still at least a couple of ways for the user to make invalid input, e.g. trying to write “done” too early)
- After adding each piece, there should be either a confirmation that it was added successfully, or an error message explaining what the issue is.
- After the white and the black pieces are added, the program should print out the black pieces, if any, that the white piece can take.

**Tools used:**
Python language in Cursor

## Project Content

- **chess.py** - python file with full project code