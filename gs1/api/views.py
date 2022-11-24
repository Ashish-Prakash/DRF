from django.shortcuts import render
from .models import Student
from .serializers import studentSerializers
from rest_framework.renderers import JSONRenderer 
from django.http import HttpResponse, JsonResponse
# Create your views here.
def students_detail(request, pk):
    stu = Student.objects.get(id = pk)
    serializer = studentSerializers(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type ='application/json')

def student_list(request):
    stu = Student.objects.all()
    serializer = studentSerializers(stu, many = True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type ='application/json')
    return JsonResponse(serializer.data, safe= False)
