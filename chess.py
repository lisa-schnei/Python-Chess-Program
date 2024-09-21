# CHESS PROJECT
# Goal: Answer the question: which black figures can the white figure take?
# ----------
# 1. Get user input on white figure placement; user can choose between two pieces; input takes piece and coordinates
# 2. User inputs placement of black pieces; minimum 1; maximum 16; "done" marks end of input
# 3. Provide feedback after user input - "ok" or "invalid"
# 4. Check if white figure can take any black figure
# 5. Provide feedback to user on which black figures can be taken


def main(): 
    """ Main function runs the program """

    # Start with an empty board to store piece placement in 
    board_state = get_new_board_state()

    # Get user input on white figure placement
    placement_white = user_input_white()

    # Update board state with white figure placement
    board_state = update_board_state(board_state, placement_white)

    # Get user input on black figure placement
    # Update board state with black figure placement
    placement_black = user_input_black(board_state)

    # Identify which black figures can be taken by the white figure
    white_figure, white_coord = placement_white # unpack tuple placement_white into figure and coordinates
    captured_figures = [] # empty list to store the captured black figures

    for coord, figure in board_state.items():
        if figure[1] == "B": # checking if the figure is black
            if can_capture(white_figure, white_coord, coord, board_state):
                captured_figures.append(figure[0]) # appending the figure type to the captured_figures list
    
    # Formatting the list of captured figures
    figure_names = { # Mapping figure letter back to full names
        'b': 'bishop',
        'r': 'rook',
        'n': 'knight',
        'q': 'queen',
        'k': 'king',
        'p': 'pawn'
        }
    full_captured_figures = [figure_names[figure[0]] for figure in captured_figures]  
    # Iterates over figures in captured_figures list 
    # Uses the first character for each figure [0] to look up full name in the figure_names dictionary
    # Collects results in a new list (full_captured_figures)
    captured_figures_str = ", ".join(full_captured_figures)  # Creates a string with full names to output

    # Provide feedback to user on which black figures can be taken
    if captured_figures:
        print(f"The white figure can capture the following black figures: {captured_figures_str}")
    else:
        print(f"The white figure cannot capture any black figures.")




def get_new_board_state():
    """ Returns an empty dictionary to store the board state """
    return {}

def user_input_white():
    """ Returns the placement of the white figure """
    print("First, tell me the placement of the white figure. You can choose between two figures: 'bishop' or 'rook'.")
    print("Enter the figure and coordinates of the white figure in this example format 'bishop a1'.")
    print() # adding a line for better readability
    
    while True:
        input_white = input("White figure: ").strip().lower() # removing spaces and making all letters lowercase
        try:    
            figure, coord = input_white.split(" ") # splitting the input into figure and coordinates
            break       
        except ValueError:
            print("Invalid input. Please try again. Ensure your input is as in the format given.")
            continue
        
    if figure == "bishop" or figure == "rook" and len(coord) == 2 and coord[0] in "abcdefgh" and coord[1] in "12345678": # checking if the input is valid
        figure = figure[0] + "W" # transforming figure variable into format to be stored in board_state dictionary
        return figure, coord
    else:
        print("Invalid input. Please try again. Ensure your input is as in the format given.")
        return user_input_white()

def update_board_state(board_state, placement_white):
    """ Updates the board state with the placement of the white figure """
    figure, coord = placement_white 
    board_state[coord] = figure # assigning coord as a key and figure as a value in the board_state dictionary
    return board_state

