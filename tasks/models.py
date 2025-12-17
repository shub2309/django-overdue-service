from django.db import models

class Task(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        IN_PROGRESS = 'IN_PROGRESS', 'In Progress'
        DONE = 'DONE', 'Done'
        OVERDUE = 'OVERDUE', 'Overdue'

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    priority = models.CharField(max_length=50, default='MEDIUM') 
    due_date = models.DateTimeField()
    
    # Linking to external tables (Laravel managed)
    project_id = models.BigIntegerField()
    assigned_to = models.BigIntegerField(null=True, blank=True) # User ID
    created_by = models.BigIntegerField(null=True, blank=True) # Admin ID

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Assuming Laravel uses 'tasks' table
        db_table = 'tasks'
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return f"{self.title} ({self.status})"
