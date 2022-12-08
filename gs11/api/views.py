from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
# Create your views here.


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def studentapi(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Inserted'}
            return Response(res, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        data = request.data
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Completely Updated'}
            return Response(res, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        data = request.data
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Partial Updated'}
            return Response(res, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        res = {'msg': 'Data Deleted'}
        return Response(res, status=status.HTTP_200_OK)
