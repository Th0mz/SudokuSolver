import display
from resolver import x, y, _
from time import sleep

tamanho = (41, 25)

def editar():
    novo_sudoku = [[_] * 9 for i in range(9)]
    display.curses.resize_term(tamanho[y], tamanho[x])

    a_correr = True
    update = True
    cursor = (0, 0)

    while a_correr:
        if update:
            display.gui("EDITAR", tamanho[x], novo_sudoku, pos_highLight=cursor, cor_highLight=display.curses.color_pair(5))
            update = False

            display.ecra.addstr(19, 2, "> Selecionar com wasd")
            display.ecra.addstr(20, 2, "> Usar os números parar por o número")
            display.ecra.addstr(21, 2, "> Reset posição [r]")
            display.ecra.addstr(22, 2, "> Sair guardando o sudoku [Enter]")
            display.ecra.addstr(23, 2, "> Sair sem guardar o sudoku [x]")
            display.ecra.refresh()

        key_pressed = display.ecra.getch()

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
        elif ord("1") <= key_pressed <= ord("9"):
            novo_sudoku[cursor[y]][cursor[x]] = int(chr(key_pressed))
            update = True
        elif key_pressed == ord("r"):
            novo_sudoku[cursor[y]][cursor[x]] = _
            update = True
        elif key_pressed == 10:
            a_correr = False
            guardar = True
        elif key_pressed == ord("x"):
            a_correr = False
            guardar = False

    if guardar:
        with open("sudoku.txt", "w") as ficheiro:
            ficheiro.write(str(novo_sudoku))
