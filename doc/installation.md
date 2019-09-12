## Installation

### Create an environment

Create a project folder and a `venv` folder within:

```bash=
mkdir flask-blog
cd flask-blog
python3 -m venv venv
```

On Windows:

```bash=
py -3 -m venv venv
```

### Activate the environment

```bash=
. venv/bin/activate
```

On Windows:

```bash=
venv\Scripts\activate
```

### Install Flask & packages

Within the activated environment, install dependencies:

For the first time

```bash=
pip install Flask
pip install gunicorn
pip install Flask-SQLAlchemy
pip install Flask-Migrate
pip install flask_login
pip install flask_wtf
pip install requests
pip freeze > requirements.txt
```

For someone who clone the project

```bash=
pip install -r requirements.txt
```

### .gitignore

```
venv/

\*.pyc
**pycache**/

instance/

.pytest_cache/
.coverage
htmlcov/

dist/
build/
\*.egg-info/

```

### Run project
```bash=
flask db init
flask run 
```

### Database migration
```
flask db migrate -m "Message"
flask db upgrade
```