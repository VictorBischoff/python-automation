import vagrant
import os
from fabric.api import env
from dotenv import load_dotenv

load_dotenv()

def start_ubuntu():
    ubuntu_vm = vagrant.Vagrant(os.getenv("UBUNTUPATH"))
    ubuntu_vm.up()
    env.hosts = [ubuntu_vm.user_hostname_port()]
    env.key_filename = ubuntu_vm.keyfile()
    env.disable_known_hosts = True

def stop_ubuntu():
    ubuntu_vm = vagrant.Vagrant(os.getenv("UBUNTUPATH"))
    ubuntu_vm.halt()