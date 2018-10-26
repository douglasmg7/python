#!/usr/bin/env bash

# Project name.
while [ -z $PROJECT_NAME ]; do
  read -p "Project name: " PROJECT_NAME
done

# Install virtualvenv.
pip3 install virtualenv

# Create project folder.
mkdir -p $PROJECT_NAME && cd "$_"

# Create virtualenv.
python3 -m venv venv
source venv/bin/activate
