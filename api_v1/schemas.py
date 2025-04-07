from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers

# Common Parameters
student_id_param = openapi.Parameter(
    'studentId',
    openapi.IN_PATH,
    description="Student ID",
    type=openapi.TYPE_STRING
)

subject_code_param = openapi.Parameter(
    'subjectCode',
    openapi.IN_PATH,
    description="Subject Code",
    type=openapi.TYPE_INTEGER
)

# Response Schemas
class StudentResponse(serializers.Serializer):
    studentId = serializers.CharField()
    firstName = serializers.CharField()
    lastName = serializers.CharField()
    email = serializers.EmailField()
    mobileNo = serializers.CharField()
    department = serializers.CharField()

class SubjectResponse(serializers.Serializer):
    subjectCode = serializers.IntegerField()
    title = serializers.CharField()
    department = serializers.CharField()
    credits = serializers.IntegerField()

class AttendanceResponse(serializers.Serializer):
    studentId = serializers.CharField()
    subjectCode = serializers.IntegerField()
    lectureDate = serializers.DateField()
    status = serializers.ChoiceField(choices=['present', 'absent', 'late', 'excused'])
    remarks = serializers.CharField(required=False)

# Error Response Schema
class ErrorResponse(serializers.Serializer):
    error = serializers.CharField()
    message = serializers.CharField()
    status_code = serializers.IntegerField()

# Common Responses
error_response = {
    '400': openapi.Response('Bad Request', ErrorResponse),
    '401': openapi.Response('Unauthorized', ErrorResponse),
    '403': openapi.Response('Forbidden', ErrorResponse),
    '404': openapi.Response('Not Found', ErrorResponse),
    '500': openapi.Response('Internal Server Error', ErrorResponse),
} 