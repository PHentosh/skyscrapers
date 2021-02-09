def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.

    >>> read_input("check.txt")
    ['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']
    """
    with open(path, 'r') as pole:
        lines = pole.readlines()
        pole_list = []
        for i in lines:
            if i[-1] == '\n':
                i = i[:-1]
            pole_list.append(i)
    return pole_list


def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """
    pass


def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5', '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for i in board:
        if '?' in i:
            return False
            break
    return True


def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*553215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    board = board[1:-1]
    for i in board:
        i = i[1:-1]
        for j in i:
            i = i[1:]
            if j in i:
                return False
    return True


def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    board = board[1:-1]
    for i in board:
        left = i[0]
        right = i[-1]
        i = i[1:-1]
        if left != '*':
            el = int(i[0])
            wise = 1
            for j in i[1:]:
                if int(j) > el:
                    el = int(j)
                    wise += 1
            if wise != int(left):
                return False
        if right != '*':
            wise = 1
            i = ''.join(reversed(i))
            el = int(i[0])
            for j in i[1:]:
                if int(j) > el:
                    el = int(j)
                    wise += 1
            if wise != int(right):
                return False
    return True




def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness (buildings of unique height) and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    new_board = []
    for i in range(len(board)):
        new_board.append('')
    for i in board:
        for j in range(len(i)):
            new_board[j] = i[j] + new_board[j]
    wise = check_horizontal_visibility(new_board)
    unity = check_uniqueness_in_rows(new_board)
    return wise and unity



def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.

    >>> check_skyscrapers("check.txt")
    True
    """
    board = read_input(input_path)
    if not check_not_finished_board(board):
        return False
    wise_row = check_horizontal_visibility(board)
    unity_row = check_uniqueness_in_rows(board)
    row = wise_row and unity_row
    col = check_columns(board)
    return row and col


if __name__ == "__main__":
    print(check_skyscrapers("check.txt"))
