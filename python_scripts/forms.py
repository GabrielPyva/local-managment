from output_layer import print_form, println
from input_layer import get_name, get_password
from getpass import getpass


def make_form(menu):
    if isform(menu):
        if menu == [0, 1]:
            sign_in()
        if menu == [0, 2]:
            join()


def sign_in():
    println('#=')
    fname()
    fpassword()


def join():
    println('#=')
    fname()
    fpassword(True, True)


def fname():
    print_form('name')
    get_name()


def fpassword(show=False, confirm=False):
    if show == True:
        print_form('password')
        get_password()
    else:
        getpass('\tPassword: ')
    if confirm == True:
        print_form('confirm password')
        get_password()


def isform(menu):
    form_menus = [[0, 1], [0, 2]]

    if menu in form_menus:
        return True
        
    return False