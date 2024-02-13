# drf-taskmanager-api
`drf-taskmanager-api` is  built using Django and Django REST framework. It follows a RESTFul API design architecture. For user signup and authentication it uses third-party package `django-rest-authemail'

## Motivation
The project has made an effort to build a very intuitive and easy-to-use RESTFul API for a task manager that can greatly simplify your project management and improve your development efficiency.
Defining tasks in `drf-taskmanager-api` is simple and intuitive. You can specify task names and status using a user-friendly syntax. This makes it easy to organize and manage complex projects.

## Features
`drf-taskmanager-api` is a task built using Django and Django REST framework. It follows a RESTFul API design architecture and for user signup and authentication it uses third-party package `django-rest-authemail'.

`django-rest-authemail` is a Django/Python application with a RESTful API interface for user signup and authentication. Email addresses are used for authentication, rather than usernames. Because the authentication user model is based on Django's AbstractBaseUser and is itself abstract, the model can be extended without additional database tables. Token authentication allows the API to be accessed from a variety of front ends, including Django, React and AngularJS clients, and iOS and Android mobile apps.

- API endpoints for signup, signup email verification, login, logout, password reset, password reset verification, password change, email change, and user details.
- Extensible abstract user model.
- Perform password confirmation and other client-side validation on the front end for a better user experience.
- Token authentication.
- User models in the admin interface include inlines for signup and password reset codes.



## ⚙️ Installation

- Open CMD
  
- Change directory to desktop

  `cd desktop`
   
- Clone this repository

  `git clone git@github.com:backendkolawole/drf-taskmanager-api.git`

- Change the current directory

  `cd drf-taskmanager-api`

- Create a virtual environment

  `python -m venv myvirtualenv`
  
- Activate virtual environment

  `myvirtualenv\Scripts\activate`

- Install all the packages listed in your requirements.txt file

  `pip install -r requirements.txt`

- In the same directory as settings.py, create a file called `.env`

  - Generate a secret key and set up the `SECRET_KEY` variable in the .env file
  - Set up the `DEBUG` variable in the .env file
  - Include email settings as environment variables or in your project's `settings.py` file.  For example,

```
mysite/settings.py

import os


EMAIL_FROM = env('EMAIL_FROM') or '<YOUR DEFAULT_EMAIL_FROM HERE>'
EMAIL_BCC = env('EMAIL_BCC') or '<YOUR DEFAULT_EMAIL_BCC HERE>'
EMAIL_HOST = env('EMAIL_HOST') or 'smtp.gmail.com'
EMAIL_PORT = env('EMAIL_PORT') or 587
EMAIL_HOST_USER = env('EMAIL_HOST_USER') or '<YOUR EMAIL_HOST_USER HERE>'
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD') or '<YOUR EMAIL_HOST_PASSWORD HERE>'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
```

> [!WARNING]
> `SECRET_KEY` is the key to securing signed data – it is vital you keep this secure, or attackers could use it to generate their own signed values.

  
- Make migrations

  `python manage.py makemigrations`

- Apply migrations

  ` python manage.py migrate`

- Create a superuser

  `python manage.py createsuperuser`
  
- Run server

  `python manage.py runserver`

## Usage

Authemail API Endpoints
-----------------------

**POST [project_url]/signup**

Call this endpoint to sign up a new user and send a verification email.  

Unverified users can sign up multiple times, but only the latest signup code will be active.

- Payload
    
    - email (required)
    - password (required)
    - first_name (optional)
    - last_name (optional)

- Possible responses

```python
201 (Created)
Content-Type: application/json
{
	"email": "amelia.earhart@boeing.com"
	"first_name": "Amelia", 
	"last_name": "Earhart", 
}

400 (Bad Request)
Content-Type: application/json
{
	"email": [
		"This field may not be blank."
	], 
	"password": [
		"This field may not be blank."
	] 
}

{
	"email": [
		"Enter a valid email address."
	]
}

{
	"detail": "User with this Email address already exists."
}
```

**GET [project_url]/signup/verify/?code=\<code\>**

The user clicks the link in the verification email to verify the user.

- Parameters

    - code (required)

- Possible responses

```python
200 (OK)
Content-Type: application/json
{
	"success": "User verified."
}

400 (Bad Request)
Content-Type: application/json
{
	"detail": "Unable to verify user."
}
```

**POST [project_url]/login**

Call this endpoint to log in as a user.  Use the authentication token in future calls to identify the user.

- Payload

    - email (required)
    - password (required)

- Possible responses


```python
200 (OK)
Content-Type: application/json
{
	"token": "91ec67d093ded89e0a752f35188802c261899013"
}

400 (Bad Request)
Content-Type: application/json
{
	"password": [
		"This field may not be blank."
	], 
	"email": [
		"This field may not be blank."
	]
}

{
	"email": [
		"Enter a valid email address."
	]
}

401 (Unauthorized)
{
	"detail": "Authentication credentials were not provided."
}

{
	"detail": "Unable to login with provided credentials."
}
```

**GET [project_url]/logout**

Call this endpoint to log out as an authenticated user.

- HTTP Header

```python
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

- Possible responses

```python
200 (OK)
Content-Type: application/json
{
	"success": "User logged out."
}

