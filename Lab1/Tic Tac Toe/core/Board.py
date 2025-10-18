class Board:
    def __init__(self):
        # Пустая 3×3 сетка: None, 'X' или 'O'
        self.grid = [[None] * 3 for _ in range(3)]
        self.current = 'X'
        self.winner = None

    def make_move(self, row, col):
        if not self.winner and self.grid[row][col] is None:
            self.grid[row][col] = self.current
            self._check_winner()
            if not self.winner:
                self.current = 'O' if self.current == 'X' else 'X'
            return True
        return False

    def _check_winner(self):
        lines = []
        # строки и столбцы
        for i in range(3):
            lines.append(self.grid[i])  # строка i
            lines.append([self.grid[0][i], self.grid[1][i], self.grid[2][i]])  # столбец i
        # диагонали
        lines.append([self.grid[0][0], self.grid[1][1], self.grid[2][2]])
        lines.append([self.grid[0][2], self.grid[1][1], self.grid[2][0]])

        for line in lines:
            if line[0] and line.count(line[0]) == 3:
                self.winner = line[0]
                return

        # ничья
        if all(cell for row in self.grid for cell in row):
            self.winner = 'Draw'

    def reset(self):
        self.__init__()
