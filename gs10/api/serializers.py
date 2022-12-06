from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']
        # read_only_fields = ['name']

    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Greater than 200')
        return value

    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')

        if nm.lower() == 'ashish' and ct.lower() != 'delhi':
            raise serializers.ValidationError('City is Not Delhi')
        return data
