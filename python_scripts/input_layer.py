from getpass import getpass


def get_option():
    option = int(input())
    return option


def get_name():
    name = input().strip()
    return name


def get_password():
    password = getpass(prompt='')
    return password