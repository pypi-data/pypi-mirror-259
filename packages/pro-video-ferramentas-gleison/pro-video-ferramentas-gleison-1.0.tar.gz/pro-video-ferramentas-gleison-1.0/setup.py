from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='pro-video-ferramentas-gleison',
    version=1.0,
    description='Este produto é de teste para envio de módulos para o pypi.org',
    long_description=Path('README.md').read_text(),
    author='Gleison Silva',
    author_email='gleisondev5690@gmail.com',
    keywords=['teste','Python','student'],
    packages=find_packages()
)
