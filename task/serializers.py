from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Task
        fields = ('id', 'name', 'deadline', 'priority',
                  'description', 'completed', 'created_at', 'updated_at',
                  'user'
                  )
