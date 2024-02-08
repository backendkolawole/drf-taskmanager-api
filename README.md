# drf-taskmanager-api
`drf-taskmanager-api` is  built using Django and Django REST framework. It follows a RESTFul API design architecture. For user signup and authentication it uses third-party package `django-rest-authemail'

## Motivation
The project has made an effort to build a very intuitive and easy-to-use RESTFul API for a task manager that can greatly simplify your project management and improve your development efficiency.
Defining tasks in `drf-taskmanager-api` is simple and intuitive. You can specify task names and status using a user-friendly syntax. This makes it easy to organize and manage complex projects.

## Features
`drf-taskmanager-api` is a task built using Django and Django REST framework. It follows a RESTFul API design architecture and for user signup and authentication it uses third-party package `django-rest-authemail'
`django-rest-authemail` is a Django/Python application with a RESTful API interface for user signup and authentication. Email addresses are used for authentication, rather than usernames. Because the authentication user model is based on Django's AbstractBaseUser and is itself abstract, the model can be extended without additional database tables. Token authentication allows the API to be accessed from a variety of front ends, including Django, React and AngularJS clients, and iOS and Android mobile apps.

- API endpoints for signup, signup email verification, login, logout, password reset, password reset verification, password change, email change, and user details.
- Extensible abstract user model.
- Perform password confirmation and other client-side validation on the front end for a better user experience.
- Token authentication.
- User models in the admin interface include inlines for signup and password reset codes.



## ⚙️ Installation

## Usage

Defining tasks in drf-taskmanager-api is simple and intuitive and makes it easy to organize and manage complex projects.

### Task API Endpoints
**POST /task**

Call this endpoint to create a new task

**GET /task**

Call this endpoint to get all tasks

**GET /task/:id**

Call this endpoint to get a task with a specific id

**PATCH /task/:id**

Call this endpoint to update a task with a specific id

**DELETE /task/:id**

Call this endpoint to delete a task with a specific id


## Authemail API Endpoints
For the endpoints that follow, the base path is shown as /. This path is for example purposes. It can be customized in your project's urls.py file.

**POST /signup**

Call this endpoint to sign up a new user and send a verification email. 
Unverified users can sign up multiple times, but only the latest signup code will be active.

**GET /signup/verify/?code=code**

When the user clicks the link in the verification email, the front end should call this endpoint to verify the user.

**POST /login**

Call this endpoint to log in as a user. Use the authentication token in future calls to identify the user.

**GET /logout**

Call this endpoint to log out an authenticated user

**POST /password/reset**

Call this endpoint to send an email to a user so they can reset their password

**GET /password/reset/verify/?code=code**

When the user clicks the link in the password reset email, call this endpoint to verify the password reset code

**POST /password/reset/verified**

Call this endpoint with the password reset code and the new password, to reset the user's password. The front end should prompt the user for a confirmation password and give feedback if the passwords don't match

**POST /email/change**

Call this endpoint to send a notification email to the previous email address and a confirmation email to the new email address. Similar to signup and password reset verification, the email change email templates are found in authemail/templates/authemail. Override the default templates by placing your similarly-named templates in your_app/templates/authemail

**GET /email/change/verify/?code=code**

When the user clicks the link in the email change email, call this endpoint to verify the email change code and, if appropriate, change the email address

**POST /password/change**

Call this endpoint to change a user's password

**GET /users/me**

Call this endpoint after logging in and obtaining an authorization token to learn more about the user

## Contact
