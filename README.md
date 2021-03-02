# Student Portal
> A 3 page portal that captures marks of students in one page and displays the leaderboard in another page.

## How to run ?
> first create .venv using [Pipenv](//google.com/?q=pipenv) [venv](//google.com/?q=venv)

```bash
$ source .venv/bin/activate
$ # set DATABASE_URL SECRET_KEY DEBUG in .env
$ pip install -r requirements.txt 
$ python manage.py makemigration studentportal
$ python manage.py migrate
$ python manage.py runserver
```
# or go to [Shyamkummar yadav](//shyamkumaryadava3.herokuapp.com/)