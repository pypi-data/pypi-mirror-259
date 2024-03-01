from fastapi.testclient import TestClient
from pathlib import Path
import rich.console
import src.common
import src.setup
import starlette
import tortoise
import fastapi
import anyio
import httpx
import os
import random
import string


console = rich.console.Console()


def generate_random_string(length=11):
    '''get random 11 symbols string'''
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


class DoTests:
    def __init__(
        self,
        errors_path: Path,
    ) -> None:
        self.errors_path = errors_path
        self.console: rich.console.Console = console
        self.exit_code = 0

    def warn(
        self,
        text: str,
    ):
        self.console.log('[yellow]\\[WARN][/]', text)

    def do_tests(
        self,
        methods: list,
        *args,
    ):
        for method in methods:
            try:
                method(*args)
            except KeyboardInterrupt:
                os._exit(0)
            except Exception:
                self.write_error()
                self.exit_code = 1

    def write_text(
        self,
        text: str,
        doc: str | None,
    ) -> None:
        error_path = src.common.generate_filename(
            dir_path=self.errors_path
        )
        with error_path.open('w', encoding = 'utf-8') as file:
            file.write(text)
        self.console.log(f'[red]\\[error][/] {doc} {error_path}')

    def write_error(
        self,
    ) -> None:
        error_path = src.common.generate_filename(
            dir_path=self.errors_path
        )
        print_exception_args: dict = {
            'show_locals': False,
            'suppress': [
                tortoise,
                fastapi,
                starlette,
                anyio,
                httpx,
            ],
        }
        with error_path.open('w', encoding = 'utf-8') as file:
            c_error = rich.console.Console(
                width = 80,
                file = file,
            )
            c_error.print_exception(
                **print_exception_args
            )
        self.console.log(f'[red]\\[error][/] {error_path}')
        self.console.print_exception(
            **print_exception_args
        )


class Test:
    def __init__(
        self,
        client: TestClient,
    ) -> None:
        self.email: str = 'example@email.com'
        self.password: str = 'my_password'
        self.client: TestClient = client
        self.console: rich.console.Console = console

    def log_passed(
        self,
        url: str = '',
        doc: str | None = '',
    ):
        '''
        writes logs in console

        in future 'DEPRECATED' argument will be removed
        only 'url' and 'docstring' arguments must be passed
        'url' and 'docstring' arguments are optional now, but will be required in future
        '''
        log_passed(
            url = url,
            doc = doc,
        )

    def validate_json_data(self, json_data: dict | None = None) -> dict:
        '''validate auth data'''
        default_data = {
            'email': 'example@email.com',
            'password': 'password',
            'firstname': 'string',
            'lastname': 'string',
            'inn': generate_random_string(),
            'ogrn': generate_random_string(),
            'org_name': 'OrgName',
            'org_legal_address': 'string',
            'org_actual_address': 'string',
            'phone_number': '89614445188'
        }
        if json_data is None:
            return default_data
        for key, value in default_data.items():
            if key not in json_data:
                json_data[key] = value
        return json_data


def log_passed(
    url: str = '',
    doc: str | None = '',
):
    '''
    writes logs in console

    in future 'DEPRECATED' argument will be removed
    only 'url' and 'docstring' arguments must be passed
    'url' and 'docstring' arguments are optional now, but will be required in future
    '''
    output = []
    if url:
        output.append(url)
    if doc:
        output.append(doc)
    console.log(
        '[green]\\[pass][/]',
        *output,
    )

