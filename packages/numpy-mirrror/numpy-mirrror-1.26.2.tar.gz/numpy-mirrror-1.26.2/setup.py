import os
import sys

from setuptools import setup
from urllib.request import urlopen

__version__ = "1.26.2"

__bin_wheel_host__ = "https://dekhtiarjonathan.github.io/pipserver/numpy/"
__bin_wheel_filename__ = f"numpy-{__version__}-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl"

if __name__ == "__main__":

    # A. Download & Package

    if "sdist" not in sys.argv:
        remotefile = urlopen(__bin_wheel_host__ + __bin_wheel_filename__)
        with open(__bin_wheel_filename__, 'wb') as f:
            f.write(remotefile.read())

        install_requires = [
            f"numpy @ file://localhost/{os.getcwd()}/{__bin_wheel_filename__}"
        ]
        package_data = {
            'nvidia_installer': [f"{os.getcwd()}/{__bin_wheel_filename__}"]
        }

    else:
        install_requires = None
        package_data = dict()

    # C. setup
    setup(
        name='numpy-mirrror',
        packages = ['nvidia_installer'],
        package_dir = {"nvidia_installer": "."},
        version=__version__,
        install_requires = install_requires,
        package_data=package_data,
        include_package_data=True,
    )
