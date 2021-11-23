import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_system.settings')

app = Celery('school_system')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()