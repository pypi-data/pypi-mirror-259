# -*- coding: utf-8 -*-
from typing import Optional
from logging import Logger
from requests import get as original_get, auth
from rds.core.config import settings


logger = Logger(__name__)

URL_PREFIX = "https://api.rds.lais.ufrn.br/service/datasus"


def get(
    url: str,
    username: Optional[str] = None,
    password: Optional[str] = None,
) -> dict:
    credentials = settings.get("RDS2", {"username": username, "password": password})
    basic = auth.HTTPBasicAuth(**dict(credentials))
    response = original_get(url, auth=basic)
    if response.status_code != 200:
        raise Exception(response.text)
    print(response.text)
    return response.json()
