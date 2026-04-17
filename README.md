# jsonplaceholder

A small publishable Python module that wraps selected JSONPlaceholder endpoints.

## Features

- `fetch_post(post_id)`
- `fetch_user(user_id)`

## Structure

```text
jsonplaceholder/
├── src/jsonplaceholder/__init__.py
├── src/jsonplaceholder/client.py
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

## Build

```bash
python -m build
```

## Publish to Artifactory

```bash
python -m twine upload --repository-url http://localhost:8081/artifactory/api/pypi/pypi-local dist/*
```
