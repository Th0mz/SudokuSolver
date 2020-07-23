from os import system as consola
import curses
import time

x = 0
y = 1


def init():
    global ecra
    # Inicializar ecra
    ecra = curses.initscr()
    
    # Definições do ecrã
    curses.noecho()
    curses.curs_set(0)

    # Cores
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_WHITE)


def end():
    curses.curs_set(0)
    curses.echo()
    curses.endwin()    


def header(nome, tamanho_X, pos_y):
    """ Da display de um header com  """
    bordo = "#"

    linha = bordo*(tamanho_X - 5)
    ecra.addstr(pos_y, 2, linha, curses.color_pair(1))

    ecra.addstr(pos_y + 1, 2, bordo, curses.color_pair(1))
    ecra.addstr(pos_y + 1, 2 + ((tamanho_X - 5)//2 - len(nome) // 2), nome, curses.color_pair(2) + curses.A_BOLD)
    ecra.addstr(pos_y + 1, 2 + (tamanho_X - 6), bordo, curses.color_pair(1))
    
    ecra.addstr(pos_y + 2, 2, linha, curses.color_pair(1))

def display_sudoku(sudoku, pos_y, pos_highLight = "default", cor_highLight="default"):
    """ Da display da tabela do sudoku no std.out """

    linha = "|"
    separador = "+-----------+-----------+-----------+"

    # Por linhas (verticais) no sudoku
    for i in range(4, 4*4 + 1):
        if i % 4 == 0:
            ecra.addstr(pos_y + i, 2, separador, curses.color_pair(3) + curses.A_BOLD)

        for j in range(len(separador)):
            if j % 12 == 0 and i % 4 != 0: 
                ecra.addstr(pos_y + i, 2 + j, linha, curses.color_pair(3) + curses.A_BOLD)
    
    for y in range(len(sudoku)):
        for x in range(len(sudoku[0])):
            quadrado_offset = y//3
            try:
                if pos_highLight == (x, y):
                    ecra.addstr(pos_y + 5 + y + quadrado_offset, 4 + (x * 4), str(sudoku[y][x]), cor_highLight)
                else:
                    ecra.addstr(pos_y + 5 + y + quadrado_offset, 4 + (x * 4), str(sudoku[y][x]))
            except curses.error:
                pass


def gui(nome, tamanhoX, sudoku, pos_highLight = "default", cor_highLight="default"):

    ecra.clear()
    header(nome, tamanhoX, 1)
    if cor_highLight == "default":
            display_sudoku(sudoku, 1, pos_highLight = pos_highLight, cor_highLight=curses.color_pair(4))
    else:
        display_sudoku(sudoku, 1, pos_highLight = pos_highLight, cor_highLight=cor_highLight)

    ecra.refresh()