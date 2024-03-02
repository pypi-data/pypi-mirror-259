from setuptools import setup
# read the contents of your README file
from pathlib import Path


setup(
    name='copspy',
    version='0.1.2',
    description='a fan made python API wrapper for the c-ops public api',
    long_description_content_type='text/markdown',
    license='MIT',
    packages=['copspy/', 'copspy/errors', 'copspy/urls'],
    author='Kitsune',
    author_email='kitsune@yokaigroup.gg',
    keywords=['cops', 'api', 'wrapper','apiwrapper', 'python', 'c-ops'],
    url='https://github.com/Kitsune-San/cops.py',
    install_requires = ['requests', 'colorama'],
)
