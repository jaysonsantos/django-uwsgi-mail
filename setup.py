from setuptools import setup
setup(
    name='django-uwsgi-mail',
    version='1.0',
    author='Jayson Reis',
    author_email='santosdosreis@gmail.com',
    description='A Django backend for e-mail delivery using uWSGI Spool to queue deliveries.',
    url='https://github.com/jaysonsantos/django-uwsgi-mail',
    packages=['uwsgi_mail'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)
