from output_layer import print_form, println
from input_layer import get_name, get_password


def make_form(menu):
    if isform(menu):    
        if menu == [0, 1]:
            sign_in()


def sign_in():
    println('#=')
    fname()
    fpassword()


def fname():
    print_form('name')
    get_name()


def fpassword():
    print_form('password')
    get_password()


def isform(menu):
    form_menus = [[0, 1]]

    if menu in form_menus:
        return True
        
    return False