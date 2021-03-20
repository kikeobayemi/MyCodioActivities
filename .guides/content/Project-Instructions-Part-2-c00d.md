# Configure the Django admin
Next, we will configure the Django admin. Django will automatically generate the database for a superuser. Before we create the superuser, run the command below:

~~~python
python manage.py migrate
~~~
Now create the admin/superuser:

~~~python
python manage.py createsuperuser
~~~
Type your django admin user, email, and password.
~~~python
Username (leave blank to use 'codio'):
Email address: a.body@every-lab.io
Password:
Password (again):
~~~

When the "Superuser created successfully." message appears, go ahead and click on ![Run_server](.guides/img/Runserver.png) to generate the page and link.

Then click on ![Box_URL](.guides/img/BoxURL.png "Box URL button") to generate the Django admin page.

Login with the details you provided and you can view the actual site by clicking on the top left hand option ![Admin_page](.guides/img/Adminpage.png "Django Admin page")