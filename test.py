from github import Github
from dotenv import dotenv_values


CONFIG = dotenv_values(".env")

my_gyt = Github(CONFIG['GIT_HUB'])

# for repo in my_gyt.get_user().get_repos():
#     print(repo.name)


softuni_test_repo = my_gyt.get_repo('ceo-py/softuni')
# print(softuni_test_repo.get_contents('test.py').decoded_content.decode('utf-8'))
python_basic = softuni_test_repo.get_contents('Python Basics')

# print(softuni_test_repo.get_contents('Python Basics/Conditional Statements - Exercise/1_sum_seconds.py').decoded_content.decode('utf-8'))


def get_files_raw_data_git_hub():
    for directory in python_basic:
        new_dir = directory.path
        for file in softuni_test_repo.get_contents(new_dir):
            file_name = softuni_test_repo.get_contents(file.path)
            print(file_name.decoded_content.decode('utf-8'))