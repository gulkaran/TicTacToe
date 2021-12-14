import pygame
import numpy

# window creation
pygame.init()
WIDTH = 500
HEIGHT = 650
win_size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(win_size)
icon = pygame.image.load("imgs/tic-tac-toe.png")
pygame.display.set_icon(icon)

pygame.display.set_caption('Tic Tac Toe')
font = pygame.font.SysFont("Cambria", 30)
purple = (87, 77, 112)
white = (234, 241, 249)
blue = (63, 192, 221)
pink = (237, 85, 169)
screen.fill(purple)
gameover = False
run = True
board_col = 3
board_row = 3
player = 1

global clicked_col
global clicked_row

# board lines


def board_lines():
    pygame.draw.line(screen, white, (166, 20), (166, 480), 10)
    pygame.draw.line(screen, white, (332, 20), (332, 480), 10)
    pygame.draw.line(screen, white, (20, 166), (480, 166), 10)
    pygame.draw.line(screen, white, (20, 332), (480, 332), 10)


board_lines()


board = numpy.zeros((board_row, board_col))


def marked(row, col, player):
    board[row][col] = player


def available(row, col):
    return board[row][col] == 0


def draw():
    pygame.draw.line(screen, blue, (clicked_col * 166 + 35, clicked_row * 166 +
                                    166 - 35), (clicked_col * 166 + 166 - 35, clicked_row * 166 + 35), 30)
    pygame.draw.line(screen, blue, (clicked_col * 166 + 35, clicked_row * 166 + 35),
                     (clicked_col * 166 + 166 - 35, clicked_row * 166 + 166 - 35), 30)


def draw2():
    pygame.draw.circle(screen, pink, (clicked_col * 166 + 83, clicked_row * 166 + 83), 55, 20)


def win_check(player):
    # vertical
    for col in range(board_col):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_win(col, player)
            return True

    # horizontal
    for row in range(board_row):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_win(row, player)
            return True

    # diagonal
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_diagonal_ascending(player)
        return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_diagonal_desc(player)
        return True

    return False


def draw_vertical_win(col, player):
    posx = col * 166 + 83
    if player == 1:
        colour = blue
    elif player == 2:
        colour = pink

    pygame.draw.line(screen, colour, (posx, 20), (posx, 500 - 20), 15)


def draw_horizontal_win(row, player):
    posy = row * 166 + 83
    if player == 1:
        colour = blue
    elif player == 2:
        colour = pink

    pygame.draw.line(screen, colour, (20, posy), (500 - 20, posy), 15)


def draw_diagonal_ascending(player):
    if player == 1:
        colour = blue
    elif player == 2:
        colour = pink

    pygame.draw.line(screen, colour, (20, 500 - 20), (500 - 20, 20), 15)


def draw_diagonal_desc(player):
    if player == 1:
        colour = blue
    elif player == 2:
        colour = pink

    pygame.draw.line(screen, colour, (20, 20), (500 - 20, 500 - 20), 15)


def restart():
    screen.fill(purple)
    board_lines()
    button()
    for row in range(board_row):
        for col in range(board_col):
            board[row][col] = 0


def button():
    button1 = pygame.Rect(50, 520, 400, 75)
    button2 = pygame.Rect(53, 523, 394, 69)
    pygame.draw.rect(screen, white, button1)
    pygame.draw.rect(screen, purple, button2)

    title = font.render("Press 'R' To Restart", 1, white)
    screen.blit(title, (110, 535))


button()


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and not gameover:
            mx = event.pos[0]
            my = event.pos[1]
            clicked_row = my // 166
            clicked_col = mx // 166

            if available(clicked_row, clicked_col):
                if player == 1:
                    marked(clicked_row, clicked_col, 1)
                    win_check(player)
                    if win_check(player):
                        gameover = True
                    player = 2
                    draw()
                elif player == 2:
                    marked(clicked_row, clicked_col, 2)
                    win_check(player)
                    if win_check(player):
                        gameover = True
                    player = 1
                    draw2()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player = 1
                gameover = False
    pygame.display.update()

pygame.quit()
