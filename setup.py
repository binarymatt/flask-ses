'''
    Flask-ses
    ------------

    Flask application that provides AWS SES integration via boto
'''

from setuptools import setup

setup(
    name='Flask-Ses',
    version='0.1',
    url='https://github.com/binarydud/flask-ses',
    license='BSD',
    author='Matt George',
    author_email='mgeorge@gmail.com',
    description='ses integration for Flask.',
    long_description=__doc__,
    py_modules=['flask_ses'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'boto'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite='test_ses'
)

