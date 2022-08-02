from utils.read_file import read_file
from utils.password_check import PasswordCheck


def execute():
    password_check = PasswordCheck(read_file())
    print('Attention: passwords check only in lowercase!')
    print(f'Valid passwords: {password_check.get_correct_passwords()}')


if __name__ == '__main__':
    execute()
