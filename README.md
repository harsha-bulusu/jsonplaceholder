# jsonplaceholder

A small publishable Python module that wraps selected JSONPlaceholder endpoints.

## Features

- `fetch_post(post_id)`
- `fetch_user(user_id)`

## Structure

```text
jsonplaceholder/
├── src/client.py
├── requirements.txt
├── README.md
└── pyproject.toml
```

## Install dependencies

```bash
python -m pip install -r requirements.txt
```

## Install this project

```bash
python -m pip install ../jsonplaceholder
```

## Build and publish

```bash
poetry build
python -m twine upload dist/*
```
# jsonplaceholder
