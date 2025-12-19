from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def check_overdue(request):
    tasks = request.data.get('tasks', [])
    overdue_ids = []

    today = datetime.utcnow().date()

    for task in tasks:
        due_date = datetime.fromisoformat(task['due_date']).date()
        status = task['status']

        if due_date < today and status != 'DONE':
            overdue_ids.append(task['id'])

    return Response({
        "overdue_task_ids": overdue_ids
    })
