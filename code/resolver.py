# Para resolver este problema vou usar um algoritmo de backtrack parecido com o
# procedimento do prolog ou até mesmo o DFS 
#
# Em cada casa vazia escolhe um valor possível e continua para a proxima casa se
# por acaso um dos valores for escolhido mal o quadro terna-se unsolvable e o algoritmo
# da backtrack até a ultima escolha feita

from display import gui
import display
from time import sleep

x = 0
y = 1

_ = ' '
nao_parar = True
tamanho = (41, 21)


def init():
    """ Inicializar o resultado do sudoku """
    global sudoku_resolvido
    sudoku_resolvido = [[] for i in range(9)]

def posicoes_possiveis(sudoku, posicao):
    """ Obtem todos os numeros possiveis para um espaco dado pela posicao """

    posicoes_possiveis = list(range(1, 10))

    # Verificar coluna 
    for i in range(len(sudoku)):
        numero = sudoku[i][posicao[x]] 
        if numero in posicoes_possiveis:
            posicoes_possiveis.remove(numero)

    # Verificar linha
    for i in range(len(sudoku[posicao[y]])):
        numero = sudoku[posicao[y]][i] 
        if numero in posicoes_possiveis:
            posicoes_possiveis.remove(numero)

    # Verifica quadrado
    quadrado = ((posicao[x] // 3) * 3, (posicao[y] // 3) * 3)
    for i in range(3):
        for j in range(3):
            numero = sudoku[quadrado[y] + i][quadrado[x] + j]
            if numero in posicoes_possiveis:
                posicoes_possiveis.remove(numero)

    return posicoes_possiveis


def espacos_brancos(sudoku):
    """ Conta o numero de espaços brancos do sudoku """
    num_espacos = 0 

    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == _:
                num_espacos += 1

    return num_espacos


def resolve(sudoku, velocidade, gui_mode):
    """ Resolve o sudoku passado como argumento usando um algoritmo de backtrack """
    num_espacos = espacos_brancos(sudoku)
    global nao_parar

    # Percorre todas as posições do sudoku
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            # Verificar se é um espaço vazio
            if sudoku[i][j] == _:
                numeros_possiveis = posicoes_possiveis(sudoku, (j, i))
                num_espacos -= 1

                # Testa todas as posições possiveis para aquele espaço
                for numero in numeros_possiveis:
                    sudoku[i][j] = numero

                    if gui_mode and nao_parar:
                        gui("A RESOLVER...", tamanho[x], sudoku, pos_highLight=(j, i))
                        sleep(velocidade)

                    if num_espacos == 0:
                        nao_parar = False
                    
                    # Chamada recursiva
                    resolve(sudoku, velocidade, gui_mode)
                    sudoku[i][j] = _
                    num_espacos += 1

                return
    
    copia_sudoku(sudoku)


def copia_sudoku(sudoku):
    """ Copia o sudoku para a variavel global sudoku_resolvido """
    global sudoku_resolvido

    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            sudoku_resolvido[i].append(sudoku[i][j])


def visualizacao_resolucao(sudoku):
    global sudoku_resolvido
    display.curses.resize_term(tamanho[y], tamanho[x])

    gui("SUDOKU", tamanho[x], sudoku)

    display.ecra.addstr(18, 3, "> Pressiona qualquer tecla para \n    resolver ")
    display.ecra.getch()

    resolve(sudoku, 0.1, True)
    
    gui("SUDOKU", tamanho[x], sudoku_resolvido)
    display.ecra.addstr(19, 3, "> Pressiona qualquer tecla para sair ")
    sudoku_resolvido = [[] for i in range(9)]
    display.ecra.getch()

def instantanea_resolucao(sudoku):
    global sudoku_resolvido
    display.curses.resize_term(tamanho[y], tamanho[x])

    gui("SUDOKU", tamanho[x], sudoku)

    display.ecra.addstr(18, 3, "> Pressiona qualquer tecla para \n    resolver ")
    display.ecra.getch()

    resolve(sudoku, 0.1, False)
    
    gui("SUDOKU", tamanho[x], sudoku_resolvido)
    display.ecra.addstr(19, 3, "> Pressiona qualquer tecla para sair ")
    sudoku_resolvido = [[] for i in range(9)]
    display.ecra.getch()
