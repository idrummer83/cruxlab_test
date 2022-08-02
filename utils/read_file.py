import os


def read_file():
    """
    Get data from file
    :return: list
    """
    for filename in os.listdir('password_tmp'):

        try:
            with open(os.path.join('password_tmp', filename), 'r') as f:
                lines = f.readlines()
                return lines
        except Exception as e:
            print(f"Read file error - {e}")