def user_input_black(board_state):
    """ Returns the placement of the black figures """
    print("Now it is time to enter the placements of the black figures.")
    print("Enter minimum 1 figure and maximum 16 figures in the format 'bishop a1'.")
    print("When you have inserted all figures, type 'done'.")
    print() # adding a line for better readability
    
    while True:
        input_black = input("Black figure: ").strip().lower()  # Get user input, remove spaces, and lowercase
        if input_black == "done":
            if len(board_state) > 1:  # Ensure at least one black figure has been added
                break
            else:
                print("You must enter at least one black figure.")
                continue
        
        try: # block used to attempt execute code that may raise an error
            figure, coord = input_black.split(" ")  # Split the input into figure and coordinates
        except ValueError:
            print("Invalid input. Please enter in the format 'bishop a1'.")
            continue
        
        # Validate the figure and coordinate
        if figure in ["bishop", "rook", "knight", "queen", "king", "pawn"] and len(coord) == 2 and coord[0] in "abcdefgh" and coord[1] in "12345678":
            figure = figure[0] + "B"  # Transform figure variable into a format to be stored in the board_state dictionary
            if coord in board_state:
                print("There is already a figure at that position. Please choose another position.")
            else:
                # Update the board state for this black piece
                board_state = update_board_state(board_state, (figure, coord))
                if len(board_state) >= 17:  # 1 white + 16 black = 17 pieces max on the board
                    print("Maximum number of figures on the board (17) reached.")
                    break
        else:
            print("Invalid input. Please try again. Ensure your input is in the correct format.")
    
    return board_state

def can_capture(white_figure, white_coord, black_coord, board_state):
    white_type = white_figure[0] # extract figure type; b for bishop, r for rook

    white_x, white_y = ord(white_coord[0]), int(white_coord[1]) # returning the numeric value of the string character through ord()  
    black_x, black_y = ord(black_coord[0]), int(black_coord[1])
    # black_coord are passed from the main() function with 'if can_capture(white_figure, white_coord, coord, board_state)'

    if white_type == "r": #checking for rook if on same row or column
        if white_x == black_x or white_y == black_y: # if the black figure is one same row or column as white figure: check if path is clear
            if is_path_clear(white_coord, black_coord, board_state, "straight"):
                return True
        
    
    elif white_type == "b": #checking for bishop if on same diagonal
        if abs(white_x - black_x) == abs(white_y - black_y):
            if is_path_clear(white_coord, black_coord, board_state, "diagonal"):
                return True
    
    return False

def is_path_clear(start, end, board_state, direction): 
    """ Checks if the path between two figures (white and black) is clear, returning True or False """
    start_x, start_y = ord(start[0]), int(start[1]) # start coordinate corresponds to white figure coordinates (white_coord). Ord() transforms letter to ASCII number
    end_x, end_y = ord(end[0]), int(end[1]) # end coordinate corresponds to black figure coordinates (black_coord)

    if direction == "diagonal": # check for bishop figure movement; 4 possible combinations of movement (1,1), (1,-1), (-1,1), (-1,-1)
        step_x = 1 if end_x > start_x else -1
        step_y = 1 if end_y > start_y else -1

        x, y = start_x + step_x, start_y + step_y # x and y are coordinates of the first diagonal square between white and black figure
        while x != end_x and y != end_y: # loop going further through the squares between white and black figure until meeting end square (black figure)
            if chr(x) + str(y) in board_state: # check if any of the squares in loop are in the board_state dictionary
                return False
            x += step_x # incrementing the x coordinate by 1 unit in the direction of the movement
            y += step_y # incrementing the y coordinate by 1 unit in the direction of the movement
            # += is equivalent to x = x + step_x

    elif direction == "straight": # checks for rook figure movement 
        if start_x == end_x:  # If white and black figure are on same column
            step_y = 1 if end_y > start_y else -1 # determining the direction of the movement (up or down)
            for y in range(start_y + step_y, end_y, step_y): # loop going through the square between the white and black figure placement. 
                # start_y + step_y: starting with the square next to the white figure in movement direction
                # end_y: loop running up to but not including the black figure placement
                # step_y: incrementing the y coordinate by 1 unit in the direction of the movement
                if chr(start_x) + str(y) in board_state: #chr(start_x) converts ASCII number back to letter; checks if any squares between white and black figure are in the board_state dictionary
                    return False
        else:  # If white and black figure are on same row
            step_x = 1 if end_x > start_x else -1 # determining the direction of the movement (right or left)
            for x in range(start_x + step_x, end_x, step_x): 
                if chr(x) + str(start_y) in board_state: 
                    return False

    return True


main()