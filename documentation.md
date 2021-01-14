## Installation
1. Clone the repository

   ```bash
   $ git clone <write url here>
   ```

2. Install python dependencies
   ```bash
   $ pipenv install -r requirements.txt
   ```

3. Open psql and create user and database
   - Create user <username here> with password "<<super_strong_secret_password>>"
   - Create database <database_name_here> with owner <above username>

4. In /api create a .env and add configuration modeled on .env.example

5. Enter pipenv and make sure you're in /cocktail_backend

   ```bash
   $ pipenv shell
   $ cd cocktail_backend/
   ```

6. Run migration
   ```bash
   $ python manage.py migrate
   ```

7. Seed data
   ```bash
    $ python manage.py loaddata seed/all.json
   ```

8. Run Django server
   ```bash
   $ python manage.py runserver
   ```

*IMPORTANT!*
If you add any python dependencies to your pipfiles, you'll need to regenerate your requirements.txt before deployment.
You can do this by running:

```bash
$ pipenv lock -r > requirements.txt
```

## Database Schema
https://dbdiagram.io/d/5fa0692f3a78976d7b7a327d
