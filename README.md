# Course Registration Portal

## Video Link : https://bit.ly/3sTvR8J
## more snapshots : https://bit.ly/3kz5VLN
## Postman API Documentation and API collection link : https://bit.ly/3zwyhfW
(Note : can download this API collection and documentation from above link and import in postman to view and test ALL API's used in this web app)

## Backend API's deployed on heroku : https://course-registration-motorq.herokuapp.com/

# Project Description
#### Developed a Web App on top of requirements mentioned in PDF for university students and course co-ordinator to add, modify, delete courses and also to make thier own fully flexible classes. This Web App includes two roles i.e university students who can make thier own table, add classes of their chocies, modify slots and also can get location of classes using Maps section and second role will be course co-ordinator being course co-ordinator can add courses, location, users and class slots as per schedule.

# Tech Stack Used :
1. Django Rest Framework (Python3 based backend framework)
2. Javascript
3. PostgreSQL (SQL Database)
4. HTML
5. CSS

# Standard Formats :
1. Code Format - PEP-8 (python standard format)
2. API format - REST based

# Tools Used :
1. Postman (for API testing and API documentation)
2. Git
3. Github
4. VScode
5. Heroku (for deployment)

# Third Party API Used :
1. leaflet
2. Mapbox

## Web APP Features :
1. OTP based JWT authentication for more security.
2. Two roles : student and course co-ordinator. Both roles have same authentication.
3. Each roles have different view of template as per permission to each roles.
   - Permission : 
   1. student
   - View and Delete course from Timetable
   - Add class of own choice without any clash of timing
   - Can view location of class based on course code
   2. course co-ordinator
   - can Add users
   - can Add courses with course code and name.
   - can Add classes with slots, faculties and location.
   - Can Add location of building on map
4. Each API has extra layer of security according to user permission
   

## How to run project on your local setup :
## STEP-1 : Install PostgreSQl with pgAdmin
### How to install PostgreSQL?
##### Download postgreSQL from following link and install 
##### https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

## STEP-2 : Set Up Database 
##### Open PgAdmin and Create a database with name as per choice in PgAdmin.

## STEP-3 : Clone this repository

## STEP-4 : Creating Virtual environment
##### Use following command to set up virtual environment
```py -m venv <env-name>```
##### Activate environment
```<env-name>\Scripts\activate.bat```

## STEP-5 Install requirements.txt
```pip install -r requirements.txt```

## STEP-6 : Go to course_registration/settings.py
##### Replace database_name, database_user and database_password in following code

```DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your-database-name',
        'USER': 'your-user-name',
        'PASSWORD': 'your-password',
        'HOST': 'localhost'
    }
} 
```

## STEP-7 : Run following commands
```python manage.py makemigrations```

```python manage.py migrate```

```python manage.py runserver```

#### Hurrah your website is running


## Set up superuser
#### Use following command
```python manage.py createsuperuser```

## Thank you


