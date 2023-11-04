#https://blog.naver.com/PostView.naver?blogId=dnpc7848&logNo=221506783416&parentCategoryNo=&categoryNo=&viewDate=&isShowPopularPosts=false&from=postView
import pygame, sys
from pygame.locals import *
from rule import *

board_color1 = (153, 102, 000)
board_color2 = (153, 102, 51)
board_color3 = (204, 153, 000)
board_color4 = (204, 153, 51)
bg_color = (128, 128, 128)
black = (0, 0, 0)
blue = (0, 50, 255)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 200, 0)

fps = 60
fps_clock = pygame.time.Clock()

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Gomoku')
    screen.fill(bg_color)

    omok = Omok(surface)
    menu = Menu(surface)
    while True:
        run_game(screen, omok, menu)
        menu.is_countinue(omok)

def run_game(screen, omok, menu):
    omok.init_game()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
               pygame.terminate()
            elif event.type == MOUSEBUTTONUP:
                if not omok.check_board(event.pos):
                    if menu.check_rect(event.pos, omok):
                        ook.init_game()

        if omok.is_gameover:
            return
        
        pygame.display.update()
        fps_clock.tick(fps)

class Omok(object):
    def __init__(self, surface):
        self.board = [[0 for i in range(board_size)] for j in range(board_size)]
        self.menu Menu(surface)
        self.rule = Rule(self.board)
        self.surface = surface
        self.pixel_coords = []
        self.set_coords()
        self.set_image_font()
        self.is_show = True

    def init_game(self):
        self.turn = black_stone
        self.draw_board()
        self.menu.show_msg(empty)
        self.init_board()
        self.coords = []
        self.redos = []
        self.id = 1
        self.is_gameover = False

# 보드판 그리기'
