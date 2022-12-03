import sys
import pygame

pygame.init()

# initialize the window
screen = pygame.display.set_mode((322, 642))
pygame.display.set_caption("My Tetris")
screen.fill((0, 0, 0))
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
board = [[Square((2 * x + 2 + x * 30, 2 * y + 2 + y * 30)) for x in range(10)] for y in range(20)]
T = (128, 0, 128)
L = (255, 165, 0)
J = (0, 0, 255)
I = (0, 255, 255)
Z = (255, 0, 0)
S = (0, 128, 0)
O = (255, 255, 0)


# functions of tetromino movements
def create_a_tetro(type):
    if type == "T":
        board[3, 0].change(T)  # load the flat side first
        board[4, 0].change(T)
        board[5, 0].change(T)
        pygame.time.delay(g*frame)
        pygame.display.update()
        board[3, 0].clear()
        board[5, 0].clear()
        board[3, 1].change(T)
        board[4, 1].change(T)
        board[5, 1].change(T)
        pygame.display.update()
        return board[4, 0], board[3, 1], board[4, 1], board[5, 1]
    elif type == "L":
        board[3, 0].change(L)  # load the flat side first
        board[4, 0].change(L)
        board[5, 0].change(L)
        pygame.time.delay(g*frame)
        pygame.display.update()
        board[4, 0].clear()
        board[5, 0].clear()
        board[3, 1].change(L)
        board[4, 1].change(L)
        board[5, 1].change(L)
        pygame.display.update()
        return board[3, 0], board[3, 1], board[4, 1], board[5, 1]
    elif type == "J":
        pass
    elif type == "I":
        pass
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
