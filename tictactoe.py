table = [' ' for i in range(9)]
player = 'X'
is_not_game_over = True

def print_table():
    global table
    t = lambda x: table[x]
    print(
        '+ --- + --- + --- +     + --- + --- + --- +\n'
        f'|  {t(0)}  |  {t(1)}  |  {t(2)}  |     |  1  |  2  |  3  |\n'
        '+ --- + --- + --- +     + --- + --- + --- +\n'
        f'|  {t(3)}  |  {t(4)}  |  {t(5)}  |     |  4  |  5  |  6  |\n'
        '+ --- + --- + --- +     + --- + --- + --- +\n'
        f'|  {t(6)}  |  {t(7)}  |  {t(8)}  |     |  7  |  8  |  9  |\n'
        '+ --- + --- + --- +     + --- + --- + --- +\n'
    )

def check_table():
    global table, is_not_game_over

    # ROW CHECK
    for i in range(3):
        if (table[i] == table[i+3] == table[i+6]) and table[i] != ' ':
            print(f'The winner is: \'{table[i]}\'')
            is_not_game_over = False
            return

    # COLUMN CHECK
    for i in range(0, 4, 3):
        if (table[i] == table[i+1] == table[i+2]) and table[i] != ' ':
            print(f'The winner is: \'{table[i]}\'')
            is_not_game_over = False
            return

    # DIAGONAL CHECK
    for i in range(0, 3, 2):
        if (table[i] == table[4] == table[8-i]) and table[i] != ' ':
            print(f'The winner is: \'{table[i]}\'')
            is_not_game_over = False
            return

    if ' ' in table:
        return

    print('No winner')
    is_not_game_over = False

def get_input():
    global table, player
    while (True):
        inp = input(f'{player}: ')
        if inp not in [str(i+1) for i in range(9)]:
            print('[ERROR] Should be number from 1-9!\n')
        elif int(inp) < 1 or int(inp) > 9:
            print('[ERROR] Should be number from 1-9!\n')
        elif table[int(inp)-1] != ' ':
            print(f'[ERROR] Box {inp} is not empty!\n')
        else:
            table[int(inp)-1] = player
            player = 'X' if player == 'O' else 'O'
            break

if __name__ == '__main__':
    print('\n              [ TIC-TAC-TOE ]\n')
    print_table()
    while is_not_game_over:
        get_input()
        print_table()
        check_table()
    print('\n               [ GAME OVER ]\n')
