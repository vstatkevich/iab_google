#!/bin/bash

apt-get install -qq -y python3-pip > /dev/null
pip3 -q install virtualenv
virtualenv -q VENV
source ./VENV/bin/activate
pip3 install -q --upgrade pandas tldextract 
python3 iab_google_mapping.py 
deactivate