#   Edition Multi-Pivots : Vers une Edition Multi-Directionnelle et Démêlée

____
*Paper:*

____

## Résumé

><p align=justify>Les réseaux antagonistes génératifs (GAN) permettent d’éditer des images en manipulant leurs caractéristiques. Cependant, ces manipulations ne sont pas toujours démêlées. Par exemple, lorsqu’une ride spécifique est modifiée, d’autres caractéristiques liées à l’âge sont souvent modifiées également. Cet article propose une nouvelle méthode d’édition démêlée. L’approche présentée est basée sur des images pivots qui permettent d’apprendre des directions d’édition pour une image d’entrée. Ces pivots sont basés sur une image réelle (l’entrée) et des modifications synthétiques de l’image réelle. Bien que notre principal cas d’applications d’édition soit les rides, notre méthode peut être étendue à d’autres tâches d’édition, telles que l’édition de la couleur des cheveux ou du rouge à lèvres. Les résultats qualitatifs et quantitatifs montrent que notre Edition Multi-Pivots (EMP) fournit un niveau plus élevé de démêlage et une édition plus réaliste que les méthodes de l’état de l’art.</p>

![Alt text](./misc/exemple_editing.svg)


## Installation

![Static Badge](https://img.shields.io/badge/build-3.10.12-rgb(255%2C%20225%2C%2095)?style=flat&logo=python&logoColor=rgb(223%2C%20223%2C%20223)&label=python&labelColor=rgb(61%2C%20122%2C%20171)&link=https%3A%2F%2Fwww.python.org%2Fdownloads%2Frelease%2Fpython-31012%2F)
![Static Badge](https://img.shields.io/badge/build-11.7-rgb(116%2C%20183%2C%2027)?style=flat&logo=nvidia&logoColor=rgb(223%2C%20223%2C%20223)&label=cuda&labelColor=rgb(0%2C%200%2C%200)&link=https%3A%2F%2Fdeveloper.nvidia.com%2Fcuda-11-7-0-download-archive)

Pour installer les dépendances avec Pypi:

    pip install -r requirements.txt

Ou en utilisant conda:

    conda env create -f environment.yml 

## Usage

Pour le détails du fonctionnement du code aller voir le [Jupyter Notebook](./demo.ipynb). Vous pouvez également essayer des éditions via [app](./app.py).

## Contact

Pour toute question sur l'article ou le code vous pouvez me contacter dans la section issues ou par emails (neil99.farmer@gmail.com or neil.farmer@chanel.com).