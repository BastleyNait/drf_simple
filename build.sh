#!/usr/bin/env bash
# exit on erro

ser-o errexit 
pip intall -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate