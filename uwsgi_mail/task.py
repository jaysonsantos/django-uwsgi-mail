from uwsgidecorators import spool
try:
    from cPickle import loads
except ImportError:
    from Pickle import loads

from django.conf import settings
from django.core.mail import get_connection

BACKEND=getattr(settings, 'UWSGI_EMAIL_BACKEND',
    'django.core.mail.backends.smtp.EmailBackend')

@spool
def send_mail(arguments):
    conn = get_connection(backend=BACKEND)
    conn.send_messages([loads(arguments['email_message'])])
