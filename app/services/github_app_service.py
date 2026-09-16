import time
import requests
import jwt

from app.config import (
    GITHUB_APP_CLIENT_ID,
    GITHUB_APP_PRIVATE_KEY
)


def generate_jwt():
    private_key = (
        GITHUB_APP_PRIVATE_KEY
        .replace("\\n", "\n")
        .encode()
    )

    now = int(time.time())

    payload = {
        "iat": now - 60,
        "exp": now + 540,
        "iss": GITHUB_APP_CLIENT_ID
    }

    return jwt.encode(
        payload,
        private_key,
        algorithm="RS256"
    )


def generate_installation_token(installation_id: int):
    jwt_token = generate_jwt()

    url = f"https://api.github.com/app/installations/{installation_id}/access_tokens"

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {jwt_token}",
        "X-GitHub-Api-Version": "2026-03-10"
    }

    response = requests.post(url, headers=headers)
    response.raise_for_status()

    return response.json()["token"]