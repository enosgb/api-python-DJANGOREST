# Api python with DJANGO REST FRAMEWORK

# install DJANGO
`pip install django`

# Create Project
`django-admin startproject setup`


# settings.py
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'


# django rest install
`pip install djangorestframework`

`pip install markdown`

# create App
`python manage.py startapp <project name>`


# setting database MYSQL example:
DATABASES = {
    
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your data base',
        'USER': 'root',
        'HOST': 'localhost',
        'PORT': 3306,
        'PASSWORD': 'you password',      
    } 
    
}

# generate class model already existing database

`python manage.py inspectdb > models.py`


