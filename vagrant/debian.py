import vagrant
import os
from fabric.api import env
from dotenv import load_dotenv


load_dotenv()

def start_debian():
    debian_vm = vagrant.Vagrant(os.getenv("DEBIANPATH"))
    debian_vm.up()
    env.hosts = [debian_vm.user_hostname_port()]
    env.key_filename = debian_vm.keyfile()
    env.disable_known_hosts = True

def stop_debian():
    debian_vm = vagrant.Vagrant(os.getenv("DEBIANPATH"))
    debian_vm.halt()
    
