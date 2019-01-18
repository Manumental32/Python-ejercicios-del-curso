//creditos a ff

# -*- coding: utf-8 -*-

import copy

Infinite = 1000

def negamax(node, alpha, beta, color, depth):
    if depth == 0 or node.is_final():
        return color * node.eval_board(), None
        
    childNodes = node.generate_moves()
    # childNodes = order_moves(childNodes)        
    value = -Infinite
    node = None
    for child in childNodes:
        new_value, _ = negamax(child, -beta, -alpha, -color, depth-1)
        if new_value >= value:
            value = new_value
            node = child
        alpha = max(alpha, value)
        if alpha >= beta: break
    return value, node

                    
class Neutron:

    Empty = ' '    
    Black = '0'
    White = 'X'
    Neutron = 'N'
    
    def __init__(self, size=5):
        self.size = size
        self.blacks = [(i, 0) for i in range(size)]
        self.whites = [(i, size-1) for i in range(size)]
        self.neutron = (size//2, size//2)
        self.color = self.White
        # generate board
        self.board = []
        self.board.append(self.Black * size)
        for i in range(size-2):
            self.board.append(self.Empty * size)
        self.board[size//2] = self.Empty * (size//2) + self.Neutron + self.Empty * (size//2)
        self.board.append(self.White * size)

    def __repr__(self):
        return '|'.join(self.board)
    
    def __str__(self):
        return '\n'.join(self.board)

    def is_final(self):
        # si el neutron está en alguna línea base o si el neutron no se puede mover
        return self.neutron[1] == 0 or self.neutron[1] == self.size-1 or not [i for i in self.generate_coord(self.neutron)]

    def eval_board(self):
        if self.color == self.White:
            color = -1
        else:
            color = 1
        # si está en línea base no depende de quien juega
        if self.neutron[1] == 0: return -Infinite
        if self.neutron[1] == self.size-1: return Infinite
        # si el neutron no se puede mover depende de quien es el turno
        if not [i for i in self.generate_coord(self.neutron)]: return color * -Infinite
        # premiamos si las fichas "tapan" los lugares del adversario y viceversa
        value = 0
        for i in range(self.size):
            if self.board[0][i] != self.Empty: value += 4
            if self.board[1][i] != self.Empty: value += 3
            if self.board[-2][i] != self.Empty: value -= 3
            if self.board[-1][i] != self.Empty: value -= 4
        return color * value

    def toggle_color(self):            
        if self.color == self.White:
            self.color = self.Black
        else:
            self.color = self.White            
        
    def get_pieces(self):
        if self.color == self.White:
            return self.whites
        else:
            return self.blacks

    def set_piece(self, i, x, y):
        if self.color == self.White:
            self.whites[i] = x, y
        else:
            self.blacks[i] = x, y
            
    def generate_coord(self, piece):
        x, y = piece
        for dx in range(-1, 2): # dx: -1, 0, +1
            for dy in range(-1, 2): # dy: -1, 0, +1
                # tiene que estar dentro del tablero y tener el lugar vecino libre
                if (dx != 0 or dy != 0) and 0 <= x+dx < self.size and 0 <= y+dy < self.size and self.board[y+dy][x+dx] == self.Empty:
                    yield dx, dy               
                
    def generate_positions(self, piece):
        for dx, dy in self.generate_coord(piece):
            x, y = piece
            # mientras haya lugar libre avanzamos la pieza todo lo que pueda sin salirse del tablero
            while 0 <= x+dx < self.size and 0 <= y+dy < self.size and self.board[y+dy][x+dx] == self.Empty:
                x += dx
                y += dy
            yield x, y

    def generate_neutron(self):
        for x, y in self.generate_positions(self.neutron):
            move = copy.deepcopy(self)
            move.neutron = x, y
            move.board[y] = move.board[y][:x] + self.Neutron + move.board[y][(x+1):]
            x, y = self.neutron
            move.board[y] = move.board[y][:x] + self.Empty + move.board[y][(x+1):]
            yield move
            
    def generate_moves(self):                
        for m in self.generate_neutron():
            for i, p in enumerate(m.get_pieces()):
                for x, y in m.generate_positions(p):            
                    move = copy.deepcopy(m)
                    move.set_piece(i, x, y)
                    move.board[y] = move.board[y][:x] + move.color + move.board[y][(x+1):]
                    x, y = p
                    move.board[y] = move.board[y][:x] + self.Empty + move.board[y][(x+1):]
                    move.toggle_color()
                    yield move
            
    
if __name__ == "__main__":
    root = Neutron()
    color = 1
    depth = 5
    value, node = negamax(root, -Infinite, Infinite, color, depth)
    print(value)
   
