# Changelog

## What's New


### March 19, 2022
- added return to hompage and logout on admin navbar
- Admin now fully functioning and protected. Ready to merge with main.
- admin now requires authentication.
- DB views now added to admin
- base flask admin up and running.

### March 18, 2022
- contact form now sending correctly. Changed index.html header image and added attributions.
- removed ability to register for site from navigation. route is commented out for reuse at a later time.

### March 17, 2022
- fully deployed to Heroku and working
- updated requirements.txt
- updated config to check for sqlite in dev or postgres in prod, updated init to check if db exists and build if not
- Updated config for Postgres URI
- Changed db to Postgres
- Updated config.py, removed dev environment var
- Added wsgi.py, updated procfile
- Added gunicorn and Procfile
- Updated README
- first commit
