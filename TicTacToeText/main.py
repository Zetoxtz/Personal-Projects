class board(object):
    def __init__(self):
        """
        The board
        0 = empty
        1 = p1
        2 = p2
        """
        self.state = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def print_board(self):
        """
        prints the board
        :return: void
        """
        print("   |   |   ")
        print(" {} | {} | {}".format(self.state[0][0], self.state[0][1], self.state[0][2]))
        print("-----------")
        print(" {} | {} | {}".format(self.state[1][0], self.state[1][1], self.state[1][2]))
        print("-----------")
        print(" {} | {} | {}".format(self.state[2][0], self.state[2][1], self.state[2][2]))
        print("   |   |   ")

    def add(self, cord, sign):
        """
        adds the sign to the board
        :param cord: the coordinates given by the user
        :param sign: the sign of user "x" or "o"
        :return:
        """
        c1 = cord[0]
        c2 = cord[1]
        self.state[c1][c2] = sign

    def check_if_won(self):
        """
        Checks if the current (any) player has won.
        Does work out to see who has won.
        :return: True when certain win condition is met else returns false
        """

        for i in range(3):
            for j in range(3):
                if self.state[i][j] == " ":
                    continue
                if self.state[i][0] == self.state[i][1] == self.state[i][2]:
                    return True
                if self.state[0][j] == self.state[1][j] == self.state[2][j]:
                    return True

                if i == j:
                    if self.state[0][0] == self.state[1][1] == self.state[2][2]:
                        return True

                if (i, j) == (0, 2) or (i, j) == (1, 1) or (i, j) == (2, 0):
                    if self.state[0][2] == self.state[1][1] == self.state[2][0]:
                        return True

        return False

    def is_valid(self, c):
        """
        Checks if player can put the sign there
        A player may only put a sign there when no other player has put sign there
        :param c: The coordinates
        :return: True if it is a valid position to put a sign else returns false
        """

        c1 = c[0]
        c2 = c[1]

        if self.state[c1][c2] == " ":
            return True
        else:
            return False


class player(object):
    def __init__(self, name, sign):
        self.sign = sign
        self.name = name
        self.score = 0

    def add_to_board(self, b1, cord):
        """
        Adds the sign to the board. This is only done after a check to see if it is valid
        :param b1: the current board
        :param cord: the coordinates
        :return: void
        """
        b1.add(cord, self.sign)

    def getName(self):
        """
        Returns the name lol
        :return: name of player
        """
        return self.name


if __name__ == '__main__':
    # Initializes the board
    board1 = board()
    board1.print_board()

    # Initializes the players
    p1 = player("James", "x")
    p2 = player("David", "o")

    players = [p1, p2]
    playerCount = 0  # The player number

    while True:
        # The count may go out of bounds So to prevent that
        # Ensures a infinite circular loop
        if playerCount == 2:
            playerCount = 0

        current_player = players[playerCount]

        # The coordinates the player will enter to put the sign
        cord = []

        # IN case user tries something funny
        try:
            cord.append(int(input("Enter the x coordinate: ")) - 1)
            cord.append(int(input("Enter the y coordinate: ")) - 1)
        except ValueError:
            print("Please enter coordinates")
            continue

        # Makes sure the coordinates are in bounds
        if cord[0] > 2 or cord[0] < 0 or cord[1] > 2 or cord[1] < 0:
            print("Enter valid coordinates!!!")
            continue

        # If the coordinates array is somehow empty
        if not cord:
            continue

        # In case the placement of sign is not valid
        if not board1.is_valid(cord):
            print("You cannot place it here!!")
            continue

        # Places the sign
        current_player.add_to_board(board1, cord)

        board1.print_board()

        # Checks if the current player has won. Somehow seems to work
        won = board1.check_if_won()

        if won:
            print("{} has won the game".format(current_player.getName()))
            break

        # Changes the player
        playerCount += 1
