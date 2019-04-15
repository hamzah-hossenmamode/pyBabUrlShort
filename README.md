>INTRO
This is an implementation of the solution to a sorten url problem.

The solution was implemented as a visual studio project in python using a Django framework.

It also requires a PostgreSQL access

The choice of using Django and PostgreSQL is to allow the solution to be easily ported to a scaling framework, specifically Azure

>HOW TO RUN
If the solution is to be tested on a different machine python, Django and PostgreSQL need to be present, Visual Studio 2019 community edition should be sufficient for the first two

PostgreSQL will need to be installed, "pip install psycopg2" may be used to install postgreSQL

>CONFIGURATION
Depending on the infrastructure of the host computer

database.ini - change the settings to match required database access

UrlShortTest/env/pyenv.cfg - change the "home" parameter "PYTHONPATH" to the local python home directory

>THE SOLUTION
with a valid PostgreSQL connection, the solution will create its own datatable on first run to keep the links and shortened url

the use of a database connection is to allow multiple instances of the python program to run in parallel while having unique tags associated with each stored url

the files in this project are mainly the project framework

in order to facilitate access to the programming logic

the logic element for the solution is present in the app folder


