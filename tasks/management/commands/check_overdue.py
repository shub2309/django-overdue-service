from django.core.management.base import BaseCommand
from django.utils import timezone
from tasks.models import Task
import pymysql

pymysql.install_as_MySQLdb()

class Command(BaseCommand):
    help = 'Checks for tasks that are past their due date and marks them as OVERDUE'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        # Tasks: Due date in past, Status not DONE, Status not OVERDUE
        overdue_tasks = Task.objects.filter(due_date__lt=now).exclude(status__in=['DONE', 'OVERDUE'])
        
        count = overdue_tasks.count()
        if count > 0:
            overdue_tasks.update(status='OVERDUE')
            self.stdout.write(self.style.SUCCESS(f'Successfully marked {count} tasks as OVERDUE'))
        else:
            self.stdout.write(self.style.SUCCESS('No overdue tasks found'))
