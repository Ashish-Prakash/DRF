from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from django.http import JsonResponse

# Create your views here.


def studentinfo(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    return JsonResponse(serializer.data, safe=False)
