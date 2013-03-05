import os
from setuptools import setup, find_packages

from projects import __version__ as VERSION

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

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
        "django==1.4",
    ),
    author='Zenobius Jiricek',
    author_email='airtonix@gmail.com',
    description='a simple project portfolio application for django.',
    license='MIT',
    keywords='django, portfolio, showcase',
    url='http://git.zenobi.us/django-project-portfolio/',
    include_package_data=True,
)