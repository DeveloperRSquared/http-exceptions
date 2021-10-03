import os
from pathlib import Path

from setuptools import find_packages
from setuptools import setup

setup_directory = Path(__file__).absolute().parent

requirements = []
with open(os.path.join(setup_directory, 'requirements.txt'), 'r') as requirements_file:
    for requirement in requirements_file.read().splitlines():
        if requirement:
            requirements.append(requirement)


setup(
    name='http-exceptions',
    version='0.0.1',
    description='HTTP Exceptions',
    long_description="HTTP Exceptions built on FastAPI's HTTPException",
    url='https://github.com/DeveloperRSquared/http-exceptions/',
    author='rikhilrai',
    author_email='developerrsquared@gmail.com',
    packages=find_packages(exclude=['tests*']),
    license='MIT LICENSE',
    python_requires='~=3.7',
    install_requires=requirements,
    tests_require=[],
    package_data={
        'http-exceptions': [
            'py.typed',
        ]
    },
    test_suite='tests',
    include_package_data=True,
    extras_require={},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Typing :: Typed',
    ],
)
