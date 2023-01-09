import vagrant
from fabric.api import env

def start_ubuntu():
    ubuntu_vm = vagrant.Vagrant("/Users/victormorkeberg/Documents/vms/ubuntu")
    ubuntu_vm.up()
    env.hosts = [ubuntu_vm.user_hostname_port()]
    env.key_filename = ubuntu_vm.keyfile()
    env.disable_known_hosts = True

def stop_ubuntu():
    ubuntu_vm = vagrant.Vagrant("/Users/victormorkeberg/Documents/vms/ubuntu")
    ubuntu_vm.halt()