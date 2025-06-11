import pygame
from pygame.locals import *
from OpenGL.GL import *
import math
import sys
import tkinter as tk
from tkinter import messagebox

# Game logic functions
def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    return None

def is_draw(board):
    return all(all(cell is not None for cell in row) for row in board)

# Minimax for CPU moves
def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == "O": return 1
    if winner == "X": return -1
    if is_draw(board):    return 0
    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] is None:
                    board[i][j] = "O"
                    score = minimax(board, False)
                    board[i][j] = None
                    best = max(score, best)
        return best
    best = math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                board[i][j] = "X"
                score = minimax(board, True)
                board[i][j] = None
                best = min(score, best)
    return best


def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                board[i][j] = "O"
                score = minimax(board, False)
                board[i][j] = None
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Choose game mode via Pygame window
def choose_mode(width, height):
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Select Mode")
    font = pygame.font.SysFont(None, 48)
    btn1 = pygame.Rect(width//4 - 100, height//2 - 50, 240, 100)
    btn2 = pygame.Rect(3*width//4 - 100, height//2 - 50, 210, 100)
    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit(); sys.exit()
            if e.type == MOUSEBUTTONDOWN:
                if btn1.collidepoint(e.pos): return True
                if btn2.collidepoint(e.pos): return False
        
        # Green gradient background
        for i in range(height):
            r = int(0 + (i / height) * 34)  # Start from a lighter green, end darker
            g = int(100 + (i / height) * 120) # Green component
            b = int(0 + (i / height) * 34)  # Blue component
            pygame.draw.line(screen, (r, g, b), (0, i), (width, i))

        # Draw abstract trees and bushes
        # Larger bush on left
        pygame.draw.ellipse(screen, (40, 150, 40), (50, height - 200, 150, 100)) # Darker green
        pygame.draw.ellipse(screen, (60, 180, 60), (70, height - 220, 130, 90)) # Lighter green

        # Smaller bush on right
        pygame.draw.ellipse(screen, (40, 150, 40), (width - 180, height - 150, 120, 80)) # Darker green
        pygame.draw.ellipse(screen, (60, 180, 60), (width - 160, height - 170, 100, 70)) # Lighter green

        # Tree 1 (updated for stacked leaves)
        pygame.draw.rect(screen, (100, 70, 40), (120, height - 150, 20, 100)) # Trunk 1
        pygame.draw.circle(screen, (34, 139, 34), (130, height - 160), 40) # Bottom leaf layer
        pygame.draw.circle(screen, (34, 139, 34), (130, height - 190), 35) # Middle leaf layer
        pygame.draw.circle(screen, (34, 139, 34), (130, height - 220), 30) # Top leaf layer

        # Tree 2 (updated for stacked leaves)
        pygame.draw.rect(screen, (100, 70, 40), (width - 100, height - 120, 25, 90)) # Trunk 2
        pygame.draw.circle(screen, (34, 139, 34), (width - 87, height - 130), 45) # Bottom leaf layer
        pygame.draw.circle(screen, (34, 139, 34), (width - 87, height - 165), 40) # Middle leaf layer
        pygame.draw.circle(screen, (34, 139, 34), (width - 87, height - 200), 35) # Top leaf layer

        # Draw rock-like X on the floor
        x_rock_pos_x = width // 4
        x_rock_pos_y = height - 70
        rock_color_x = (80, 80, 80) # Dark grey
        pygame.draw.line(screen, rock_color_x, (x_rock_pos_x - 30, x_rock_pos_y - 30), (x_rock_pos_x + 30, x_rock_pos_y + 30), 10) # X arm 1
        pygame.draw.line(screen, rock_color_x, (x_rock_pos_x - 30, x_rock_pos_y + 30), (x_rock_pos_x + 30, x_rock_pos_y - 30), 10) # X arm 2

        # Draw rock-like O on the floor
        o_rock_pos_x = 3 * width // 4
        o_rock_pos_y = height - 80
        rock_color_o = (120, 120, 120) # Medium grey
        pygame.draw.circle(screen, rock_color_o, (o_rock_pos_x, o_rock_pos_y), 40, 10) # O circle

        # Add Title "Tic Tac Toe" in black and red
        title_font = pygame.font.SysFont(None, 80)
        tic_tac_text = title_font.render("Tic Tac ", True, (0, 0, 0)) # Black
        toe_text = title_font.render("Toe", True, (255, 0, 0)) # Red

        # Calculate total width for centering
        total_title_width = tic_tac_text.get_width() + toe_text.get_width()
        start_x = (width - total_title_width) // 2
        title_y = height // 8 # Position near the top

        screen.blit(tic_tac_text, (start_x, title_y))
        screen.blit(toe_text, (start_x + tic_tac_text.get_width(), title_y))

        pygame.draw.rect(screen, (70, 130, 180), btn1, border_radius=15) # SteelBlue for Single Player
        pygame.draw.rect(screen, (220, 90, 90), btn2, border_radius=15) # Light Red for Two Player
        screen.blit(font.render("Single Player", True, (255,255,255)), (btn1.x+10, btn1.y+30))
        screen.blit(font.render("Two Player", True, (255,255,255)), (btn2.x+20, btn2.y+30))
        pygame.display.flip()

# Draw functions using OpenGL
def draw_grid(w,h):
    glColor3f(0.8, 0.8, 0.8) # Lighter grey for grid lines
    glLineWidth(8)
    glBegin(GL_LINES)
    for x in (w/3, 2*w/3): glVertex2f(x,0); glVertex2f(x,h)
    for y in (h/3, 2*h/3): glVertex2f(0,y); glVertex2f(w,y)
    glEnd()

def draw_x(r,c,w,h):
    pad = w/3 * 0.2
    x1,y1 = c*w/3 + pad, r*h/3 + pad
    x2,y2 = (c+1)*w/3 - pad, (r+1)*h/3 - pad
    glColor3f(0.4, 0.4, 0.4) # Dark grey for rock-like X
    glLineWidth(14)
    glBegin(GL_LINES)
    glVertex2f(x1,y1); glVertex2f(x2,y2)
    glVertex2f(x1,y2); glVertex2f(x2,y1)
    glEnd()

def draw_o(r,c,w,h):
    cx,cy = c*w/3 + w/6, r*h/3 + h/6
    rad = w/3 * 0.3
    glColor3f(0.5, 0.5, 0.5) # Medium grey for rock-like O
    glLineWidth(14)
    glBegin(GL_LINE_LOOP)
    for i in range(32):
        th = 2*math.pi*i/32
        glVertex2f(cx + math.cos(th)*rad, cy + math.sin(th)*rad)
    glEnd()

# Main loop with restart option
def main():
    pygame.init()
    tk.Tk().withdraw()
    width,height = 600,600

    while True:
        mode = choose_mode(width, height)
        pygame.display.set_mode((width,height), DOUBLEBUF|OPENGL)
        pygame.display.set_caption("Tic Tac Toe")
        glClearColor(1.0, 1.0, 0.6, 1) # Yellowish background for game board
        glMatrixMode(GL_PROJECTION); glLoadIdentity(); glOrtho(0,width,height,0,-1,1)
        glMatrixMode(GL_MODELVIEW); glLoadIdentity()

        board = [[None]*3 for _ in range(3)]
        current = 'X'; game_over = False; winner = None
        clock = pygame.time.Clock()

        while not game_over:
            glClear(GL_COLOR_BUFFER_BIT)
            draw_grid(width,height)
            for i in range(3):
                for j in range(3):
                    if board[i][j]=='X': draw_x(i,j,width,height)
                    if board[i][j]=='O': draw_o(i,j,width,height)
            pygame.display.flip()

            for e in pygame.event.get():
                if e.type==QUIT:
                    pygame.quit(); sys.exit()
                if e.type==MOUSEBUTTONDOWN:
                    mx,my = e.pos
                    c,r = int(mx//(width/3)), int(my//(height/3))
                    if 0<=r<3 and 0<=c<3 and board[r][c] is None:
                        board[r][c] = current
                        winner = check_winner(board)
                        if not winner and not is_draw(board):
                            if mode:  # single player
                                move = best_move(board)
                                if move:
                                    board[move[0]][move[1]] = 'O'
                                winner = check_winner(board)
                                if winner or is_draw(board):
                                    game_over = True
                            else:  # two player
                                current = 'O' if current == 'X' else 'X'
                        else:
                            game_over = True
            clock.tick(60)

        # Render final state
        glClear(GL_COLOR_BUFFER_BIT)
        draw_grid(width,height)
        for i in range(3):
            for j in range(3):
                if board[i][j]=='X': draw_x(i,j,width,height)
                if board[i][j]=='O': draw_o(i,j,width,height)
        pygame.display.flip()
        pygame.time.delay(300)

        # Show result and ask to play again
        msg = f"{winner} Wins!" if winner else "Draw!"
        again = messagebox.askyesno("Game Over", msg + "\nPlay Again?")
        if not again:
            pygame.quit(); break

if __name__=='__main__':
    main()
