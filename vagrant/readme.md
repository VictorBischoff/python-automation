# Vagrant Virtual Machine Control

This script allows you to start and halt Vagrant virtual machines using the python-vagrant library.

## Prerequisites

- Install Vagrant and vmware on your machine by following the instructions [here](https://github.com/VictorBischoff/python-automation/blob/main/vagrant/vmware-vagrant-setup.md).
  
- Install the python dependencies:
  `pip install -r requirements.txt`

- Create a .env file inside of the vagrant directory with the following variables:
  - UBUNTUPATH: path to your Ubuntu virtual machine
  - FEDORAPATH: path to your Fedora virtual machine
  - DEBIANPATH: path to your Debian virtual machine

## Usage

Ensure that you are in the vagrant directory:

`cd vagrant`

To use the script, run the following command:

`python main.py`

Follow the prompts to choose which virtual machine you want to start or halt.