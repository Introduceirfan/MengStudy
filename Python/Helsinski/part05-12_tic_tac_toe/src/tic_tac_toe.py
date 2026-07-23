# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    coord = [0,1,2]
    if x not in coord or y not in coord:
        return False
    if game_board[y][x] == "":
        game_board[y][x] = piece
        return True
    return False

if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "X"))
    print(game_board)