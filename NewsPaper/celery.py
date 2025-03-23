import os
from celery import Celery
from celery.schedules import crontab
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPaper.settings')
 
app = Celery('NewsPaper')
app.config_from_object('django.conf:settings', namespace = 'CELERY')

app.conf.beat_send_notifications = {
    'clear_board_every_minute': {
        'task': 'board.tasks.period_send_notifications',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
    },
}


app.autodiscover_tasks()