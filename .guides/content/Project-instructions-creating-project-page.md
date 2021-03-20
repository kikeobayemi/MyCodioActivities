# Create your Project Page with Django
In this step, we will first install Django inside a virtual environment and then start building the project with Django. 

Create new virtual environment.  An example here is named *django01*.

~~~python
virtualenv --python=python django01
~~~
Go to the *django01* directory and activate the virtual environment.

~~~python
cd django01/
source bin/activate
~~~
Now install Django 2.2.12 using `pip`.
~~~python
pip install Django==2.2.12
~~~
When the installation is complete, create a new project (called *mysite* in this example) with the `django-admin` command:
~~~python
django-admin startproject mysite
~~~
The command will create a new directory *mysite* that contains Django files:
~~~python
cd mysite/
~~~
Now edit the *settings.py* under the *mysite* directory, visible in your Filetree.  You will need to set the server IP address inside the 'ALLOWED_HOSTS' line to allow all, as shown below.
~~~python
ALLOWED_HOSTS = ['*']
~~~
Save and exit.

Now run the python `django runserver` command.
~~~python
python manage.py runserver 0.0.0.0:8000
~~~
The command will run python django on the IP address '0.0.0.0', on port '8000'.  


Click on the link generated to take you to the project page (http://0.0.0.0:8000/).

__++Note++__:

Press 'Ctrl+c' to exit from the `django runserver`.