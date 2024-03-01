import argparse
from pathlib import Path
import subprocess
import shutil
import json
import time
import venv
import sys
import os

app_name = 'magnus_backend'
app_version = '23.0.3'
app_path = Path(
    __file__
).parent.parent.resolve()
venv_path = app_path / '.venv'
requirements_txt = app_path / 'requirements.txt'
src_main_path = app_path / 'src' / 'main.py'
tests_main_path = app_path / 'tests' / 'main.py'
app_launcher_path = app_path / 'magnus.py'
user_systemd_dir = Path.home() / '.config' / 'systemd' / 'user'
data_path = app_path / f'{app_name}_data'
db_backups_path = app_path / 'db_backups/last'
data_path.mkdir(
    parents = True,
    exist_ok = True,
)
systemd_faq = '''
commands to manage it:
systemctl enable --user --now {service_name}
systemctl disable --user --now {service_name}
systemctl status --user {service_name}
journalctl --user -u {service_name}
'''
systemd = '''
[Unit]
After=network.target

[Service]
ExecStart={exec_start}
Restart=always

[Install]
WantedBy=default.target
'''


def get_venv_python_pip() -> list[Path]:
    venv_bin = venv_path / 'bin'
    venv_scripts = venv_path / 'Scripts'
    if venv_bin.exists():
        venv_python = venv_bin / 'python'
        venv_pip = venv_bin / 'pip'
    elif venv_scripts.exists():
        venv_python = venv_scripts / 'python.exe'
        venv_pip = venv_scripts / 'pip.exe'
    else:
        raise FileNotFoundError()
    return [venv_python, venv_pip]


def install_requirements(
    force: bool = False,
):
    if venv_path.exists() and not force:
        print('dependencies already installed, skipping')
        print('remove .venv dir if you want to reinstall dependencies')
        return
    if not venv_path.exists():
        print('installing dependencies')
        venv.create(
            env_dir=venv_path,
            with_pip=True,
        )
    if venv_path.exists() and force:
        print('reinstralling dependencies')
    _, venv_pip = get_venv_python_pip()
    subprocess.run(
        [venv_pip, 'install', '-U', 'pip']
    )
    subprocess.run(
        [venv_pip, 'install', '-Ur', requirements_txt]
    )


def systemd_generate(
    service_name: str,
    exec_start: Path | str,
):
    formated_faq = systemd_faq.format(
        service_name=service_name
    )
    service_path = user_systemd_dir / f'{service_name}.service'
    user_systemd_dir.mkdir(
        parents=True,
        exist_ok=True,
    )
    service_path.write_text(
        systemd.format(
            exec_start = exec_start,
        )
    )
    print('systemd service sucessfuly generated')
    print(formated_faq)


def parse_requirements_txt() -> dict:
    requirements: dict = {}
    with requirements_txt.open('r') as file:
        for line in file:
            if '==' in line:
                package, version = line.strip().split('==')
                requirements[package] = version
    return requirements


def get_outdated() -> list[dict]:
    venv_python, _ = get_venv_python_pip()
    result = subprocess.run(
        [str(venv_python), '-m', 'pip', 'list', '--outdated', '--format=json'],
        capture_output=True,
        text=True,
    )
    unparsed = result.stdout
    start = unparsed.find('[')
    end = unparsed.rfind(']')
    cutted = unparsed[start:end + 1]
    return json.loads(cutted)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--db_url', type=str, help='set url for database')
    parser.add_argument('--reload', action='store_true', help='enable uvicorn reloading')
    parser.add_argument('--noreload', action='store_true', help='disable uvicorn reloading')
    parser.add_argument('--clean', action='store_true', help='delete .venv dir, stop all containers and delete all podman and docker data')
    parser.add_argument('--podman', action='store_true', help='run code in podman container')
    parser.add_argument('--podman_rebuild', action='store_true', help='rebuild podman container and run code')
    parser.add_argument('--systemd', action='store_true', help='generate systemd service')
    parser.add_argument('--systemd_postgresql', action='store_true', help='generate systemd service that deploys postgresql database')
    parser.add_argument('--update_req_txt', action='store_true', help='update requirements.txt file to newest versions')
    parser.add_argument('--install_req', action='store_true', help='install all requirements via pip')
    parser.add_argument('--autotests', action='store_true', help='run autotests')
    args: argparse.Namespace = parser.parse_args()
    got_conflicts: list[str] = []
    possible_conflicts = {
        '--clean': args.clean,
        '--podman': args.podman,
        '--podman_rebuild': args.podman_rebuild,
        '--systemd': args.systemd,
        '--systemd_postgresql': args.systemd_postgresql,
    }
    for arg, is_enabled in possible_conflicts.items():
        if is_enabled:
            got_conflicts.append(arg)
    if len(got_conflicts) > 1:
        print('conflicting arguments:', *got_conflicts)
        os._exit(0)
    return args


