from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView


class CLStudent(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class RDUStudent(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
