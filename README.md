# GHETTOGROUPO

## Project Description

GhettoGroup aims at providing a single platform for a large group of audience by taking inspiration from Google Classroom, Google Forms, Kahoot and Trello Cards. It focuses on and encourages shared work environments with efficient team management. It targets groups of people both academic and non academic and also individuals who are willing to work on/find open source projects. Currently it only supports `Pubic` and `Private` groups but we plan developing this project on a full scale very soon.
\
P.S: This project is still at a very early stage and has a lot of scope for improvement.

***

## Key Featuers

1. Hierarchical User System for efficient group management

2. Different types of groups supporting every type of work environment

3. Option to send Invites/ Requests to join a group

4. Recommendation System for users to join new groups and expand their domain

5. Subgroup Task Assginment and Task Trackers to reach them deadlines

6. Quizzes/Surveys to check your progress and so the constructive critsim helps you grow

7. Checklists for you to keep track of your very own personal tasks

8. An active developer portal where users can get their test keys for using our REST API services

9. Whiteboard & Audio rooms for your project dicussion and breaks

10. Integrated Social Media sharing allows you to share your achievements with your dear ones

## Completed Modules

Hierarchical structure, group segregation, (sub)group task assignment, quiizes, checklists, an almost active developer portal.
**Percentage Completed: 70%**

***

## Services Exposed (and to be exposed)

1. CRUD for Tasks `(exposed)`

2. CRUD for Quizzes `(exposed)`

3. Leaderboard for Quizzes `(exposed)`

4. Checklists `(exposed)`

5. Sending Requests/Invites `(to be exposed)`

## Services Consumed (and to be consumed)

1. Stripe Checkout for payments `(consumed)`

2. Authentication `(consumed)`

3. Social Media APIs `(to be consumed)`

4. Youtube API `(to be consumed)`

5. Spotify API `(to be consumed)`

***

## Test the project

#### Steps to setup evironment

Create a virtualenv with python3.8
> pip install -r requirements.txt

#### Steps to setup Postgres

  *Linux*:
> sudo apt-get update
> sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
> sudo su - postgres
> createuser --interactive --pwprompt
> role name: ghetto
> role password: ghetto
  (if prompted for superuser choose yes)
>createdb -O ghetto Ghetto

*Windows*:
  Use this link for installing it:
  https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
  You can use PgAdmin to create the new user and the database with the same credentials as above.

##### Database dump and restore

For Windows, you can use PgAdmin directly.

###### Linux Dump

  > psql ghetto > dump.sql

###### Linux Restore

  > psql ghetto < dumo.sql

#### Run migrations and create superuser

> python manage.py makemigrations
> python manage.py migrate
> python manage.py createsuperuser
> python manage.py runserver

#### Create dummy data

Since this project is not live, we are using Test API Keys for the consumed APIs. So create dummy subscriptions or directly create the groups to check other functionalities.
`_baseurl_/api/docs` has a detailed API documentation

***

## Other Contributors

**Aditi Verma**
**Manjju Shree**
**Leela Madhuri**

***

_This project belongs to Team Ghettogroup ©2020_
