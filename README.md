This is a [Django](https://www.djangoproject.com) example project to use with [`gorunn`](https://github.com/parapidcom/gorunn).

## Getting Started

### Add project to the stack

Create file **mydjango.yaml** with contents :

```bash
name: mydjango
git_repo: git@github.com:parapidcom/gorunn-example-django
type: python
version: "3.10"
endpoint: mydjango.local.gorunn.io
env_vars: true
start_command: gunicorn mydjango.wsgi:application --bind 0.0.0.0:3000 --workers 3 --reload
listen_port: 3000
build_commands:
  - pip install -r requirements.txt
  - python create_postgresql_db.py
  - python manage.py migrate
```

Save it in `~/gorunn/projects/`

### Parse the project
```bash
gorunn parse
```

### Build the project
```bash
gorunn build --app mydjango
```
### Open it
Open [https://mydjango.local.gorunn.io](https://mydjango.local.gorunn.io) with your browser to see the result.

### Exec
You can execute shell commands inside container:
```bash
gorunn terminal --app mydjango
```
