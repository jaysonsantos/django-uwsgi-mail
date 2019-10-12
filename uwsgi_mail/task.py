
from django.conf import settings
from django.core.mail import get_connection

from uwsgi_mail.compat import loads, spool


DJANGO_DEFAULT_EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


def get_backend():
    return getattr(settings, 'UWSGI_EMAIL_BACKEND', DJANGO_DEFAULT_EMAIL_BACKEND)


@spool
def send_mail(arguments, get_backend_function=None):
    get_backend_function = get_backend_function or get_backend
    conn = get_connection(backend=get_backend_function())
    conn.send_messages([loads(arguments['body'])])
