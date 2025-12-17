from django.core.management.base import BaseCommand
from django.utils import timezone
from tasks.models import Task

class Command(BaseCommand):
    help = 'Marks tasks as OVERDUE if due_date is past and status is not DONE'

    def handle(self, *args, **options):
        now = timezone.now()
        # Criteria: due_date < now AND status != DONE AND status != OVERDUE
        overdue_tasks = Task.objects.filter(
            due_date__lt=now,
        ).exclude(
            status__in=[Task.Status.DONE, Task.Status.OVERDUE]
        )

        count = overdue_tasks.count()
        if count > 0:
            updated_count = overdue_tasks.update(status=Task.Status.OVERDUE)
            self.stdout.write(self.style.SUCCESS(f'Successfully marked {updated_count} tasks as OVERDUE'))
        else:
            self.stdout.write(self.style.SUCCESS('No tasks to mark as OVERDUE'))
