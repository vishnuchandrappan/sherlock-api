# Sherlock API

## Getting Started

- Clone Repo
- Create a virtual env

```bash
python -m venv env
```

- Activate env

```bash
source env/bin/activate
```

- Install dependencies

```bash
pip install -r requirements.txt
```

- Set env variables for flask

```bash
export FLASK_APP=app.py
export FLASK_ENV=development # defaults to production
```

- Start server

```bash
flask run
```


## Instructions
* `lib/` is exact clone of the sherlock project
* changes made inside sherlock project
  - `lib/sherlock/sherlock.py`
    ```diff
    - from result import QueryStatus
    + from lib.sherlock.result import QueryStatus

    - from result import QueryResult
    + from lib.sherlock.result import QueryResult

    - from notify import QueryNotifyPrint
    + from lib.sherlock.notify import QueryNotifyPrint

    - from sites  import SitesInformation
    + from lib.sherlock.sites  import SitesInformation
    ```
  - `lib/sherlock/notify.py`
    ```diff
    - from result import QueryStatus
    + from lib.sherlock.result import QueryStatus
    ```

## Available Endpoints
- `/user/<username>`
- `/user/usernames=user1,user2`

## Documentation `http://localhost:5000/docs`