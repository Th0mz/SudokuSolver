import display
from resolver import x, y, _
from time import sleep

tamanho = (41, 25)

def editar():
    """ É um loop que dado o input do utilizador cria um novo sudoku
        que pode ser resolvido usando os algoritmos desenvolvidos """

    # Inicialização de um novo sudoku vazio
    novo_sudoku = [[_] * 9 for i in range(9)]
    display.curses.resize_term(tamanho[y], tamanho[x])

    a_correr = True
    update = True

    # Posição do cursor
    cursor = (0, 0)

    while a_correr:
        if update:
            # Display do sudoku que esta a ser editado (inicialmente vazio [novo_sudoku])
            display.gui("EDITAR", tamanho[x], novo_sudoku, pos_highLight=cursor, cor_highLight=display.curses.color_pair(5))
            update = False

            # Display das intruções de como usar o editor
            display.ecra.addstr(19, 2, "> Selecionar com wasd")
            display.ecra.addstr(20, 2, "> Usar os números parar por o número")
            display.ecra.addstr(21, 2, "> Reset posição [r]")
            display.ecra.addstr(22, 2, "> Sair guardando o sudoku [Enter]")
            display.ecra.addstr(23, 2, "> Sair sem guardar o sudoku [x]")
            display.ecra.refresh()

        # Obter teclas que são primidas
        key_pressed = display.ecra.getch()

        # Tendo a tecla que foi primida executar a funcionalidade correspondente
            # Update do cursor
        if key_pressed == ord('w'):
            cursor = (cursor[x], (cursor[y] - 1) % 9)
            update = True
        elif key_pressed == ord('s'):
            cursor = (cursor[x], (cursor[y] + 1) % 9)
            update = True
        elif key_pressed == ord('a'):
            cursor = ((cursor[x] - 1) % 9, cursor[y])
            update = True
        elif key_pressed == ord('d'):
            cursor = ((cursor[x] + 1) % 9, cursor[y])
            update = True

            # Update do número na posição do cursor 
        elif ord("1") <= key_pressed <= ord("9"):
            novo_sudoku[cursor[y]][cursor[x]] = int(chr(key_pressed))
            update = True
        elif key_pressed == ord("r"):
            novo_sudoku[cursor[y]][cursor[x]] = _
            update = True

            # Sair do modo de edição
        elif key_pressed == 10:
            a_correr = False
            guardar = True
        elif key_pressed == ord("x"):
            a_correr = False
            guardar = False

    # Guardar a edição feita
    if guardar:
        with open("sudoku.txt", "w") as ficheiro:
            ficheiro.write(str(novo_sudoku))
