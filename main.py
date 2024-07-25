class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
    
    def move(self, start_pos, end_pos, board):
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        
        if not self.is_valid_position(end_row, end_col):
            return False
        
        piece_at_end = board.board[end_row][end_col]
        if piece_at_end and piece_at_end.color == self.color:
            return False
        
        direction = 1 if self.color == 'black' else -1
        
        if start_col == end_col and end_row == start_row + direction and not piece_at_end:
            board.board[end_row][end_col] = self
            board.board[start_row][start_col] = None
            return True
        
        if (start_col == end_col and end_row == start_row + 2 * direction and
            (self.color == 'black' and start_row == 6 or self.color == 'white' and start_row == 1) and
            not piece_at_end and not board.board[start_row + direction][start_col]):
            board.board[end_row][end_col] = self
            board.board[start_row][start_col] = None
            return True
        
        if (abs(start_col - end_col) == 1 and end_row == start_row + direction and
            piece_at_end and piece_at_end.color != self.color):
            board.board[end_row][end_col] = self
            board.board[start_row][start_col] = None
            return True
        
        return False

    def is_valid_position(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8
