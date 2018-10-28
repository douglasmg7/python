#!/usr/bin/env bash

[[ $_ != $0 ]] && echo "Usage: source init_project" && exit 0

PROJECT_NAME=''
echo "Give a project name"
while [ -z $PROJECT_NAME ]; do
  read PROJECT_NAME
done

# Python 3.3+ comes with a module called venv. For applications that require an older version of Python, virtualenv must be used.
# Install virtualvenv if not installed yet.
# pip3 install virtualenv
# pip3 install --user virtualenv
# sudo apt install python3-venv
# sudo pacman -S python3-virtualenv

echo Creating project foleder...
mkdir -p $PROJECT_NAME && cd "$_"

echo Creating virtualenv...
python3 -m venv venv

echo Enabling virtualenv...
source venv/bin/activate

echo Installing flask...
pip3 install flask

pip3 freeze

# echo "To stop virtualenv: deactivate"
# echo "To start virtualenv: source venv/bin/activate"

