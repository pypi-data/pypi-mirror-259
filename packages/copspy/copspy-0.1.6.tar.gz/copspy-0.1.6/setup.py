from setuptools import setup
# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='copspy',
    version='0.1.6',
    long_description="a fan made python API wrapper for the c-ops public api",
    description='a fan made python API wrapper for the c-ops public api',
    license='MIT',
    packages=['copspy/', 'copspy', 'copspy/errors', 'copspy/urls'],
    author='Kitsune',
    author_email='kitsune@yokaigroup.gg',
    keywords=['cops', 'api', 'wrapper','apiwrapper', 'python', 'c-ops'],
    url='https://github.com/Kitsune-San/cops.py',
    install_requires = ['requests', 'colorama'],
)
