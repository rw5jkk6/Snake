import pygame
from pygame.locals import QUIT, Rect, KEYDOWN,K_LEFT,K_RIGHT,K_UP,K_DOWN
import sys

pygame.init()
SURFACE = pygame.display.set_mode((600,600))
FPSCLOCK = pygame.time.Clock()
(W,H)=(20,20)
SNAKE = []


def paint():
    SURFACE.fill((0,0,0))

    for body in SNAKE:
        pygame.draw.rect(SURFACE, (0, 255, 255), Rect(body[0]*30, body[1]*30, 30, 30))

    for index in range(20):
        # 縦線が描かれる
        pygame.draw.line(SURFACE, (64, 64, 64), (index*30, 0),(index*30, 600))
        # 横線が描かれる
        pygame.draw.line(SURFACE, (64, 64, 64), (0, index*30),(600, index*30))
    pygame.display.update()

def main():
    
    key = K_DOWN
    game_over = False
    SNAKE.append((int(W/2), (int(H/2))))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                key = event.key
        
        if not game_over:
            if key == K_LEFT:
                head = (SNAKE[0][0]-1, SNAKE[0][1])
            elif key == K_RIGHT:
                head = (SNAKE[0][0]+1, SNAKE[0][1])
            elif key == K_UP:
                head = (SNAKE[0][0], SNAKE[0][1]-1)
            elif key == K_DOWN:
                head = (SNAKE[0][0], SNAKE[0][1]+1)
        

        SNAKE.insert(0, head)
        SNAKE.pop()

        paint()
        FPSCLOCK.tick(5)

if __name__ == "__main__":
    main()
