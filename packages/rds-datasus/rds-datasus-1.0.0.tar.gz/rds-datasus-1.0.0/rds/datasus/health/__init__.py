# -*- coding: utf-8 -*-
from rds.datasus import get, URL_PREFIX


def up() -> dict:
    return get(f"{URL_PREFIX}/healthz/")


def status() -> dict:
    return get(f"{URL_PREFIX}/health/")
