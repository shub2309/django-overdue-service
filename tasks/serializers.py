from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['status']

    def validate_status(self, value):
        instance = self.instance
        user = self.context['request'].user

        # Rule 1: Overdue tasks cannot move back to WIP (IN_PROGRESS)
        if instance.status == Task.Status.OVERDUE and value == Task.Status.IN_PROGRESS:
            raise serializers.ValidationError("Overdue tasks cannot move back to IN_PROGRESS.")

        # Rule 2: Only Admins can close overdue tasks (Mark as DONE)
        if instance.status == Task.Status.OVERDUE and value == Task.Status.DONE:
            if not (user and user.is_staff):
                raise serializers.ValidationError("Only Admins can close overdue tasks.")

        return value
