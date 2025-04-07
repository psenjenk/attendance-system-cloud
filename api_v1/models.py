from django.db import models
from django.core.validators import EmailValidator, RegexValidator
from django.utils import timezone
from uuid import uuid4

def generateUUID():
    return str(uuid4())

class record(models.Model):
    recordAdded = models.DateTimeField(auto_now_add=True)
    recordModified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, unique=True)
    
    def __str__(self):
        return f"{self.code} - {self.name}"

class student(record):
    studentId = models.CharField(primary_key=True, default=generateUUID, editable=False, max_length=200)
    firstName = models.CharField(max_length=200, blank=False, null=False)
    lastName = models.CharField(max_length=200, blank=False, null=False)
    address = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    mobileNo = models.CharField(
        max_length=15,
        blank=False,
        null=False,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ]
    )
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='students')
    is_active = models.BooleanField(default=True)

    class Meta:
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['mobileNo']),
            models.Index(fields=['department']),
        ]

    def __str__(self):
        return f"{self.firstName} {self.lastName} ({self.studentId})"

class subjects(record):
    subjectCode = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, blank=False, null=False)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='subjects')
    credits = models.PositiveIntegerField(default=3)
    description = models.TextField(blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['department']),
        ]
        unique_together = ['title', 'department']

    def __str__(self):
        return f"{self.title} ({self.subjectCode})"

class studentSubject(record):
    studentId = models.ForeignKey(student, on_delete=models.CASCADE, related_name='enrolled_subjects')
    subjectCode = models.ForeignKey(subjects, on_delete=models.CASCADE, related_name='enrolled_students')
    enrollment_date = models.DateField(default=timezone.now)
    grade = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        unique_together = ['studentId', 'subjectCode']
        indexes = [
            models.Index(fields=['studentId', 'subjectCode']),
        ]

    def __str__(self):
        return f"{self.studentId} - {self.subjectCode}"

class attendance(record):
    ATTENDANCE_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
        ('excused', 'Excused'),
    ]

    studentId = models.ForeignKey(student, on_delete=models.CASCADE, related_name='attendances')
    subjectCode = models.ForeignKey(subjects, on_delete=models.CASCADE, related_name='attendances')
    lectureDate = models.DateField()
    status = models.CharField(max_length=20, choices=ATTENDANCE_CHOICES, default='absent')
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ['studentId', 'subjectCode', 'lectureDate']
        indexes = [
            models.Index(fields=['studentId', 'lectureDate']),
            models.Index(fields=['subjectCode', 'lectureDate']),
        ]

    def __str__(self):
        return f"{self.studentId} - {self.subjectCode} - {self.lectureDate} ({self.status})"