401 (Unauthorized)
Content-Type: application/json
{
	"detail": "Authentication credentials were not provided."
}

{
	"detail": "Invalid token"
}
```

**POST [project_url]/password/reset**

Call this endpoint to send an email to a user so they can reset their password.   

- Payload

    - email (required)

- Possible responses

```python
201 (Created)
Content-Type: application/json
{
	"email": "amelia.earhart@boeing.com"
}

400 (Bad Request)
Content-Type: application/json
{
	"email": [
		"This field may not be blank."
	]
}

{
	"email": [
		"Enter a valid email address."
	]
}

{
	"detail": "Password reset not allowed."
}
```

**GET [project_url]/password/reset/verify/?code=\<code\>**

The user clicks the link in the password reset email to verify the password reset code.

- Parameters

    - code (required)

- Possible responses

```python
200 (OK)
Content-Type: application/json
{
	"success": "User verified."
}

400 (Bad Request)
Content-Type: application/json
{
	"password": [
		"This field may not be blank."
	] 
}

{
	"detail": "Unable to verify user."
}
```

**POST [project_url]/password/reset/verified**

Call this endpoint with the password reset code and the new password, to reset the user's password.  

- Payload

    - code (required)
    - password (required)

- Possible responses

```python
200 (OK)
Content-Type: application/json
{
	"success": "Password reset."
}

400 (Bad Request)
Content-Type: application/json
{
	"password": [
		"This field may not be blank."
	] 
}

{
	"detail": "Unable to verify user."
}
```

**POST [project_url]/email/change**

Call this endpoint to send a notification email to the previous email address and a confirmation email to the new email address.  

- HTTP Header

```python
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

- Payload

    - email (required)

- Possible responses

```python
201 (Created)
Content-Type: application/json
{
	"email": "amelia.earhart@boeing.com"
}

400 (Bad Request)
Content-Type: application/json
{
	"email": [
		"This field may not be blank."
	] 
}

{
	"email": [
		"Enter a valid email address."
	] 
}

{
	"detail": "Email address already taken."
}

401 (Unauthorized)
Content-Type: application/json
{
	"detail": "Authentication credentials were not provided."
}

{
	"detail": "Invalid token"
}
```

**GET [project_url]/email/change/verify/?code=\<code\>**

Call this endpoint to verify the email change code and, if appropriate, change the email address.

- Parameters

    - code (required)

- Possible responses

```python
200 (OK)
Content-Type: application/json
{
	"success": "Email address changed."
}

400 (Bad Request)
Content-Type: application/json
{
	"detail": "Email address already taken."
}

{
	"detail": "Unable to verify user."
}
```

**POST [project]/password/change**

Call this endpoint to change a user's password.

- HTTP Header

```python
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

- Payload

    - password (required)

- Possible responses

```python
200 (OK)
Content-Type: application/json
{
	"success": "Password changed."
}

400 (Bad Request)
Content-Type: application/json
{
	"password": [
		"This field may not be blank."
	] 
}

401 (Unauthorized)
Content-Type: application/json
{
	"detail": "Authentication credentials were not provided."
}

{
	"detail": "Invalid token"
}
```

**GET [project_url]/users/me**

Call this endpoint after logging in and obtaining an authorization token to learn more about the user.

- HTTP Header

```python
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

- Possible responses

```python
200 (OK)
Content-Type: application/json
{
	"id": 1,
	"email": "amelia.earhart@boeing.com",
	"first_name": "Amelia",
	"last_name": "Earhart",
}

401 (Unauthorized)
Content-Type: application/json
{
	"detail": "Authentication credentials were not provided."
}

{
	"detail": "Invalid token"
}
```


## Task API Endpoints

Use the authentication token to identify the user.

- HTTP Header
  
` Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b`


**POST [project_url]/task**

Call this endpoint to create a new task.

Possible responses

```

201 (CREATED)

{
    "id": 6,
    "name": "first task",
    "completed": true
}


400 (Bad Request)

{
    "name": [
        "This field is required."
    ]
}


401 (Unauthorized)

{
    "detail": "Invalid token."
}
```

**GET [project_url]/task**

Call this endpoint to get all tasks

- Possible responses

```
200 (OK)

[
    {
        "id": 6,
        "name": "first task",
        "completed": true
    },
    {
        "id": 7,
        "name": "first task",
        "completed": false
    }
]


401 (Unauthorized)

{
    "detail": "Invalid token."
}

```

**GET [project_url]/tasks/:id**

Call this endpoint to get a task with a specific id

Possible responses

```
200 (OK)

{
    "id": 6,
    "name": "first task",
    "completed": true
}

401 (Unauthorized)

{
    "detail": "Invalid token."
}


404 (Not Found)

{
    "detail": "Not found."
}

```


**PATCH /task/:id**

Call this endpoint to update a task with a specific id

Possible responses

```
200 (OK)

{
    "id": 6,
    "name": "some task updated",
    "completed": true
}


401 (Unauthorized)

{
    "detail": "Invalid token."
}


404 (Not Found)

{
    "detail": "Not found."
}

```

**DELETE /task/:id**

Call this endpoint to delete a task with a specific id

Possible responses

```
204 (No content)


401 (Unauthorized)

{
    "detail": "Invalid token."
}


404 (Not Found)

{
    "detail": "Not found."
}

```
