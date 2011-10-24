import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
    '..')))
sys.path.append(os.path.join(os.path.dirname(__file__)))
os.environ['DJANGO_SETTINGS_MODULE'] = 'test_project.settings'
import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
