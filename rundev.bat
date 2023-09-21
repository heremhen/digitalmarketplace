@echo off
cd plugins
start npm run tailwind-dev
cd ..
python manage.py runserver