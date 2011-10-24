from django.core import mail
from django.http import HttpResponse

def test(request):
    print dir(mail)
    mail.send_mail('Subject here', 'Here is the message.', 'from@example.com',
              ['to@example.com'], fail_silently=False)
    return HttpResponse('Queued')
