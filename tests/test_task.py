from mock import patch

from uwsgi_mail.compat import dumps
from uwsgi_mail.task import send_mail, DJANGO_DEFAULT_EMAIL_BACKEND


@patch('uwsgi_mail.task.get_connection')
def test_send_email(mocked_get_connection):
    send_mail({'body': dumps({})}, get_backend_function=lambda: DJANGO_DEFAULT_EMAIL_BACKEND)
    mocked_get_connection.assert_called_once_with(backend=DJANGO_DEFAULT_EMAIL_BACKEND)
    mocked_get_connection().send_messages.assert_called_once_with([{}])
