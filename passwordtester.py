"""passwordtester.py"""

import re

NEW_LIST = ['ABd1234@1', 'a F1#', '2w3E*', '2We3345']


def password_checker(new_list):
    """function to check passwords"""
    if isinstance(new_list, list):
        pass_list = []
        for element in new_list:
            if len(element) >= 6 and len(element) <= 12:
                search_parameter = r"\w+\W+\s*"

                if re.match(search_parameter, element):
                    pass_list.append(element)

        for value in pass_list:
            return value


print(password_checker(NEW_LIST))
print("Hello world")


