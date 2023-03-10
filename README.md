

## Stack:
- Flask
- Python 3.10

## Installation

-Clone the repository

```bash
git clone https://github.com/ruslan-kornich/memory_service.git
```

# Run locally

- Create and activate virtual environment

```bash
$ python3 -m venv venv
source venv/bin/activate
```
- Install requirements:
```bash
$ pip install -r requirements.txt
```

- Starting a local server
```bash
$ cd flask_memory_service
```
```bash
$ python wsgi.py
```



Run with Docker :

```bash
$ sudo docker compose up -d --build
```

## API:
Support for GET, POST, PUT requests
## Assumed data structure

```jsx
{
	id: 
	value_used: String
}
```

GET http://localhost:8080/ get all records
```jsx
[
  {
    "_id": "63eb85f9286bad15760d6873",
    "value_used": "5273 Kb"
  },
  {
    "_id": "63eb8603286bad15760d6874",
    "value_used": "5340 Kb"
  }
]
```


POST http://localhost:8080/ Create a new database entry
key=value_used, 
value={ some value RAM}

PUT http://localhost:8080/string:id_key Changing a record by id

```jsx

{
   "value_used":"5676 Kb"
}
```




### Starting the script alarm.py:
```bash
$ cd alarm
```

```bash
$ python3 -m venv venv
source venv/bin/activate
```

```bash
pip install  - r req.txt
```

```bash
python alarm.py
```

When running the script, you must specify the values of the used RAM in kilobytes
when exceeded, a request will be sent to the server http://localhost:8080/


## Run tests:
- In a second terminal window with the local server running, run tests

```bash
$ pytest tests.py -v
```



