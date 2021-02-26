import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / 'README.md').read_text()

setup(
    name='hermes-herald',
    version='0.1',
    description='Hermes - the herald of the gods',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://rooters.it',
    author='Pasquale \'sid\' Fiorillo',
    author_email='me@rooters.it',
    license='GPL3',
    packages=['hermes'],
    install_requires=["requests"],
    include_package_data=True,
)
