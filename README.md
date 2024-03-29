[python-download]: https://www.python.org/downloads/
[django-link]: https://www.djangoproject.com/

![Python Badge](https://img.shields.io/badge/Python-3.9.2-blue?logo=python)
![Python Badge](https://img.shields.io/badge/Django-3.2.4-092E20?logo=django)


# Send Emails

<p align="center">
    <img src="media/project_img.png" width="500px">
</p>
A simple app where a user can send emails to his friends. Easy to use.

### Built with

![Django Badge](https://img.shields.io/badge/-Django-092E20?style=for-the-badge&labelColor=black&logo=django&logoColor=white)


## :hammer: Getting started

### Pre requisites

- [Python][python-download] - 3.9 or up
- [Django][django-link] - 3.2.4


### Installation

#### Pipfile and Pipfile.Lock

Inside the Pipfile there's all the modules name needed for the project. 

1. Download Pipenv through the terminal window ***(make sure you have [Python][python-download] installed)***:

	```python
    pip install pipenv
    ```
    
2. After installing pipenv all you have to do is to download the files and in the terminal window, go to the folder with these files and run:

	```python
    pipenv install
    ```
    This will create a virtual environment with all the modules needed.

3. We must have this virtual environment to run our program, through the terminal window:

	```python
    pipenv shell # To run the virtual environment
    exit         # To close the virtual environment
    ```

If any doubts here's a link to some more explanations: [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/basics.html)


### Setting up Gmail for Django Mail API

We need to make some changes in our Gmail account to send an Email. Visit this link with your account signed in:

[Gmail Account Settings](https://myaccount.google.com/security?pli=1)

The link contains a specific setting that allows access via Django mail API. Since our web application is not a google registered service, it is a less secured app. Therefore, we allow less secured apps to our settings.

<img src="media/Gmail-Security-Section.png">

**Less secure app** access option will be present. Turn on the access.

<img src="media/Less-Secure-App-Access-Option.png">

**Note:**

If you are just testing, then you can temporarily do this setting. 


## :email: Send emails

On your terminal window, go to the folder with the Pip files and type: 

```python
pipenv shell
```


Then change to the folder with `manage.py` and type: 

```python
python manage.py runserver
```
Paste this link on your browser:
**http://127.0.0.1:8000/emails/send_email**
