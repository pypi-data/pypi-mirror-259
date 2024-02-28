import os
from setuptools import setup


def fast_scandir(dirname):
    subfolders = [f.path for f in os.scandir(dirname) if f.is_dir()]
    for dirname in list(subfolders):
        subfolders.extend(fast_scandir(dirname))
    return subfolders


def package_data_dirs(root, data_dirs):
    data_dirs_path = [x + "/*" for x in data_dirs]
    for data_dir in data_dirs:
        data_dirs_path += [x.replace(f"{root}/", "") + "/*" for x in fast_scandir(f"{root}/{data_dir}")]

    return {root: data_dirs_path}


requirements = [
    "rds-core>=0.2.3",
]

with open("requirements.txt", "w") as file1:
    for requirement in requirements:
        file1.write(f"{requirement}\n")

setup(
    name="rds-datasus",
    version="1.0.0",
    description="Biblioteca para serviços dados online do DATASUS usando a RDS do LAIS",
    long_description="Framework para serviços dados online do DATASUS usando a RDS do LAIS",
    author="Kelson da Costa Medeiros",
    author_email="kelson.medeiros@lais.huol.ufrn.br",
    keywords=["rds", "datasus", "cnes", "cadsus"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    packages=[
        "rds",
        "rds.datasus",
        "rds.datasus.cadsus",
        "rds.datasus.cnes",
        "rds.datasus.health",
    ],
    package_dir={"rds": "rds"},
    package_data=package_data_dirs("rds.core", []),
    download_url="https://github.com/lais-huol/rds-datasus-python/tags",
    url="https://github.com/lais-huol/rds-datasus-python",
)
