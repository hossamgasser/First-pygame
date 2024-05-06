import pygame
from pygame.locals import *

pygame.init()

screen_width, screen_height = 300, 300

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My First Game: TicTacToe")

font = pygame.font.SysFont(None, 40)

markers = []
clicked = False
pos = []
player = 1
winner = 0
game_over = False
blue =(0, 0, 255)
turn = 0


X_IMG = pygame.image.load("assets/X.png")
resized_x = pygame.transform.scale(X_IMG, (50, 50))
O_IMG = pygame.image.load("assets/O.png")
resized_O = pygame.transform.scale(O_IMG, (50, 50))

again_rect = Rect(screen_width // 2 - 85, screen_height // 2 + 10, 170, 50)

def draw_grid():
    line_width = 6
    bg = (255, 255, 200)
    grid = (50, 50 , 50)
    screen.fill(bg)
    for x in range (1, 3):
        pygame.draw.line(screen, grid, (0, x * 100), (screen_width, x * 100), line_width)
        pygame.draw.line(screen, grid, (x * 100, 0), (x * 100, screen_height), line_width)
def initialize_markers():
    for x in range(3):
        row = [0] * 3
        markers.append(row)

def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x: 
            if y == 1:
                screen.blit(resized_x, (x_pos * 100 + 25, y_pos * 100 + 25))
            if y == -1:
                screen.blit(resized_O, (x_pos * 100 + 25, y_pos * 100 + 25))
            y_pos += 1
        x_pos += 1

def check_winner():
    y_pos = 0
    global winner
    global game_over
    global turn

    for x in markers:
        if sum(x) == 3:
            winner = 1
            game_over = True
        if sum(x) == -3:
            winner = 2
            game_over = True

        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == 3:
            winner = 1
            game_over = True
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == -3:
            winner = 2
            game_over = True
        y_pos += 1
    
    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[2][0] + markers[1][1] + markers[0][2] == 3:
        winner = 1
        game_over = True

    if markers[0][0] + markers[1][1] + markers[2][2] == -3 or markers[2][0] + markers[1][1] + markers[0][2] == -3:
        winner = 2
        game_over = True
    if turn == 9:
        game_over = True
    

def display_win(winner):
    win_text = "Player " + str(winner) + " wins!"
    win_image = font.render(win_text, True, blue)
    pygame.draw.rect(screen, (0, 255, 0), (screen_width // 2 - 100, screen_height // 2 - 50, 200, 50))
    screen.blit(win_image, (screen_width // 2 - 95, screen_height // 2 - 40))

    again_text = "Play again?"
    again_img = font.render(again_text, True, blue)
    pygame.draw.rect(screen, (0, 255, 0), again_rect)
    screen.blit(again_img, ((screen_width // 2 - 80, screen_height // 2 + 20)))

def display_draw():
    draw_text = "The game is drawn!"
    draw_image = font.render(draw_text, True, blue)
    pygame.draw.rect(screen, (0, 255, 0), (screen_width // 2 - 135, screen_height // 2 - 50, 275, 50))
    screen.blit(draw_image, (screen_width // 2 - 135, screen_height // 2 - 40))

    again_text = "Play again?"
    again_img = font.render(again_text, True, blue)
    pygame.draw.rect(screen, (0, 255, 0), again_rect)
    screen.blit(again_img, ((screen_width // 2 - 80, screen_height // 2 + 20)))

initialize_markers()
run = True 
while run: 

    draw_grid()
    draw_markers()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if game_over == False:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0]
                cell_y = pos[1]
                if markers[cell_x // 100][cell_y // 100] == 0:
                    markers[cell_x // 100][cell_y // 100] = player
                    player *=-1         # makes switching player values easier -1 to 1 and vice versa
                    turn += 1
                    check_winner()
    if game_over == True:
        if winner != 0:
            display_win(winner)
        if winner == 0:
            display_draw()
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                markers = []
                pos = []
                player = 1
                winner = 0
                game_over = False
                turn = 0

                initialize_markers()

    pygame.display.update()

pygame.quit()
