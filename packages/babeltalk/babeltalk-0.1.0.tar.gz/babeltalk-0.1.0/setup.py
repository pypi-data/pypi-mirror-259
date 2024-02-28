
# -*- coding: utf-8 -*-
from setuptools import setup

import codecs

with codecs.open('README.md', encoding="utf-8") as fp:
    long_description = fp.read()
INSTALL_REQUIRES = [
    'torch>=2.2.1',
    'torchvision>=0.17.1',
    'torchaudio>=2.2.1',
    'transformers>=4.38.1',
    'datasets>=2.17.1',
    'gradio>=4.19.2',
]

setup_kwargs = {
    'name': 'babeltalk',
    'version': '0.1.0',
    'description': 'Default template for PDM package',
    'long_description': long_description,
    'license': 'MIT',
    'author': '',
    'author_email': 'lili <fancyerii@gmail.com>',
    'maintainer': None,
    'maintainer_email': None,
    'url': '',
    'packages': [
        'babeltalk',
        'babeltalk.asr',
        'babeltalk.tts',
        'babeltalk.nlp',
        'babeltalk.ui',
    ],
    'package_dir': {'': 'src'},
    'package_data': {'': ['*']},
    'long_description_content_type': 'text/markdown',
    'install_requires': INSTALL_REQUIRES,
    'python_requires': '>=3.9',

}


setup(**setup_kwargs)
