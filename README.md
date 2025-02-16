# demo-project
This is a demo project


## Requirements
Install python. You can check that it's been installed by running `python --version` on your terminal


## Installation
```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```


### Curl commands for REST APIs
Get the List of Tasks:
```
curl http://localhost:8000/api/tasks/
```

Get the Task by ID:
```
curl http://localhost:8000/api/tasks/1/
```

Create a Task:
```
curl -X POST -H "Content-Type: application/json" --data '{"name":"task 1"}' http://localhost:8000/api/tasks/
```

Update a Task by ID:
```
curl -X PUT -H "Content-Type: application/json" --data '{"name":"task 1 update name"}' http://localhost:8000/api/tasks/1/
```

Delete a Task by ID:
```
curl -X DELETE http://localhost:8000/api/tasks/1/
```


## Guides
Official Django Tutorial: [https://docs.djangoproject.com/en/5.1/intro/](https://docs.djangoproject.com/en/5.1/intro/)

Offical Django REST Tutorial: [https://www.django-rest-framework.org/tutorial/quickstart/](https://www.django-rest-framework.org/tutorial/quickstart/)

Tutorial by Mozilla: [https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django)

