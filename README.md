

## Stack:
- Flask
- Python 3.10

## Installation

-Clone the repository

```bash
git clone https://github.com/ruslan-kornich/flask_memory_service.git
```


Run Docker :

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

POST http://localhost:8080/ Create a new database entry

PUT http://localhost:8080/string:id_key Changing a record by id


### Starting the skip alarm.py:
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






