from urllib.parse import urlparse
import subprocess
import platform
import datetime
import shutil
import common
import setup
import json
import stat
import os


class Config:
    def __init__(self) -> None:
        self.config_json_path = setup.data_path / 'config.json'
        self.secret_key: bytes = b''
        self.db_url: str = 'sqlite://:memory:'
        self.reload: bool = False
        self.force_write: bool = False
        self.force_restart: bool = False
        self.smtp_host: str = "smtp.gmail.com"
        self.smtp_port: int = 587
        self.smtp_user: str = "test@gmail.com"
        self.smtp_password: str = "11111"
        self.is_test: bool = True
        self.verbose: bool = False
        self.system_uptime: str = ''
        self.backend_uptime: str = ''
        self.cdek_base_url: str = ''
        self.cdek_client_id: str = ''
        self.cdek_client_secret: str = ''
        self.start_time = datetime.datetime.now()
        # emails of users that becomes admins after registration
        self.admins_emails = ['admin@gmail.com']
        # emails of users that can acces /api/cabinet/admin/pull_and_restart even if user is not admin
        self.pull_restart_emails = ['ci_cd@example.com']
        if self.config_json_path.exists():
            self.read_json()
        if not self.secret_key:
            self.secret_key = os.urandom(256)
        self.parse_args()
        if not self.config_json_path.exists() or self.force_write:
            self.write_json()
        self.config_json_path.chmod(stat.S_IRUSR | stat.S_IWUSR)  # Set file permissions to 600
        if self.force_restart:
            common.restart()
        self.parse_db_info()
        system_name = platform.system()
        if system_name == 'Linux':
            try:
                system_name = platform.freedesktop_os_release()['PRETTY_NAME']
            except Exception:
                pass
        self.get_uptime()
        self.system_info = {
            'backend_version': setup.app_version,
            'backend_uptime': self.backend_uptime,
            'system': system_name,
            'system_uptime': self.system_uptime,
            'kernel': platform.release(),
            'python_ver:': platform.python_version(),
            'python_implementation': platform.python_implementation(),
        }

    def get_uptime(self) -> None:
        backend_uptime = datetime.datetime.now() - self.start_time
        days = backend_uptime.days
        seconds = backend_uptime.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        self.backend_uptime = f"{days} days, {hours} hours, {minutes} minutes"
        try:
            uptime = subprocess.run(
                ['uptime'],
                text=True,
                capture_output=True,
            )
        except:
            pass
        else:
            self.system_uptime = uptime.stdout.strip()

    def parse_db_info(self) -> None:
        parsed = urlparse(self.db_url)
        if parsed.scheme == 'postgres':
            self.db_postgres_used = True
            self.db_username = str(parsed.username)
            self.db_password = str(parsed.password)
            self.db_hostname = str(parsed.hostname)
            self.db_pg_dump = shutil.which('pg_dump')
            self.db_name = parsed.path.lstrip('/')
        else:
            self.db_postgres_used = False
            self.db_username = ''
            self.db_password = ''
            self.db_hostname = ''
            self.db_pg_dump = ''
            self.db_name = ''

    def parse_args(self) -> None:
        args = setup.parse_args()
        if args.db_url:
            if self.db_url != args.db_url:
                self.db_url = args.db_url
                self.force_write = True
        if args.reload:
            self.reload = True
            self.force_write = True
        if args.noreload:
            self.force_write = True
            self.reload = False

    def read_json(self) -> None:
        with self.config_json_path.open('r') as config_json:
            data = json.load(config_json)
            if 'db_url' in data:
                self.db_url = data['db_url']
            if 'reload' in data:
                self.reload = data['reload']
            if 'secret_key' in data:
                self.secret_key = bytes.fromhex(
                    data['secret_key']
                )
            if 'app_version' in data:
                if data['app_version'] != setup.app_version:
                    self.force_write = True
                if data['app_version'] < '23.0.3':
                    # in 23.0.3 apscheduler added to dependencies, so reinstalling dependencies
                    setup.install_requirements(force=True)
                    self.force_restart = True
            if 'smtp_host' in data:
                self.smtp_host = data['smtp_host']
            if 'smtp_port' in data:
                self.smtp_port = data['smtp_port']
            if 'smtp_user' in data:
                self.smtp_user = data['smtp_user']
            if 'smtp_password' in data:
                self.smtp_password = data['smtp_password']
            if all([
                'smtp_host' in data,
                'smtp_port' in data,
                'smtp_user' in data,
                'smtp_password' in data,
            ]):
                self.is_test = True
            if 'cdek_base_url' in data:
                self.cdek_base_url = data['cdek_base_url']
            else:
                self.cdek_base_url = 'https://api.edu.cdek.ru/v2/'
            if "cdek_client_id" in data:
                self.cdek_client_id = data['cdek_client_id']
            else:
                self.cdek_client_id = 'EMscd6r9JnFiQ3bLoyjJY6eM78JrJceI'
            if 'cdek_client_secret' in data:
                self.cdek_client_secret = data['cdek_client_secret']
            else:
                self.cdek_client_secret = 'PjLZkKBHEiLK3YsjtNrt3TGNG0ahs3kG'


    def write_json(self) -> None:
        data = {
            'app_version': setup.app_version,
            'secret_key': self.secret_key.hex(),
            'db_url': self.db_url,
            'reload': self.reload,
        }
        with self.config_json_path.open('w') as config_json:
            json.dump(
                obj = data,
                fp = config_json,
                indent = 4,
                ensure_ascii = False,
            )
        print(f'data written to {self.config_json_path}')


config = Config()

