"""Minimal JSONPlaceholder HTTP client."""

from __future__ import annotations

from typing import Any

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
DEFAULT_TIMEOUT_SECONDS = 10


def _get_json(path: str) -> dict[str, Any]:
    response = requests.get(f"{BASE_URL}{path}", timeout=DEFAULT_TIMEOUT_SECONDS)
    response.raise_for_status()
    payload = response.json()
    if not isinstance(payload, dict):
        raise TypeError(f"Expected JSON object from {path}, got {type(payload).__name__}")
    return payload


def fetch_post(post_id: int) -> dict[str, Any]:
    return _get_json(f"/posts/{post_id}")


def fetch_user(user_id: int) -> dict[str, Any]:
    return _get_json(f"/users/{user_id}")
