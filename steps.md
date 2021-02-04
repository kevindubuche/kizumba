1.  [] Start django project:
>>>django-admin startproject kizumba 
2.  [] To create an app:
>>>cd kizumba
>>> python3 manage.py startapp dancer
3.  [] Create Dancer model:
4.  [] Allow managing Dancer in admin site
>>> admin.site.register(Dancer)
5.  [] Add the app in the install app array in settings.py:
>>> 'dancer.apps.DancerConfig'
5.  [] Create urls.py page in dancer directory.
6.  [] Add index route and name the route index.
7.  [] Include our url file in kizumba/urls.py file
8.  [] Create dancer/templates/dancers/base.html file
9.  [] Create body block.
10. []Create dancer/templates/dancers/header.html
11. []Create dancer/templates/dancers/footer.html
12. [] Include header & footer in base.html
13. [] Create index.html
14. [] Create index method in views.py
11. [] Create static file to add css, js, and img
11. [] Add the static in the base.html
>>>  {% load static %}
15. [] To make migration:
>>> python3 manage.py makemigrations
5.  [] To migrate:
>>> python3 manage.py migrate
7. [] To create superuper:
>>> python3 manage.py createsuperuser
15. [] To run the django server:
>>>python3 manage.py runserver

......... TEST ............
1.  [] Start testing:
>>> python3 manage.py test


......... CI/CD ............
1.  [] To genarate all requirements of the project
>>>pip3 install pipreqs
>>> pipreqs .
2.  [] Create .travis.yml file