import vagrant
import os
from fabric.api import env
from dotenv import load_dotenv


load_dotenv()

def start_fedora():
    fedora_vm = vagrant.Vagrant(os.getenv("FEDORAPATH"))
    fedora_vm.up()
    env.hosts = [fedora_vm.user_hostname_port()]
    env.key_filename = fedora_vm.keyfile()
    env.disable_known_hosts = True

def stop_fedora():
    fedora_vm = vagrant.Vagrant(os.getenv("FEDORAPATH"))
    fedora_vm.halt()