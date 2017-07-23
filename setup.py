"""
Flask-Chartjs
-------------

Flask extension to make chartjs easier to use
"""
from setuptools import setup


setup(
    name='Flask-Chartjs',
    version='1.0',
    url='http://abdullahsolutions.com/flask-chartjs/',
    license='BSD',
    author='Abdullah Zainul Abidin',
    author_email='abdullah.zainul@gmail.com',
    description='Flask extension for chartjs',
    long_description=__doc__,
    py_modules=['flask_chartjs'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_sqlite3'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
