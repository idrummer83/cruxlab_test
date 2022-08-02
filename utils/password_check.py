class PasswordCheck:

    def __init__(self, data: list):
        self.data_list = data

    letter, letter_min, letter_max, password, correct_passwords = None, None, None, None, 0

    def get_correct_passwords(self) -> int:
        """
        Check passwords.
        Passwords check only in lowercase, no information about upper or lowercase in task.
        Passwords are in *.txt file but it better insert in *.csv, but this point not specified in task

        :return: number of valid passwords
        :return: int
        """

        for line in self.data_list:
            if not line.isspace():

                # split data string
                line_list = line.split(' ')

                self.letter = line_list[0]

                self.letter_min = line_list[1].split('-')[0]

                self.letter_max = line_list[1].split('-')[1]
                self.letter_max = self.letter_max.replace(':', '')

                self.password = line_list[-1].strip()

                if int(self.letter_min) > int(self.letter_max):
                    print(f'min and max are incorrect - {line_list}')

                letter_count = self.password.count(self.letter)

                if int(self.letter_min) <= letter_count <= int(self.letter_max):
                    self.correct_passwords += 1

        return self.correct_passwords
