# demo-project

### Installation
```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Curl commands
```
curl http://localhost:8000/api/tasks/ --header 'Authorization: Token token_value'
curl http://localhost:8000/api/tasks/1/ --header 'Authorization: Token token_value'
curl -X POST -H "Content-Type: application/json" --data '{"name":"task 1"}' http://localhost:8000/api/tasks/ --header 'Authorization: Token token_value'
curl -X PUT -H "Content-Type: application/json" --data '{"name":"task 1 update name"}' http://localhost:8000/api/tasks/1/ --header 'Authorization: Token token_value'
curl -X DELETE http://localhost:8000/api/tasks/1/ --header 'Authorization: Token token_value'
```
