inputData = []

file = open("input.txt", "r")

for line in file:
    inputData.append(line.rstrip("\n"))

numbers = inputData[0]

numbers = [int(n) for n in numbers.split(',')]

boards = []

counter = 1


def check_row(board, index):
    for num in board[index]:
        if int(num) != -1:
            return False

    return True

def locate_num_row(board, number, index):
    for i in range(len(board)):
        if int(board[index][i]) == number:
            return i

    return -1

def locate_num_col(board, number, index):
    for i in range(len(board)):
        if int(board[i][index]) == number:
            return i

    return -1

def check_col(board, index):
    for i in range(len(board)):
        if int(board[i][index]) != -1:
            return False

    return True

def check_board(board):
    for i in range(len(board)):
        if check_row(board, i) or check_col(board, i):
            return True

    return False

def unmarked_sum(board):
    total = 0

    for i in range(len(board)):
        for j in range(len(board)):
            if int(board[i][j]) != -1:
                total += int(board[i][j])

    return total

board = []

for data in inputData[2:]:
    row = []

    if data:
        for n in data.split():
            if n != ' ':
                row.append(n)
        
        board.append(row)
    
        if counter % 5 == 0 and counter > 0:
            boards.append(board)
            board = []

        counter += 1

winning_board_index = 0

winnning_scores = []

for num in numbers:
    for i, board in enumerate(boards):
        for j in range(5):
            num_index = locate_num_row(board, num, j)

            if num_index != -1:
                boards[i][j][num_index] = -1
        
        for j in range(5):
            num_index = locate_num_col(board, num, j)

            if num_index != -1:
                boards[i][num_index][j] = -1
        
        if check_board(board):
            total = unmarked_sum(board) * num
            board[0][0] = -2
            winnning_scores.append(total)

    for i, board in enumerate(boards[::-1]):
        if board[0][0] == -2:
            boards.remove(board)

print(winnning_scores[-1])