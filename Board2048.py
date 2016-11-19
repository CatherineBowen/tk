from random import choice

class Board(object):
    def __init__(self, dimension=4):
        self._board = [[0 for _ in range(dimension)] for _ in range(dimension)]
        self._length = dimension
        self._prev = [[0 for _ in range(dimension)] for _ in range(dimension)]

    def newGame(self):
        for row in self._board:
            for col in row:
                col = 0
        self._populate(2,2)


    def _colify(self):
        self._board = [[self._board[c][r] for c in range(self._length)]for r in range(self._length)]

    
    def _populate(self, amount=1, number=choice([2,2,4])):
        rand = choice(range(self._length))
        for r in range(rand, rand+self._length):
            rand2 = choice(range(self._length))
            for c in range(rand2, rand2+self._length):
                if amount == 0:
                    return
                elif self._board[r%self._length][c%self._length] == 0:
                    self._board[r%self._length][c%self._length] = number
                    amount -= 1
        return "Board Full"


    
    def _moveZeros(self, direction):
        for r in range(self._length):
            nz = [col for col in self._board[r] if col != 0]
            z = [col for col in self._board[r] if col == 0]
            if direction == "left":
                self._board[r] = nz + z
            else:
                self._board[r] = z + nz


    def moveX(self, direction):
        self._prev = self._board.copy()
        self._moveZeros(direction)
        for r in range(self._length):
            for c in range(1, self._length):
                if direction == "left":
                    cur = c
                    nxt = c - 1
                else:
                    cur = self._length - 1 - c
                    nxt = self._length - c
                if self._board[r][nxt] == self._board[r][cur]:
                    self._board[r][nxt] *= 2
                    self._board[r][cur] = 0
        
        self._moveZeros(direction)
        if self._board != self._prev:
            self._populate()


    def moveY(self, direction):
        self._colify()
        if direction == "up":
            self.moveX("left")
        else:
            self.moveX("right")
        self._colify()
        
    

    
