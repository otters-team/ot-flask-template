import fnmatch
import os
import shutil
import sys

FILES_REQUIREMENTS = {
    'pip-requirements': ('requirements.txt', 'readme-requirements.md',),
    'pipenv': ('Pipfile', 'readme-pipenv.md',),
    'poetry': ('pyproject.toml', 'readme-poetry.md',),
}

NAME_FOR_README_FILE = 'README.md'


def clean_extra_package_managment_files():
    """Removes either requirements files and folders."""
    package_manager = '{{ cookiecutter.package_manager }}'
    to_delete = []

    if package_manager == 'pip-requirements':
        to_delete.extend(FILES_REQUIREMENTS['pipenv'] + FILES_REQUIREMENTS['poetry'])
    elif package_manager == 'pipenv':
        to_delete.extend(FILES_REQUIREMENTS['pip-requirements'] + FILES_REQUIREMENTS['poetry'])
    else:
        to_delete.extend(FILES_REQUIREMENTS['pipenv'] + FILES_REQUIREMENTS['pip-requirements'])

    try:
        for file_or_dir in to_delete:
            if os.path.isfile(file_or_dir):
                os.remove(file_or_dir)
            else:
                shutil.rmtree(file_or_dir)

        rename_readme_file()
        sys.exit(0)
    except OSError as e:
        sys.stdout.write(
            'While attempting to remove file(s) an error occurred'
        )
        sys.stdout.write('Error: {}'.format(e))


def rename_readme_file():
    readme_file = fnmatch.filter(os.listdir(os.getcwd()), 'readme*')[0]
    os.rename(readme_file, NAME_FOR_README_FILE)


if __name__ == '__main__':
    clean_extra_package_managment_files()
