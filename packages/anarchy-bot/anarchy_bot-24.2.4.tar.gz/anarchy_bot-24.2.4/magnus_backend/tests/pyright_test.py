from tests.common import log_passed, DoTests
import subprocess
import src.setup
import json


def main(do_tests: DoTests):
    '''pyright test'''
    venv_python, _ = src.setup.get_venv_python_pip()
    sp_result = subprocess.run(
        [
            venv_python,
            '-m',
            'pyright',
            src.setup.app_path,
            '--outputjson',
            '--project',
            src.setup.app_path / 'pyrightconfig.json',
        ],
        capture_output=True,
        text=True,
    )
    parsed = json.loads(sp_result.stdout)
    if parsed['generalDiagnostics']:
        do_tests.write_text(
            text = sp_result.stdout,
            doc = main.__doc__,
        )
    else:
        log_passed(
            doc = main.__doc__,
        )

