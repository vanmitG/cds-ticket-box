## Deployment on Heroku

### Procfile

Create Procfile for Heroku in root, and edit:
```
web: gunicorn app:app
```

### Install heroku-cli and create a new app on Heroku

[Download and install the Heroku CLI](https://devcenter.heroku.com/articles/heroku-command-line).

If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.

```bash=
$ heroku login
```

### Create a new Git repository

Initialize a git repository in a new or existing directory

```bash=
$ cd my-project/
$ git init
$ heroku git:remote -a flask-ticketbox
```

### Deploy your application

Commit your code to the repository and deploy it to Heroku using Git.

```bash=
$ git add .
$ git commit -am "make it better"
$ git push heroku master
```

For existing repositories, simply add the heroku remote
```
$ heroku git:remote -a flask-ticketbox
```

### First commit to Heroku server

```bash=
$ git init
$ heroku git:remote -a flask-ticketbox
$ git add .
$ git commit -am "First commit"
$ git push heroku master
```

### Run db migrate on Heroku

```bash=
$ heroku run flask db upgrade
```

### Logging
```
heroku logs --tail
```