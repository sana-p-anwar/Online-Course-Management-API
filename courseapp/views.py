from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from courseapp.models import CourseDb
from courseapp.serializer import CourseSerializer
from courseapp.models import EnrollmentDb
from courseapp.serializer import EnrollmentSerializer


# Create your views here.
class CourseListCreateView(APIView):
    
    def get(self, request):
        qs = CourseDb.objects.all()
        serializer_instance = CourseSerializer(qs, many=True)
        return Response(data=serializer_instance.data)

    def post(self, request):
        form_data = request.data
        serializer_instance = CourseSerializer(data=form_data)

        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            CourseDb.objects.create(**actual_data)
            return Response(data={"message": "Course added successfully."})
        else:
            return Response(data={"errors": serializer_instance.errors})
        

class CourseRetrieveUpdateDeleteView(APIView):
    
    def get(self, request, pk):
        qs = CourseDb.objects.get(id=pk)
        serializer_instance = CourseSerializer(qs)
        return Response(data=serializer_instance.data)

    def put(self, request, pk):
        form_data = request.data
        serializer_instance = CourseSerializer(data=form_data)

        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            CourseDb.objects.filter(id=pk).update(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

    def delete(self, request, pk):
        CourseDb.objects.filter(id=pk).delete()
        return Response({
            "Message": "Course deleted successfully..!"
        })

class EnrollmentListCreateView(APIView):
    def get(self, request):
        qs = EnrollmentDb.objects.all()
        enrollment_instance = EnrollmentSerializer(qs, many=True)
        return Response(data=enrollment_instance.data)

    def post(self, request):
        form_data = request.data
        serializer_instance = EnrollmentSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            EnrollmentDb.objects.create(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
class EnrollmentRetrieveUpdateDeleteView(APIView):
    def get(self, request, pk):
        qs = get_object_or_404(EnrollmentDb, id=pk)
        serializer_instance = EnrollmentSerializer(qs)
        return Response(data=serializer_instance.data)
    
class EvaluateEnrollmentView(APIView):
    
    def put(self, request, pk):
        form_data = request.data

        EnrollmentDb.objects.filter(id=pk).update(**form_data)

        return Response(data={
            "Message": "Updated..!"
        })