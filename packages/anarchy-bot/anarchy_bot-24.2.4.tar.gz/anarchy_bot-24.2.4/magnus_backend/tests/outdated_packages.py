from tests.common import log_passed, DoTests
import src.setup


def main(do_tests: DoTests):
    requirements_dict = src.setup.parse_requirements_txt()
    outdated: list[dict] = src.setup.get_outdated()
    count = 0
    for package in outdated:
        name = package['name'].lower()
        if name in requirements_dict:
            count += 1
    if count:
        do_tests.warn(
            f'{count} packages are outdated, to update requirements.txt use --update_req_txt --install_req'
        )
    else:
        log_passed('no oudtdated packages')

