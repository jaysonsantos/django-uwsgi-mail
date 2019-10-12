from django.core.mail.backends.base import BaseEmailBackend

from uwsgi_mail.compat import dumps


class EmailBackend(BaseEmailBackend):
    def __init__(self, *args, **kwargs):
        _send_mail_task = kwargs.pop('send_mail_task', None)
        if _send_mail_task:
            self._send_mail_task = _send_mail_task
        else:
            from uwsgi_mail.task import send_mail
            self._send_mail_task = send_mail

    def send_messages(self, email_messages):
        num_sent = 0
        if not email_messages:
            return
        for email_message in email_messages:
            if self._send(email_message):
                num_sent += 1
        return num_sent

    def _send(self, email_message):
        self._send_mail_task.spool(body=dumps(email_message, 2))
        return True
