import pygame
from pygame.locals import QUIT
import sys

pygame.init()
# 画面の大きさを600 * 600 ピクセルに設定
SURFACE = pygame.display.set_mode((600,600))
# 時間の設定
FPSCLOCK = pygame.time.Clock()

# 画面の描画
def display_paint():
    # 画面を真っ黒にする
    SURFACE.fill((0,0,0))
    for index in range(20):
        # 縦線が描かれる
        pygame.draw.line(SURFACE, (64, 64, 64), (index*30, 0),(index*30, 600))
        # 横線が描かれる
        pygame.draw.line(SURFACE, (64, 64, 64), (0, index*30),(600, index*30))
    # 画面を更新する
    pygame.display.update()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                # pygameの終了
                pygame.quit()
                # プログラムの終了
                sys.exit()
        display_paint()
        FPSCLOCK.tick(5)

if __name__ == "__main__":
    main()
