#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages

setup(
    name='xeval',
    version='0.1.3',
    author='deng1fan',
    author_email='dengyifan@iie.ac.cn',
    url='https://github.com/deng1fan',
    description=u'深度学习评测包',
    long_description=open("README.md", "r", encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        'xspike',
        'bert_score',
        'pandas',
        'datasets',
        'nltk',
        'rouge',
        'sacrebleu',
        'spacy',
        'rich',
    ],
    exclude=["*.tests", "*.tests.*", "tests"],
    include_package_data=True,
    python_requires='>=3.7',
    keywords=['gpu', 'queuer', 'redis'],
)
