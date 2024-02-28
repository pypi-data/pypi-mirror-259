# -*- coding: utf-8 -*-
from rds.datasus import get, URL_PREFIX


def get_cns(cpf_ou_cns: str) -> dict:
    return get("https://api.rds.lais.ufrn.br/service/datasus/cadsus/cns/64583457120/")
