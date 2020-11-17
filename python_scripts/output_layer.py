from os import get_terminal_size, system

current_window_width = get_terminal_size()[0]

def display_menu(menu=[0]):
    clear_screen()
    if menu == [0]:
        print_menu('Welcome to the local management', ['Login', 'Join', 'About', 'Exit'])
    if menu == [0, 1]:
        print_menu('Log in', ['Continue with the Log In', 'Back'])
    if menu == [0, 2]:
        print_title('Please input your data')
        print_options(['No options yet'])
        print_input_area()


def print_title(title=''):
    print(title.upper().center(len(title)+2).center(current_window_width, '='), end='\n\n')


def print_options(options):
    limit = len(options)-1
    print()
    for index, option in enumerate(options):
        print(f'\t[ {index+1 if index<limit else 0} ] {option}\n')


def print_input_area():
    print('\t>>> ', end='')


def print_menu(title, options):
    print_title(title)
    print_options(options)
    print_input_area()


def print_form(data):
    print(f'\t{data.title()}: ', end='')


def println(char: str):
    print(f'\n\t{char * (current_window_width//len(char)-16)}\n')


def clear_screen():
    system('clear')