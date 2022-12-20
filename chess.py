#
# comment block
#
class Board:
    def __init__(self):
        self.board = {}
        self.empty()
    def empty(self):
        for col in 'abcdefgh':
            for row in '12345678':
                self.board[col+row] = ' '    
    def set(self, pos, label):
        if pos in self.board.keys():
            self.board[pos] = label
    def draw(self):
        col = 'abcdefgh'
        row = '12345678'
        print('   a   b   c   d   e   f   g   h')
        for c in range(len(col)):
            print(' +---+---+---+---+---+---+---+---+')
            print(f'{c+1}',end='')
            for r in range(len(row)):
                print(f'| {self.board[col[r]+row[c]]} ', end='')
                if(r == 7):
                    print(f'|{c+1}')
        print(' +---+---+---+---+---+---+---+---+')
        print('   a   b   c   d   e   f   g   h')
                   
class Chess_Piece:
    def __init__(self, board, pos, color='white'):
        self.position = self.get_index(pos)
        self.color = color
        board.set(pos, self.get_name())
    def get_index(self, pos):
        return ('abcdefgh'.index(pos[0]), '12345678'.index(pos[1]))
    def get_rank(self, index):
        if index >= 0 and index < 8:
            return '12345678'[index]
        else:
            return ''
    def get_file(self, index):
        if index >=0 and index < 8:
            return 'abcdefgh'[index]
        else:
            return ''
    def get_name(self):
        pass
    def moves(self, board):
        pass
    
class King (Chess_Piece):
    def get_name(self):
        return 'K'
    def moves(self, board):
        board.set(self.get_file(self.position[0]-1) + self.get_rank(self.position[1]-1), 'X')
        board.set(self.get_file(self.position[0]) + self.get_rank(self.position[1]-1), 'X')
        board.set(self.get_file(self.position[0]+1) + self.get_rank(self.position[1]-1), 'X')
        board.set(self.get_file(self.position[0]-1) + self.get_rank(self.position[1]), 'X')
        board.set(self.get_file(self.position[0]+1) + self.get_rank(self.position[1]), 'X')
        board.set(self.get_file(self.position[0]-1) + self.get_rank(self.position[1]+1), 'X')
        board.set(self.get_file(self.position[0]) + self.get_rank(self.position[1]+1), 'X')
        board.set(self.get_file(self.position[0]+1) + self.get_rank(self.position[1]+1), 'X')
        
       
class Queen (Chess_Piece):
    def get_name(self):
        return 'Q'
    def moves(self, board):
        for i in range (1,8):
            board.set(self.get_file(self.position[0]+i) + self.get_rank(self.position[1]+i), 'X')
            board.set(self.get_file(self.position[0]-i) + self.get_rank(self.position[1]-i), 'X')
            board.set(self.get_file(self.position[0]+i) + self.get_rank(self.position[1]), 'X')
            board.set(self.get_file(self.position[0]) + self.get_rank(self.position[1]+i), 'X')
            board.set(self.get_file(self.position[0]-i) + self.get_rank(self.position[1]), 'X')
            board.set(self.get_file(self.position[0]) + self.get_rank(self.position[1]-i), 'X')
            board.set(self.get_file(self.position[0]+i) + self.get_rank(self.position[1]-i), 'X')
            board.set(self.get_file(self.position[0]-i) + self.get_rank(self.position[1]+i), 'X')


class Rook (Chess_Piece):
    def get_name(self):
        return 'R'
    def moves(self, board):
        for i in range (1,8):
            board.set(self.get_file(self.position[0]) + self.get_rank(self.position[1]+i), 'X')
            board.set(self.get_file(self.position[0]) + self.get_rank(self.position[1]-i), 'X')
            board.set(self.get_file(self.position[0]+i) + self.get_rank(self.position[1]), 'X')
            board.set(self.get_file(self.position[0]-i) + self.get_rank(self.position[1]), 'X')

class Bishop (Chess_Piece):
    def get_name(self):
        return 'B'
    def moves(self, board):
        for i in range (1,8):
            board.set(self.get_file(self.position[0]+i) + self.get_rank(self.position[1]+i), 'X')
            board.set(self.get_file(self.position[0]-i) + self.get_rank(self.position[1]-i), 'X')
            board.set(self.get_file(self.position[0]+i) + self.get_rank(self.position[1]-i), 'X')
            board.set(self.get_file(self.position[0]-i) + self.get_rank(self.position[1]+i), 'X')
                      
class Knight (Chess_Piece):
    def get_name(self):
        return 'N'
    def moves(self, board):
        board.set(self.get_file(self.position[0]+1) + self.get_rank(self.position[1]+2), 'X')
        board.set(self.get_file(self.position[0]-1) + self.get_rank(self.position[1]+2), 'X')
        board.set(self.get_file(self.position[0]+2) + self.get_rank(self.position[1]+1), 'X')
        board.set(self.get_file(self.position[0]-2) + self.get_rank(self.position[1]+1), 'X')
        board.set(self.get_file(self.position[0]+2) + self.get_rank(self.position[1]-1), 'X')
        board.set(self.get_file(self.position[0]-2) + self.get_rank(self.position[1]-1), 'X')
        board.set(self.get_file(self.position[0]+1) + self.get_rank(self.position[1]-2), 'X')
        board.set(self.get_file(self.position[0]-1) + self.get_rank(self.position[1]-2), 'X')

class Pawn (Chess_Piece):
    def get_name(self):
        return 'P'
    def moves(self, board):
        board.set(self.get_file(self.position[0]) + self.get_rank(self.position[1]-1), 'X')
        #board.set(self.get_file(self.position[0]+1) + self.get_rank(self.position[1]-1), 'X')
        #board.set(self.get_file(self.position[0]-1) + self.get_rank(self.position[1]-1), 'X')

# your code goes here

if __name__ == '__main__':
    print('Welcome to the Chess Game!')
    board = Board()
    board.draw()

    # your code goes here
    while (True):
        board.empty()
        user_input = input("Enter a chess piece and its position or type X to exit:").lower()  
        if (user_input[0:1] == 'k'):
            k = King(board,user_input[1:3])
            k.moves(board)
            board.draw()
            continue
        elif (user_input[0:1] == 'q'):
            q = Queen(board,user_input[1:3])
            q.moves(board)
            board.draw()
            continue
        elif (user_input[0:1] == 'b'):
            b = Bishop(board,user_input[1:3])
            b.moves(board)
            board.draw()
            continue
        elif (user_input[0:1] == 'r'):
            r = Rook(board,user_input[1:3])
            r.moves(board)
            board.draw()
            continue
        elif (user_input[0:1] == 'n'):
            n = Knight(board,user_input[1:3])
            n.moves(board)
            board.draw()
            continue
        elif (user_input[0:1] == 'p'):
            p = Pawn(board,user_input[1:3])
            p.moves(board)
            board.draw()
            continue
        elif(user_input[0:1] == 'x'):                
            print('Goodbye!')
            break
        else:
            continue
