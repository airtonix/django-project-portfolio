import os
from setuptools import setup, find_packages

from projects import __version__ as VERSION


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
	name ="django-project-portfolio",
    version=VERSION,
    classifiers = (
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ),
    packages=find_packages(),
    install_requires = (
    	"django-classy-tags",
    	"surlex",
    	"south",
    ),
    author='Zenobius Jiricek',
    author_email='airtonix@gmail.com',
    description='a simple project portfolio application for django.',
    long_description = read('README.md'),
    license='MIT',
    keywords='django, portfolio, showcase',
    url='http://github.com/airtonix/django-project-portfolio/',
    include_package_data=True,
)