from .models import Student
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']

    def validate_roll(self, value):
        if value >= 200:
            return serializers.ValidationError('Value is Greater than 200')
        return value