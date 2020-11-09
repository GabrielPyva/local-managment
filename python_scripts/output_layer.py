from os import get_terminal_size, system


def clear_screen():
    system('clear')


def display_menu(level=0):
    if level == 0:
        print_title('Welcome to the local management')
        print_options(['login', 'join', 'about', 'exit'])
        print_input_area()


def print_title(title=''):
    print(title.upper().center(len(title)+2).center(get_terminal_size()[0], '='))


def print_options(options):
    limit = len(options)-1
    print()
    for index, option in enumerate(options):
        print(f'\t[ {index+1 if index<limit else 0} ] {option}\n')


def print_input_area():
    print('\t>>> ', end='')