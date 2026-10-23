from django.db import models

# Create your models here.
from django.db import models

class CourseDb(models.Model):
    course_name = models.CharField(max_length=100)
    description = models.TextField()
    instructor = models.CharField(max_length=100)
    duration = models.IntegerField()
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)

class EnrollmentDb(models.Model):
    course_id = models.IntegerField()
    student_name = models.CharField(max_length=100)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=50)
    progress = models.PositiveIntegerField(null=True)
    remarks = models.TextField(null=True)