class ArgParser():
    def __init__(
        self,
    ):
        self.args: argparse.Namespace = parse_args()
        self.exit = False
        self.code_container_name = app_name
        self.postgresql_container_name = f'{app_name}_db'
        if self.args.reload:
            self.compose_file: Path = app_path / 'dev.docker-compose.yml'
        else:
            self.compose_file: Path = app_path / 'prod.docker-compose.yml'
        if self.args.update_req_txt:
            self.update_requirements_txt()
            self.exit = True
        if self.args.install_req:
            install_requirements(force=True)
            self.exit = True
        if self.args.systemd:
            self.exit = True
            systemd_generate(
                service_name=app_name,
                exec_start=app_launcher_path,
            )
        if self.args.systemd_postgresql:
            self.exit = True
            self.systemd_postgresql()
        if self.args.clean:
            self.clean_all()
        if self.args.podman_rebuild:
            self.rebuild_and_run_in_podman()
        if self.args.podman:
            self.run_code_in_podman(
                argv=self.clean_argv()
            )
        if self.exit:
            os._exit(0)

    def update_requirements_txt(self):
        print('checking for packages updates')
        requirements_dict = parse_requirements_txt()
        outdated: list[dict] = get_outdated()
        count = 0
        for package in outdated:
            name = package['name'].lower()
            if name in requirements_dict:
                count += 1
                version = package['latest_version']
                requirements_dict[name] = version
        with requirements_txt.open('w') as file:
            for package, version in requirements_dict.items():
                file.write(f'{package}=={version}\n')
            file.write('\n')
        print(f'{count} packages updated in requirements.txt')

    def ensure_podman(self) -> list[str]:
        self.exit = True
        podman_path = shutil.which('podman')
        if not podman_path:
            print('[error] podman in not installed')
            os._exit(1)
        return [podman_path, '--cgroup-manager=cgroupfs']

    def remove_venv(self):
        print('removing venv dir', venv_path)
        if venv_path.exists():
            shutil.rmtree(venv_path)

    def prune(
        self,
        executable: list[str],
    ):
        command = executable + ['system', 'prune', '-a', '--volumes']
        print('running command:', *command)
        subprocess.run(command)

    def stop(
        self,
        executable: list[str],
    ):
        output = subprocess.check_output(
            executable + ['ps', '-a', '-q'],
            text=True,
        )
        splitted = output.strip().split('\n')
        if not splitted:
            print('no running containers to stop')
            return
        if not splitted[0]:
            print('no running containers to stop')
            return
        subprocess.run(
            executable + ['stop'] + splitted,
            check=True,
        )

    def clean_all(self) -> None:
        self.remove_venv()
        self.exit = True
        self.clean_one(
            to_check = 'podman',
            executable = ['podman', '--cgroup-manager=cgroupfs'],
        )
        self.clean_one(
            to_check = 'docker',
            executable = ['sudo', 'docker'],
        )

    def clean_one(
        self,
        to_check: str,
        executable: list[str],
    ) -> None:
        if shutil.which(to_check):
            self.stop(executable)
            self.prune(executable)
        else:
            print(f'{to_check} is not installed, skipping')

    def delete_podman_container(self):
        executable: list[str] = self.ensure_podman()
        for container_name in [
            self.code_container_name,
            self.postgresql_container_name,
        ]:
            print('stopping container')
            subprocess.run(
                [*executable, 'stop', container_name]
            )
            print('removing container')
            subprocess.run(
                [*executable, 'rm', container_name]
            )
        subprocess.run(
            [*executable, 'network', 'rm', self.postgresql_container_name]
        )

    def rebuild_and_run_in_podman(self):
        self.remove_venv()
        self.delete_podman_container()
        self.run_code_in_podman(
            argv=self.clean_argv()
        )

    def systemd_postgresql(self):
        executable: list[str] = self.ensure_podman()
        db_url = self.args.db_url
        if not db_url:
            print('you should also set --db_url, for example --db_url=postgres://my_username:my_password@localhost:5432/magnus')
            os._exit(0)
        subprocess.run(
            [*executable, 'network', 'create', self.postgresql_container_name]
        )
        assert db_url.startswith('postgres://')
        cutted = db_url[11:]
        username_password, ip_port_dbname = cutted.split('@')
        username, password = username_password.split(':')
        port_dbname = ip_port_dbname.split(':')[-1]
        port, dbname = port_dbname.split('/')

        command = [
            *executable,
            'run',
            '--replace',
            '-e', f'POSTGRES_USER={username}',
            '-e', f'POSTGRES_PASSWORD={password}',
            '-e', f'POSTGRES_DB={dbname}',
            f'--name={self.postgresql_container_name}',
            f'--publish={port}:{port}',
            f'--network={self.postgresql_container_name}',
            f'--volume={self.postgresql_container_name}:/var/lib/postgresql/data',
            'docker.io/postgres:16',
        ]
        systemd_generate(
            service_name=f'{app_name}_db',
            exec_start=' '.join(command)
        )

    def run_code_in_podman(
        self,
        network: list[str] = [],
        argv: list[str] = [],
    ):
        executable: list[str] = self.ensure_podman()
        command: list[str] = [
            *executable,
            'run',
            '--replace',
            '--name', self.code_container_name,
            '-v', f'{app_path}:/app:Z',
            '-p', '8000:8000',
            *network,
            'docker.io/python:3.12',
            'python', '/app/magnus.py',
            *argv,
        ]
        print('running code in podman container:', *command)
        subprocess.run(
            command,
            check=True,
        )

    def clean_argv(
        self,
    ) -> list[str]:
        argv: list[str] = sys.argv[1:]
        for arg in [
            '--podman',
            '--podman_rebuild',
        ]:
            if arg in argv:
                argv.remove(arg)
        return argv

