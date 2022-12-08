from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status, viewsets


class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        # print("self BaseName " + self.basename)
        # print("self action " + self.action)
        # print("self detail " + self.detail)
        # print("self suffix " + self.suffix)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        res = serializer.data
        return Response(res)

    def retrieve(self, request, pk=None):
        # print("self BaseName " + self.basename)
        # print("self action " + self.action)
        # print("self detail " + self.detail)
        # print("self suffix " + self.suffix)
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

    def create(self, request):
        # print("self BaseName " + self.basename)
        # print("self action " + self.action)
        # print("self detail " + self.detail)
        # print("self suffix " + self.suffix)
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Updated'}, status=status.HTTP_202_ACCEPTED)
        # print("self BaseName " + self.basename)
        # print("self action " + self.action)
        # print("self detail " + self.detail)
        # print("self suffix " + self.suffix)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Patial Update'}, status=status.HTTP_202_ACCEPTED)
        # print("self BaseName " + self.basename)
        # print("self action " + self.action)
        # print("self detail " + self.detail)
        # print("self suffix " + self.suffix)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        # print("self BaseName " + self.basename)
        # print("self action " + self.action)
        # print("self detail " + self.detail)
        # print("self suffix " + self.suffix)
        return Response({'msg': 'Data Deleted'}, status=status.HTTP_204_NO_CONTENT)
