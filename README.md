# Django uWSGI Mail

A Django backend for e-mail delivery using uWSGI Spool to queue deliveries.

## Usage

First, add uWSGI backend in your settings file.

```python
EMAIL_BACKEND = 'uwsgi_mail.uwsgi.EmailBackend'
```

And send your e-mails normally.

```python
from django.core.mail import send_mail

send_mail('Subject here', 'Here is the message.', 'from@example.com',
    ['to@example.com'], fail_silently=False)
```

### Changing the backend

By default the `django.core.mail.backends.smtp.EmailBackend` is used for the real e-mail delivery. You can change that using: 

```python
EMAIL_BACKEND = 'your.backend.EmailBackend'
```

## Running the simple test

```bash
cd test_project/
uwsgi --ini uwsgi.ini
```

Open your browser with http://127.0.0.1:8000. File shoulde be queued and processed.

