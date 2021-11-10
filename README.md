# SCEMirrorDjangoProject

Both as an attacker and defender, it's important to understand how different pieces of software work. Often times that means building mock, smaller versions of what you're attacking/defending. The GSMST Alumni website runs on the Django python framework, being served behind a nginx reverse proxy. Review both the code on the internal git repository (https://git.habitual-media.com/habitual/alumni_site), django's documentation, and nginx documentation. Then build a small mock django web server where you can test potential attacks/vulns. Even outside of actual attacks and vulnerabilities, even identifying inefficiencies can benefit defensive posture, as it prevents avenues for DDOS.

**Justin Moonjeli, Samreen Farooqui, & Sean Lynch**

**GSMST SCE**


**SETTING UP POSTGRESQL FOR DJANGO**
To run the site, you will need a postgresql database set up and connected to the django project.

Steps for db setup
1. Install Postgre SQL onto the machine (default settings are fine)
2. Install python packages
```bash
pip install psycopg2
pip install sqlparse
pip install *
```
3. Open PG Admin and create an SQL server
4. Within in the SQL server, go to database, create new
5. Go to the site's configuration file called settings.py
6. Adjust the database method to line up with the postgresql server you set up
7. Save file and ensure that the server is up and running and the db has properly initialized
8. Run the site and ensure that all admin functions work as intended
```python
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': '<name of db>',
       'USER': '<admin username of db>',
       'PASSWORD': '<admin password of db>',
       'HOST': '127.0.0.1',
       'PORT': '5432',
   }
}
```
