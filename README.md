# GHETTOGROUPO

### Steps to setup evironment
Create a virtualenv with python3.8
```pip install -r requirements.txt```

### Steps to setup Postgres
  *LINUX*:

  ```sudo apt-get update```

  ```sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib```

  ```sudo su - postgres```

  ```createuser --interactive --pwprompt```

  ```role name: ghetto```

  ```role password: ghetto```
  (if prompted for superuser choose yes)
  ```createdb -O ghetto Ghetto```  

*Windows*:
  Use this link for installing it:
  https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
  You can use PgAdmin to create the new user and the database with the same credentials as above.

### Database dump and restore
    For Windows, you can use PgAdmin directly.
#### Linux Dump
  ```psql ghetto > dump.sql```
#### Linux Restore
  ```psql ghetto < dumo.sql```

## PHASE 1:

***STEP 1:***
    Add the 'User' model in 'users' app
    Run migrations
    Create Registration/Login pages
    Create forms
    Integrate it with frontend

    <!-- Schema for 'User' model:
        email -> unique
        username -> unique
        first name
        last name
        USERNAME = username
        REQUIRED FIELDS = email, first name
      Create these with and also methods to validate the email and username field -->


***STEP 2:***
    Add Todo-s
    


***STEP 3:***
