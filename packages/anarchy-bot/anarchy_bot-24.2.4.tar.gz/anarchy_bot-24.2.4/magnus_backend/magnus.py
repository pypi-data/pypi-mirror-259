#!/bin/python

from src import setup
import sys
import os


def main():
    argparser = setup.ArgParser()
    setup.app_launcher_path.chmod(0o755)
    setup.install_requirements()
    os.environ['AUTOTEST'] = 'True'
    argv = sys.argv[1:]
    venv_python, _ = setup.get_venv_python_pip()
    if argparser.args.autotests:
        command = [
            venv_python,
            str(setup.tests_main_path),
            '--db_url=sqlite://:memory:',
        ]
    else:
        command = [
            venv_python,
            '-u',
            str(setup.src_main_path),
            *argv,
        ]
    os.execv(command[0], command)


if __name__ == '__main__':
    main()

