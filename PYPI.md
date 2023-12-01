# PYPI

A seguir será descrito o processo de como colocar o projeto no repositório do PYPI. 

Projeto feito com base no tutorial: https://www.alura.com.br/artigos/como-publicar-seu-codigo-python-no-pypi

Instalei a biblioteca setuptools (de forma global):

```bash
pip install setuptools
```

Executei o seguinte comando:

```bash
python3 setup.py sdist
```

Instalei a biblioteca twine (de forma global):

```bash
pip install twine
```

Criei um arquivo chamado `.pypirc` na pasta `$HOME` do meu computador com o seguinte conteúdo:

```text
[testpypi]
  username = __token__
  password = pypi-AgENdGVzdC5weXBpLm9yZwIkNmY3NzAxY2ItMjBjZS00MDAyLWEzZDktYjhlNzdhMzgzOGZiAAIqWzMsIjE4NjRiZmZhLTkxYzItNDc5MS1iMThkLWFiOWNmZDBiZmU5NiJdAAAGIAJYyKus3qMvQo4BS_M-bijqTdP608QUGMLR-???????
```

OBS: ocultei alguns caracteres acima do meu token gerado.

Para mais informações sobre problema relacionados ao token consulte o [link](https://pypi.org/help/#apitoken).

Executei o comando abaixo para enviar o projeto para o pypi de teste.

```bash
twine upload dist/* -r testpypi
```

Para explicações sobre como incorporar o README no PYPI consulte o [link](https://packaging.python.org/en/latest/guides/making-a-pypi-friendly-readme/).

Para explicações sobre como organizar os nomes dos pacotes na biblioteca consulte o [link](https://stackoverflow.com/questions/17155804/confused-about-the-package-dir-and-packages-settings-in-setup-py).
