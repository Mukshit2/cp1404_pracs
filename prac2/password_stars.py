def main():
    min_length, password = get_passsword()

    while len(password) < min_length:
        print('Your password is too short.')
        password = input('Enter your password: ')

    print_asteriks(password)

    print()


def print_asteriks(password):
    for i in range(len(password)):
        print('*', end='')


def get_passsword():
    password = input('Enter your password: ')
    min_length = 8
    return min_length, password


main()