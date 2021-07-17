from os import system as consola
import curses
import time

x = 0
y = 1


def init():
    """ Inicialização das propriedades da biblioteca curses """
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
    """ Voltar a mudar as propriedades para default, para assim
                para assim poder fechar o programa"""

    curses.curs_set(0)
    curses.echo()
    curses.endwin()    


def header(nome, tamanho_X, pos_y):
    """ Controi um header com um certo tamanho_X e um nome, ficando:
        
        ######################################################
        #                      Nome                          #
        ######################################################
     
        |------------------- TamanhoX -----------------------|
    """

    bordo = "#"

    # Conteudo da primeira e ultima linha do cabeçalho
    linha = bordo*(tamanho_X - 5)

    ecra.addstr(pos_y + 2, 2, linha, curses.color_pair(1))
    ecra.addstr(pos_y, 2, linha, curses.color_pair(1))

    # Bordo entre o nome
    ecra.addstr(pos_y + 1, 2, bordo, curses.color_pair(1))
    ecra.addstr(pos_y + 1, 2 + (tamanho_X - 6), bordo, curses.color_pair(1))

    # Posicionamento do nome no meio do espaço entro os 2 bordos
    ecra.addstr(pos_y + 1, 2 + ((tamanho_X - 5)//2 - len(nome) // 2), nome, curses.color_pair(2) + curses.A_BOLD)
    

def display_sudoku(sudoku, pos_y, pos_highLight = "default", cor_highLight="default"):
    """ Da display do sudoku no std.out """

    linha = "|"
    separador = "+-----------+-----------+-----------+"

    # Constroi a base do sudoku
    for i in range(4, 4*4 + 1):
        # Põe linhas (horizontais) no sudoku
        if i % 4 == 0:
            ecra.addstr(pos_y + i, 2, separador, curses.color_pair(3) + curses.A_BOLD)

        # Põe linhas (verticais) no sudoku
        for j in range(len(separador)):
            if j % 12 == 0 and i % 4 != 0: 
                ecra.addstr(pos_y + i, 2 + j, linha, curses.color_pair(3) + curses.A_BOLD)
    
    # Põe os números nos espaços da base 
    for y in range(len(sudoku)):

        quadrado_offset = y//3
        for x in range(len(sudoku[0])):
            if pos_highLight == (x, y):
                ecra.addstr(pos_y + 5 + y + quadrado_offset, 4 + (x * 4), str(sudoku[y][x]), cor_highLight)
            else:
                ecra.addstr(pos_y + 5 + y + quadrado_offset, 4 + (x * 4), str(sudoku[y][x]))


def gui(nome, tamanhoX, sudoku, pos_highLight = "default", cor_highLight="default"):
    """ Cria o frame com um header e por baixo o sudoku dando display desse frame """

    ecra.clear()
    # Criação do header
    header(nome, tamanhoX, 1)
    
    # Criação do sudoku
    if cor_highLight == "default":
            display_sudoku(sudoku, 1, pos_highLight = pos_highLight, cor_highLight=curses.color_pair(4))
    else:
        display_sudoku(sudoku, 1, pos_highLight = pos_highLight, cor_highLight=cor_highLight)

    ecra.refresh()