from rest_framework import serializers
from courseapp.models import CourseDb


class CourseSerializer(serializers.Serializer):
    course_name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    instructor = serializers.CharField(max_length=100)
    duration = serializers.IntegerField()
    fee = serializers.DecimalField(max_digits=10, decimal_places=2)
    category = serializers.CharField(max_length=50)

class EnrollmentSerializer(serializers.Serializer):
    course_id = serializers.IntegerField()
    student_name = serializers.CharField()
    payment_status = serializers.CharField(read_only =True)
    progress = serializers.IntegerField(read_only=True, required=False)
    remarks = serializers.CharField(required=False, allow_blank=True)
    enrollment_date = serializers.DateTimeField(read_only=True)

    def validate(self, validate_data):
        course_id = validate_data.get("course_id")
        if not CourseDb.objects.filter(id=course_id).exists():
            raise serializers.ValidationError("Course does not exist...!")
        return validate_data