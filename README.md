# Django_DeviceManagementSystem

Device management system is used to log device deatils, date in/out that are lend to someone.
Admin can add users and allow them to add device details when they checout a device.
Users can only add details and they cannot edit/delete it.

Prerequisite:
Install the below in your system
1) Python
2) Django (https://docs.djangoproject.com/en/4.2/topics/install/)
3) Sqlite3

If you are editing models.py, then run the below command before starting the server
1) python manage.py makemigrations app
2) python manage.py migrate

To run server: python manage.py runserver <<port number>>

Default port is 8000.
