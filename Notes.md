o---------------------------------------------------o
| These are notes for the following tutorial:     	|
|	https://vkvideo.ru/video-213108013_456245430  	|
o---------------------------------------------------o

Create a Python virtual environment
	python -m venv virt				// -m runs a module as a script
	
Source the environment
	source virt/Scripts/activate
	
Install Django
	pip install django
	
Install MySQL
	pip install mysql
	
Install a connector
	pip install mysql-connector-python
	pip install mysql-connector (This one doesn't work, uninstalling was required)
	
Install MySQL (Windows)
	https://dev.mysql.com/downloads/installer/
	
Create a Django project
	django-admin startproject dcrm
	cd dcrm
	
Create an App in the project
	python manage.py startapp website
	
In dcrm/settings.py:
	- Add app to INSTALLED_APPS[]
	- 'NAME': 'fedeco',
	- 'USER': 'moy_user',
	- 'PASSWORD': 'Moy_Password123',
	- 'HOST': 'localhost',
	- 'PORT': '3306',

Write and run file to create MySQL database through mysql-connector-python
	python mydb.py
	
Check with
	python manage.py migrate

Create Django superuser
	winpty python manage.py createsuperuser
		username admin
		password Moy_Password123

Run the server
	python manage.py runserver



o--------------------------o
|	Deploying to GitHub    |
o--------------------------o

Creating SSH key on the computer
	ssh-keygen -t rsa
	Passphrase: hastaluego
	SHA256:ev22Lvfq4c3oynvVanvZp64+fOyP9SCGY9MHNMyREoE

Adding the SSH key to GitHub
	Github.com, add SSH key, paste public key

Setting up Git on /dcrm/dcrm from Git bash
	$ git config --global user.name "Your Name"
	$ git config --global user.email "you@youraddress.com"
	$ git config --global push.default matching
	$ git config --global alias.co checkout

	federico-castro-ru, password 8189

Git init, add and commit
	git init
	git add .
	git commit -am 'Initial commit'

Connect to GitHub
	git remote add origin https://github.com/federico-castro-ru/Django-CRM-Project.git
	git branch -M main
	git push -u origin main


o-------------------------------------------------------------------o
| IMPORTANT NOTE													|
|	Note the structure of the folder:								|
|	MyProjectFolder/	<- Main folder								|
|		virt/				<- Python virtual environment data		|
|		dcrm/				<- Django project folder				|
|			.git/				<- Root git directory				|
|			dcrm/				<- Django "settings" folder			|
|			website/			<- (Custom) app folder				|
o-------------------------------------------------------------------o

Manipulate the urls.py inside the Django settings folder:
	from django.contrib import admin
	from django.urls import path, include 

	urlpatterns = [
		path('admin/', admin.site.urls),
		path('', include('website.urls'))
	]


**Steps for creating a Django webpage:**
1. Create a template file (HTML page)
2. Create a URL
3. Create a view

In website/templates/
	Create
	/base.html
	/home.html