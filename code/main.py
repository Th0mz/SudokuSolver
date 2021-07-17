import display 
import resolver
import editar 
from time import sleep  

x = 0
y = 1
_ = ' '

# Inicializar sudoku já guardado no documento anteriormente
with open("sudoku.txt", "r") as ficheiro:
    sudoku = eval(ficheiro.readline())

# Funcionalidades de cada opção do menu
def resolver_func():
    global sudoku
    resolver.visualizacao_resolucao(sudoku)

def insta_func():
    global sudoku
    resolver.instantanea_resolucao(sudoku)

def editar_func():
    editar.editar()

def sair_func():
    exit()

# Opções no menu, gurdado o nome que vai ser 
# displayed e a função a executar

opcoes = [
    {"nome" : "> Visualizar algoritmo", "exec" : resolver_func},
    {"nome" : "> Resolver o sudoku ", "exec" : insta_func},
    {"nome" : "> Editar o sudoku", "exec" : editar_func},
    {"nome" : "> Sair", "exec" : sair_func} 
]

display.init()
resolver.init()

# Posição do cursor no menu
cursor = 0
num_opcoes = len(opcoes)

pos_y = 1
update = True

tamanho = (31, 10)

# Menu:
display.curses.resize_term(tamanho[y], tamanho[x])

while True:

    if update:
        display.ecra.clear()
        display.header("MENU", tamanho[x], pos_y)

        # Display de todas as opções dando highlight aquela que esta com o cursor
        for i in range(num_opcoes):
            if i == cursor:
                display.ecra.addstr(pos_y + i + 4, 2, opcoes[i]["nome"])
            else:
                 display.ecra.addstr(pos_y + i + 4, 2, opcoes[i]["nome"], display.curses.color_pair(3) + display.curses.A_BOLD)

        update = False
        display.ecra.refresh()
    
    # Obter teclas que são primidas
    key_pressed = display.ecra.getch()

    # Tendo a tecla que foi primida executar a funcionalidade correspondente
        # Update do cursor
    if key_pressed == ord('w'):
        cursor = (cursor - 1) % num_opcoes
        update = True
    elif key_pressed == ord('s'):
        cursor = (cursor + 1) % num_opcoes
        update = True

        # Executar funcionalidade
    elif key_pressed == 10:
        opcoes[cursor]["exec"]()
        update = True

        # Update tamanho ecrã
        display.curses.resize_term(tamanho[y], tamanho[x])

        # Update sudoku
        with open("sudoku.txt", "r") as ficheiro:
            sudoku = eval(ficheiro.readline())


display.end()