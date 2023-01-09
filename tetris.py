import sys
import pygame
import random

pygame.init()

# initialize the window
screen = pygame.display.set_mode((322+350, 642+100))
pygame.display.set_caption("My Tetris")
screen.fill((57, 19, 19))
screen.fill((0, 0, 0), pygame.Rect((175, 70), (322, 642)))

screen.fill((77, 77, 77), pygame.Rect((25, 90), (130, 130)))  # current hold
screen.fill((77, 77, 77), pygame.Rect((520, 90), (130, 600)))

dflt_clr = (140, 140, 140)  # the default block color - RGB(140, 140, 140)

# initialize the refresh rate
frame = 33.33  # ms per frame
g = 25  # gravity: frames per drop
frame_counter = 0
# pygame.time.set_timer(rate, 5 * 60 * 1000)


class Square(object):
    def __init__(self, topleft, color=dflt_clr):
        self.rect = pygame.Rect(topleft, (30, 30))
        self.img = screen.fill(color, self.rect)
        self.status = False  # Status False means there is tetromino. Status True means the square is clear.

    def change(self, new_color):
        self.img = screen.fill(new_color, self.rect)
        self.status = True

    def clear(self):
        self.img = screen.fill(dflt_clr, self.rect)
        self.status = False


# load the squares
board = [[Square((2 * x + 2 + x * 30 + 175, 2 * y + 2 + y * 30 + 70)) for x in range(10)] for y in range(20)]
T = (128, 0, 128)
L = (255, 165, 0)
J = (0, 0, 255)
I = (0, 255, 255)
Z = (255, 0, 0)
S = (0, 128, 0)
O = (255, 255, 0)
current = random.choice(["T", "L", "J", "I", "Z", "S", "O"])


# functions of tetromino movements
def create_a_tetro(type):
    if type == "T":
        board[0][3].change(T)  # load the flat side first
        board[0][4].change(T)
        board[0][5].change(T)
        pygame.display.update()
        pygame.time.delay(int(g * frame))
        board[0][3].clear()
        board[0][5].clear()
        board[1][3].change(T)
        board[1][4].change(T)
        board[1][5].change(T)
        pygame.display.update()
        return board[4, 0], board[3, 1], board[4, 1], board[5, 1]
    elif type == "L":
        board[0][3].change(L)  # load the flat side first
        board[0][4].change(L)
        board[0][5].change(L)
        pygame.display.update()
        pygame.time.delay(int(g * frame))
        board[0][3].clear()
        board[0][4].clear()
        board[1][3].change(L)
        board[1][4].change(L)
        board[1][5].change(L)
        pygame.display.update()
        return board[3, 0], board[3, 1], board[4, 1], board[5, 1]
    elif type == "J":
        board[0][3].change(L)  # load the flat side first
        board[0][4].change(L)
        board[0][5].change(L)
        pygame.display.update()
        pygame.time.delay(int(g * frame))
        board[0][4].clear()
        board[0][5].clear()
        board[1][3].change(L)
        board[1][4].change(L)
        board[1][5].change(L)
        pygame.display.update()
        return board[3, 0], board[3, 1], board[4, 1], board[5, 1]
    elif type == "I":
        board[0][2].change(I)
        board[0][3].change(I)
        board[0][4].change(I)
        board[0][5].change(I)
        board[0][6].change(I)
    elif type == "Z":
        pass
    elif type == "S":
        pass
    else:
        pass


def rotate_clockwise():
    pass


def rotate_anti():
    pass


def gravity_drop():
    pass


def left_shift():
    pass


def right_shift():
    pass


def soft_drop():
    pass


def hard_drop():
    pass


def hold():
    pass


# the game starts
pygame.display.update()
time = pygame.time.get_ticks()

going = True
while going:
    drop_dis = (0, 32)
    right_dis = (32, 0)
    left_dis = (-32, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            going = False
    #     elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
    #         if t.rect.right < 300:
    #             t.move(right_dis, screen, screen.blit(board, (0, 0)))
    #     elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
    #         if t.rect.left > 20:
    #             t.move(left_dis, screen, screen.blit(board, (0, 0)))
    #     elif event.type == rate and rate >= 150:  # the refresh rate decreases by 0.25 every 5 minutes
    #         rate /= 0.75
    # while pygame.key.get_pressed()[pygame.K_DOWN]:  # soft drop
    #     t.move(drop_dis, screen, screen.blit(board, (0, 0)))
    #     pygame.time.delay(100)
    #     if pygame.key.get_pressed()[pygame.K_DOWN]:
    #         break
    #
    # # hard drop
    #
    # if t.rect.bottom > 640:  # tetrominoes stop when reach the bottom
    #     drop_dis = (0, 0)
    #     right_dis = (0, 0)
    #     left_dis = (0, 0)

    if pygame.time.get_ticks() - time >= frame:  # this block controls the screen refresh and the gravitational dropping
        frame_counter += 1
        if frame_counter == g: gravity_drop()
        pygame.display.update()
        time = pygame.time.get_ticks()

sys.exit()
