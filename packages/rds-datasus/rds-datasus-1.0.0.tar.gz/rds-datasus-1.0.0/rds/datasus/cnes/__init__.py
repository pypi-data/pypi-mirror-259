# -*- coding: utf-8 -*-
from rds.datasus import get, URL_PREFIX


def get_estabelecimentos_do_municipio(co_municipio: str) -> dict:
    return get(f"{URL_PREFIX}/cnes/municipio/{co_municipio}/estabelecimentos/")


def get_estabelecimentos_por_municipio_e_competencia(
    co_municipio: str, co_competencia: str
) -> dict:
    return get(
        f"{URL_PREFIX}/cnes/municipio/{co_municipio}/competencia/{co_competencia}/estabelecimentos/"
    )


def get_estabelecimento(co_cnes: str) -> dict:
    return get(f"{URL_PREFIX}/cnes/estabelecimento/{co_cnes}/")


def get_estabelecimento_vinculos(co_cnes: str) -> dict:
    return get(f"{URL_PREFIX}/cnes/estabelecimento/{co_cnes}/vinculos/")


def get_profissional(cpf_or_cns: str) -> dict:
    return get(f"{URL_PREFIX}/cnes/profissional/{cpf_or_cns}/")


def profissional_vinculos(cpf_or_cns: str) -> dict:
    return get(f"{URL_PREFIX}/cnes/profissional/{cpf_or_cns}/")
