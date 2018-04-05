from __future__ import print_function

try:
    from cPickle import loads
except ImportError:
    from pickle import loads

try:
    from unittest import mock
except ImportError:
    import mock

from uwsgi_mail.uwsgi import EmailBackend


def test_email_gets_scheduled():
    mocked_task = mock.Mock()
    backend = EmailBackend(send_mail_task=mocked_task)

    payload = {'some': 'object', 'data': 1}
    backend.send_messages([payload])
    assert mocked_task.spool.called
    kwargs = mocked_task.spool.call_args[1]
    assert 'body' in kwargs
    assert loads(kwargs['body']) == payload
