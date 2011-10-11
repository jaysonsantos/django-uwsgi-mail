#Simple example
Add uWSGI backend in your settings file.

```python
EMAIL_BACKEND = 'uwsgi_mail.uwsgi.EmailBackend'
```

And send your e-mails normally.

```python
from django.core.mail import send_mail

send_mail('Subject here', 'Here is the message.', 'from@example.com',
    ['to@example.com'], fail_silently=False)
```

#Running the simple test

```bash
cd test_project/
uwsgi --ini uwsgi.ini
```

Open your browser with http://127.0.0.1:8000. File shoulde be queued and processed.

#Changing the backend
If you want, you can change the backend uWSGI backend will send your e-mails.

```python
EMAIL_BACKEND = 'your.backend.EmailBackend'
```