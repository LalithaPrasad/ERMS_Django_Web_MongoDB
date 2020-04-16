This app is same in functionality as the "ERMS_Django_Web', but it uses
multiple databases, including mongodb. Django documentation is confusing, so
I created this working app.

The requirements are given in 'ERMS.pdf'.

It uses two relational databases. In addition to the django default database,
it uses 'admindb' to store admin credentials. It uses 'empdb' with mongodb to
store employee details. The relational databases are accessed explicitly
without using 'dbrouter'.

To initailise the default and admindb databases, run the following commands:

    ./manage.py makemigrations app_django
    ./manage.py migrate app_django --database=default
    ./manage.py migrate app_django --database=admindata
    ./manage.py migrate

'admindata' is the name used in 'settings.py'.

For connecting to mongodb I am using pymongo. If mongodb doesnot start at system 
startup, it can be started with the following command. First create a directory in 
any convenient place, like the root directory of the app.

    mkdir empdb
    mongod --database=./empdb &

As usual run the app with

    ./manage.py runserver
