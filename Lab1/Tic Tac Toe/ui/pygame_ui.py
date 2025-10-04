import pygame
import sys
from core.board import Board

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_COLOR = (50, 50, 50)
X_COLOR = (200, 30, 30)
O_COLOR = (30, 30, 200)


class Game:
    def __init__(self):
        pygame.init()
        self.size = 300
        self.cell = self.size // 3
        self.screen = pygame.display.set_mode((self.size, self.size + 40))
        pygame.display.set_caption('Крестики-нолики')
        self.font = pygame.font.SysFont(None, 30)
        self.board = Board()

    def draw_grid(self):
        for i in range(1, 3):
            pygame.draw.line(self.screen, LINE_COLOR, (i*self.cell, 0), (i*self.cell, self.size), 3)
            pygame.draw.line(self.screen, LINE_COLOR, (0, i*self.cell), (self.size, i*self.cell), 3)

    def draw_marks(self):
        for r in range(3):
            for c in range(3):
                mark = self.board.grid[r][c]
                x = c * self.cell
                y = r * self.cell
                if mark == 'X':
                    pygame.draw.line(self.screen, X_COLOR,
                                     (x+20, y+20), (x+self.cell-20, y+self.cell-20), 5)
                    pygame.draw.line(self.screen, X_COLOR,
                                     (x+self.cell-20, y+20), (x+20, y+self.cell-20), 5)
                elif mark == 'O':
                    pygame.draw.circle(self.screen, O_COLOR,
                                       (x + self.cell//2, y + self.cell//2),
                                       self.cell//2 - 20, 5)

    def draw_status(self):
        if self.board.winner == 'Draw':
            text = 'Ничья!  (N или R — новая игра)'
        elif self.board.winner:
            text = f'Победитель: {self.board.winner}  (N или R — новая игра)'
        else:
            text = f'Ход: {self.board.current}  (N или R — новая игра)'
        img = self.font.render(text, True, BLACK)
        self.screen.blit(img, (10, self.size + 8))

    def run(self):
        clock = pygame.time.Clock()
        while True:
            for evt in pygame.event.get():
                if evt.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evt.type == pygame.KEYDOWN and evt.key in (pygame.K_r, pygame.K_n):
                    self.board.reset()
                if evt.type == pygame.MOUSEBUTTONDOWN and not self.board.winner:
                    mx, my = pygame.mouse.get_pos()
                    if my < self.size:
                        row = my // self.cell
                        col = mx // self.cell
                        self.board.make_move(row, col)

            self.screen.fill(WHITE)
            self.draw_grid()
            self.draw_marks()
            self.draw_status()
            pygame.display.flip()
            clock.tick(30)
