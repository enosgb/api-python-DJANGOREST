# Api - School Django Rest

Api to managing students in a school

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install django.

```bash
pip install django
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Django REST.

```bash
pip install djangorestframework
```
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Django markdown.
```bash
pip install markdown
```


## Clone and Run

For clone repository.

```bash
git clone https://github.com/enosgb/api-python-DJANGOREST
```
Enter the folder project.

```python
cd escola
```
Start project.

```python
python manage.py runserver
```



## DEV Infos

## settings.py
```
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'
```
## setting database MySQL example:


```
'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'your data base',
    'USER': 'root',
    'HOST': 'localhost',
    'PORT': 3306,
    'PASSWORD': 'you password',      
} 
```

## Generate class model already existing database
```
python manage.py inspectdb > models.py
```
