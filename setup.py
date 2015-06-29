import os
from setuptools import setup, find_packages

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='pyelb',
    version='0.1',
    url='https://github.com/carrerasrodrigo/pyelb',
    license='BSD',
    author='Rodrigo N. Carreras',
    author_email='carrerasrodrigo@gmail.com',
    description='Log parser for Amazon elactic load balancer',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    classifiers=[],
    entry_points={
        'console_scripts': [
            'pyelb=pyelb.parser:main',
            ],
        },
)
