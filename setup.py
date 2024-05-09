#!/usr/bin/env python

from setuptools import find_packages, setup

with open('README.md', 'r', encoding='utf-8') as f:
    description = f.read()

about = {}
with open('django_notifications_views/__version__.py', 'r', encoding="utf8") as f:
    exec(f.read(), about)

setup(
    name='django_notifications_views',
    version=about['__version__'],
    author='nachoborrelli',
    author_email='nacho2911@hotmail.com',
    url='https://github.com/nachoborrelli/Django-notifications-views',
    description='Django-notifications-views is an extension for Django-notifications-hq that provides a viewset for the notifications.',
    license='MIT',
    packages=find_packages(),
    long_description=description,
    long_description_content_type='text/markdown',
    keywords='django notifications hq views',
    zip_safe=False,
    install_requires=[
        'Django>=3.8.0',
        'pandas>=2.2.0',
        'requests>=2.30',
        'exponent-server-sdk~=2.0.0',
        'django-notifications-hq~=1.8.0',
    ],
    include_package_data=True,
    python_requires='>=3.8',
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
