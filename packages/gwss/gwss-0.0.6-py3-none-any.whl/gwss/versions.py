from typing import Union
from lastversion import latest
def get_latest(package: str) -> str:
    diff_names = {'htmx.org': 'htmx'}
    if diff_names.__contains__(package):
        package = diff_names[package]
    version: str = latest(package, output_format='tag')
    if version.startswith('v'):
        version = version[1:]
    assert version is not None
    return version