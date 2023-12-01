from setuptools import setup

from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name = 'py-utils-jsa',
    version = '1.2.0',
    author = 'Jesimar Arantes',
    author_email = 'jesimar.arantes@ufla.br',
    package_dir={"pyutilsjsa": "src"}, # chamando a pasta src de pyutilsjsa
    packages=['pyutilsjsa.core'],      # a forma como o pacote será importado será 
    description = 'Um conjunto de funções simples',
    #long_description = 'Um conjunto de funções simples para realizar conversões, '
    #                    + 'realizar calculos e outras utilidades.',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/jesimar/py-utils-jsa',
    project_urls = {
        'Código fonte': 'https://github.com/jesimar/py-utils-jsa',
        'Download': 'https://github.com/jesimar/py-utils-jsa/archive/refs/tags/v1.0.0.zip'
    },
    license = 'MIT',
    keywords = 'utilidades conversor funções',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Scientific/Engineering :: Physics'
    ]
)