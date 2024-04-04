from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.shortcuts import redirect, render
from .models import StudentAssignment
from apps.students.models import Student
from apps.corecode.models import Subject

class GradeAssignView(LoginRequiredMixin, ListView):
    model = Student
    template_name = "result/create_result.html"
    context_object_name = "students"

    def post(self, request, *args, **kwargs):
        for student in request.POST.getlist("students"):
            student_obj = Student.objects.get(id=student)
            grade = request.POST.get(f"grade_{student}")

            for assignment in student_obj.studentsubjectassignment_set.all():
                assignment.grade = grade
                assignment.save()
            else:
                StudentAssignment.objects.create(student=student_obj, subject=assignment.subject, grade=grade)

        return redirect("view-result")

class ViewGradesView(LoginRequiredMixin, ListView):
    model = StudentAssignment
    template_name = "result/view_result.html"
    context_object_name = "assignments"