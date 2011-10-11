import os
from django.conf import settings
from django.core.mail.backends.base import BaseEmailBackend
try:
    from cPickle import dumps
except ImportError:
    from Pickle import dumps


class EmailBackend(BaseEmailBackend):
    def send_messages(self, email_messages):
        num_sent = 0
        if not email_messages:
            return
        for email_message in email_messages:
            if self._send(email_message):
                num_sent += 1
        return num_sent

    def _send(self, email_message):
        from uwsgi_mail.task import send_mail
        send_mail.spool(email_message=dumps(email_message))
        return True
