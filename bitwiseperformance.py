import time


def bins(num, bits: int = 64) -> str:
    s = bin(num & 2 ** (bits + 1) - 1)[2:]
    return "0" * (bits - len(s)) + s


class Bitwise:
    def __init__(self):
        self.board = {"b": 0, "w": 0}
        self.height = 8
        self.width = 8

    def add_piece(self, piece: str, row, column):
        self.board[piece] |= 1 << ((8 - row) * 8 + (8 - column))

    def get_board(self) -> list:
        board = [['.'] * 8 for _ in range(8)]
        for piece in self.board.keys():
            for i, val in enumerate(bins(self.board[piece])):
                if board[i // 8][i % 8] == '.' and val != '0':
                    board[i // 8][i % 8] = piece
        return board


class Normal:
    def __init__(self):
        self.board = [['.'] * 8 for _ in range(8)]

    def add_piece(self, piece, row, column):
        self.board[row][column] = piece

    def get_board(self) -> list:
        return self.board


def get_speed(obj):
    start = time.time()
    for _ in range(10 ** 5):
        for i in range(8):
            for j in range(8):
                if i % 2 == 0 and j % 2 == 0:
                    obj.add_piece('b', i, j)
                else:
                    obj.add_piece('w', i, j)
    end = time.time()
    return end-start


b = Bitwise()
n = Normal()

for i in range(8):
    for j in range(8):
        if i % 2 == 0 and j % 2 == 0:
            n.add_piece('b', i, j)
        else:
            n.add_piece('w', i, j)
board = n.get_board()

start = time.process_time()
for _ in range(10**6):
    hash(str(board))
end = time.process_time()
print("str time: {}".format(end-start))

board_t = tuple(map(lambda x: tuple(x), board))
start = time.process_time()
for _ in range(10**6):
    hash(tuple(map(lambda x: tuple(x), board)))
end = time.process_time()
print("tuple time: {}".format(end-start))
#print("Bitwise Time = {}".format(get_speed(b)))
#print("Normal Time = {}".format(get_speed(n)))
