from output_layer import display_menu, print_form
from input_layer import get_option
from forms import sign_in, make_form

def program_looper():
    current_menu = [0]
    while True:
        display_menu(current_menu)
        option = get_option()
        if option == 0:
            if current_menu == [0]:
                break
            else:
                current_menu = navigate(option, current_menu)
                continue
        make_form(current_menu)
        current_menu = navigate(option, current_menu)
        manage(option, current_menu)


def navigate(option, menu):
    if option > 0:
        menu.append(option)
    else:
        menu.pop()
    return menu


def manage(option, menu):
    pass