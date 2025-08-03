import pygame
import random

pygame.init()

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
GRID_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

SHAPES = [
    [['.', 'O', '.'], ['O', 'O', 'O']],
    [['.', 'T', 'T'], ['T', 'T', '.']],
    [['L', 'L', 'L'], ['.', '.', 'L']],
    [['I', 'I', 'I', 'I']],
    [['Z', 'Z', '.'], ['.', 'Z', 'Z']],
    [['S', 'S', '.'], ['.', 'S', 'S']],
    [['.', 'J', 'J'], ['J', 'J', '.']]
]

COLORS = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
    (255, 165, 0), (0, 255, 255), (128, 0, 128)
]

class Piece:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = random.choice(COLORS)

    def rotate(self):
        self.shape = list(zip(*self.shape[::-1]))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece = self.new_piece()
        self.next_piece = self.new_piece()
        self.game_over = False
        self.score = 0
        self.font = pygame.font.SysFont('Arial', 24)

    def new_piece(self):
        shape = random.choice(SHAPES)
        x = GRID_WIDTH // 2 - len(shape[0]) // 2
        y = 0
        return Piece(x, y, shape)
    
    def draw_grid(self):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, cell, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(self.screen, GRAY, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)

    def draw_piece(self, piece):
        for y, row in enumerate(piece.shape):
            for x, cell in enumerate(row):
                if cell != '.':
                    pygame.draw.rect(
                        self.screen, piece.color,
                        ((piece.x + x) * GRID_SIZE, (piece.y + y) * GRID_SIZE, GRID_SIZE, GRID_SIZE)
                    )

    def draw_next_piece(self):
        font = pygame.font.SysFont('Arial', 20)
        text_surface = font.render('Próxima', True, WHITE)
        self.screen.blit(text_surface, (SCREEN_WIDTH - 120, 50))
        
        for y, row in enumerate(self.next_piece.shape):
            for x, cell in enumerate(row):
                if cell != '.':
                    pygame.draw.rect(
                        self.screen, self.next_piece.color,
                        ((SCREEN_WIDTH - 100 + x * GRID_SIZE), (80 + y * GRID_SIZE), GRID_SIZE, GRID_SIZE)
                    )

    def collision(self):
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell != '.':
                    grid_x = self.current_piece.x + x
                    grid_y = self.current_piece.y + y
                    
                    if not (0 <= grid_x < GRID_WIDTH and 0 <= grid_y < GRID_HEIGHT):
                        return True
                    if self.grid[grid_y][grid_x]:
                        return True
        return False
        
    def lock_piece(self):
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell != '.':
                    self.grid[self.current_piece.y + y][self.current_piece.x + x] = self.current_piece.color
        self.clear_lines()
        self.current_piece = self.next_piece
        self.next_piece = self.new_piece()
        if self.collision():
            self.game_over = True

    def clear_lines(self):
        lines_cleared = 0
        new_grid = [row for row in self.grid if not all(cell for cell in row)]
        lines_cleared = GRID_HEIGHT - len(new_grid)
        self.score += 100 * (2 ** (lines_cleared - 1)) if lines_cleared > 0 else 0
        
        while len(new_grid) < GRID_HEIGHT:
            new_grid.insert(0, [0 for _ in range(GRID_WIDTH)])
        self.grid = new_grid

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    
    game = Game(screen)
    fall_time = 0
    fall_speed = 500

    while not game.game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.current_piece.move(-1, 0)
                    if game.collision():
                        game.current_piece.move(1, 0)
                if event.key == pygame.K_RIGHT:
                    game.current_piece.move(1, 0)
                    if game.collision():
                        game.current_piece.move(-1, 0)
                if event.key == pygame.K_DOWN:
                    game.current_piece.move(0, 1)
                    if game.collision():
                        game.current_piece.move(0, -1)
                        game.lock_piece()
                if event.key == pygame.K_UP:
                    game.current_piece.rotate()
                    if game.collision():
                        game.current_piece.rotate()
                        game.current_piece.rotate()
                        game.current_piece.rotate()

        fall_time += clock.get_raw_time()
        clock.tick(FPS)
        
        if fall_time > fall_speed:
            fall_time = 0
            game.current_piece.move(0, 1)
            if game.collision():
                game.current_piece.move(0, -1)
                game.lock_piece()

        screen.fill(BLACK)
        game.draw_grid()
        game.draw_piece(game.current_piece)
        game.draw_next_piece()

        score_text = game.font.render(f"Score: {game.score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        if game.game_over:
            game_over_font = pygame.font.SysFont('Arial', 40)
            game_over_text = game_over_font.render("Game Over", True, (255, 255, 255))
            text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
            screen.blit(game_over_text, text_rect)

        pygame.display.flip()

    pygame.quit()
    
if __name__ == "__main__":
    main()
