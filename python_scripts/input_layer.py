from getpass import getpass


def get_option():
    try:
        option = int(input())
    except:
        option = -1
    return option


def get_name():
    name = input().strip()
    return name


def get_password():
    password = input()
    return password