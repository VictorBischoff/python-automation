import vagrant
from fabric.api import env

def start_fedora():
    fedora_vm = vagrant.Vagrant("/Users/victormorkeberg/Documents/vms/fedora")
    fedora_vm.up()
    env.hosts = [fedora_vm.user_hostname_port()]
    env.key_filename = fedora_vm.keyfile()
    env.disable_known_hosts = True

def stop_fedora():
    fedora_vm = vagrant.Vagrant("/Users/victormorkeberg/Documents/vms/fedora")
    fedora_vm.halt()