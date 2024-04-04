from django.db import models
from apps.corecode.models import Subject
from apps.students.models import Student

class StudentAssignment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2, choices=[("A+", "A+"), ("A", "A"), ("B", "B"), ("C", "C"), ("D", "D"), ("E", "E"), ("F", "F")])
    class Meta:
        unique_together = ['student', 'subject']  # Ensure each student has only one assignment per subject

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.grade}"
