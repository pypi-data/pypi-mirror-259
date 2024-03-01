from pathlib import Path
import platform
import datetime
import asyncio
import setup
import sys
import os


def generate_filename(
    dir_path: Path,
    max_files_in_dir: int = 30,
    extension: str = 'txt',
) -> Path:
    dir_path.mkdir(
        exist_ok = True,
        parents = True,
    )
    all_files = list(
        dir_path.iterdir()
    )
    all_files.sort()
    while len(
        all_files
    ) >= max_files_in_dir:
        all_files[0].unlink()
        all_files.remove(all_files[0])
    file_date = datetime.datetime.now().strftime('%Y.%m.%d_%H.%M')
    test_file_path = dir_path / file_date
    file_path = Path(
        f'{test_file_path}.{extension}'
    )
    index = 2
    while file_path.exists():
        file_path = Path(
            f'{test_file_path}_{index}.{extension}'
        )
        index += 1
    return file_path


async def delay_and_restart(
    delay: int = 1,
):
    await asyncio.sleep(delay)
    restart()


def restart():
    command = [sys.executable] + sys.argv
    print('restarting:', *command)
    os.execv(command[0], command)

