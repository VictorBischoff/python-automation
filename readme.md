# Vagrant Virtual Machine Control

This script allows you to start and halt Vagrant virtual machines using the python-vagrant library.

## Prerequisites

- Install the requirements library:
  `pip install -r requirements.txt`

- Create a .env file inside of the vagrant directory with the following variables:
  - UBUNTUPATH: path to your Ubuntu virtual machine
  - FEDORAPATH: path to your Fedora virtual machine

## Usage

Ensure that you are in the vagrant directory:

`cd vagrant`

To use the script, run the following command:

`python main.py`

Follow the prompts to choose which virtual machine you want to start or halt.