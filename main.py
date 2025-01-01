number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,]

winning_list = [[1, 2, 3], [1, 4, 7], [1, 5, 9],
                [2, 5, 8], [3, 5, 7], [3, 6, 9],
                [4, 5, 6], [7, 8, 9]]
user_inp_1 = []
user_inp_2 = []
winner = None

# TODO: Printing the game board
def board():
    """ the board for the game """
    print(f'     1     |     2     |     3     \n'
          f'-----------------------------------\n'
          f'     4     |     5     |     6     \n'
          f'-----------------------------------\n'
          f'     7     |     8     |     9     \n')

# TODO: to validate player input
def validate_input(input_no, num_list):
    """ ensure correct user number input """
    if input_no not in num_list:
        print(f"Wrong number, player should choose number be within {num_list}")
        return False
    return True

# TODO: check for win or tie
def check_winner(user_inputs, win_list):
    """ to check which player wins or if it is a tie
        returns a boolean true for a winner and false for a tie
    """
    for combination in win_list:
        if all(num in user_inputs for num in combination):
            return True
    return False #  TIE scenario

game_on = True

while game_on:
    while winner is None:
        valid_X = False
        while not valid_X:
            try:
                board()
                X = int(input('X enter a number: '))
                # check if player played in same position
                if user_inp_1.count(X) > 0 or user_inp_2.count(X) > 0:
                    print('number position already, pick another position')
                    valid_X = False
                # validate input before adding to the list
                elif validate_input(X, number_list):
                    valid_X = True
                    user_inp_1.append(X)
                    print(f'X played position: {user_inp_1} ')
            except ValueError:
                print('please enter a valid number.')

        # To check winner
        result_1 = check_winner(user_inp_1, winning_list)
        if result_1:
            winner = "Player 1"
            break

        # Switch Player, Player 2's turn
        valid_Y = False
        while not valid_Y:
            try:
                board()
                Y = int(input('Y enter a number: '))
                # check if player played in same position
                if user_inp_1.count(Y) > 0 or user_inp_2.count(Y) > 0:
                    print('number position already, pick another position')
                    valid_Y = False
                # validate input before adding to the list
                elif validate_input(Y, number_list):
                    valid_Y = True
                    user_inp_2.append(Y)
                    print(f'Y played positions: {user_inp_2} ')
            except ValueError:
                print('please enter a valid number')

        if check_winner(user_inp_2, winning_list):
            winner = 'Player 2'
            break

        # check maximum times player 1 can play
        if len(user_inp_1) >= 5:
            print('maximum moves reached')

    if winner:
        print(f'The winner is {winner}')
        play_again = input('Want to play again? (yes/no): ').lower()
        if play_again == 'no':
            game_on = False
    else:
        print('TIE!')
        play_again = input('Want to play again? (yes/no): ').lower()
        if play_again == 'no':
            game_on = False

