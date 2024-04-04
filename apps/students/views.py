import csv

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import widgets
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from apps.corecode.models import Subject
from apps.finance.models import Invoice
from django.shortcuts import get_object_or_404, redirect
from .models import Student, StudentBulkUpload,StudentSubjectAssignment
from django.views.generic import ListView

class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = "students/student_list.html"
    def get_queryset(self):
        # Get the registration number of the logged-in user
        registration_number = self.request.user.username
        if(registration_number=='admin'):
            return Student.objects.all()
        else:
        # Filter the queryset based on the registration number
            return Student.objects.filter(registration_number=registration_number)

    def get_object(self, queryset=None):
        # Get the object based on the filtered queryset
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs.get('pk'))
        return obj


class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = "students/student_detail.html"

    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        context["payments"] = Invoice.objects.filter(student=self.object)
        return context


class StudentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Student
    fields = "__all__"
    success_message = "New student successfully added."

    def get_form(self):
        """add date picker in forms"""
        form = super(StudentCreateView, self).get_form()
        form.fields["date_of_birth"].widget = widgets.DateInput(attrs={"type": "date"})
        form.fields["address"].widget = widgets.Textarea(attrs={"rows": 2})
        form.fields["others"].widget = widgets.Textarea(attrs={"rows": 2})
        return form


class StudentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Student
    fields = "__all__"
    success_message = "Record successfully updated."

    def get_form(self):
        """add date picker in forms"""
        form = super(StudentUpdateView, self).get_form()
        form.fields["date_of_birth"].widget = widgets.DateInput(attrs={"type": "date"})
        form.fields["date_of_admission"].widget = widgets.DateInput(
            attrs={"type": "date"}
        )
        form.fields["address"].widget = widgets.Textarea(attrs={"rows": 2})
        form.fields["others"].widget = widgets.Textarea(attrs={"rows": 2})
        # form.fields['passport'].widget = widgets.FileInput()
        return form


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy("student-list")


class StudentBulkUploadView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = StudentBulkUpload
    template_name = "students/students_upload.html"
    fields = ["csv_file"]
    success_url = "/student/list"
    success_message = "Successfully uploaded students"


class DownloadCSVViewdownloadcsv(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="student_template.csv"'

        writer = csv.writer(response)
        writer.writerow(
            [
                "registration_number",
                "surname",
                "firstname",
                "other_names",
                "gender",
                "parent_number",
                "address",
                "current_class",
            ]
        )

        return response

class StudentAssignView(LoginRequiredMixin, ListView):
    model = Student
    template_name = "students/student_assign.html"
    context_object_name = "students"

    def post(self, request, *args, **kwargs):
        student_regno = request.POST.get("student_regno")
        subject_name = request.POST.get("subject_name")

        # Get the student and subject objects
        student = Student.objects.get(registration_number=student_regno)
        subject = Subject.objects.get(name=subject_name)
        existing_assignment = StudentSubjectAssignment.objects.filter(student=student).first()

        if existing_assignment:
            # If an assignment exists, update the subject
            existing_assignment.subject = subject
            existing_assignment.save()
        # Create a new assignment
        else:
            
            assignment = StudentSubjectAssignment.objects.create(student=student, subject=subject)

        return redirect("student-assign")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add subjects to the context
        context['subjects'] = Subject.objects.all()
        return context

class StudentProjectView(LoginRequiredMixin, ListView):
    model = Student
    template_name = "students/student_project.html"
    context_object_name = "students"
    def get_queryset(self):
        # Get the registration number of the logged-in user
        registration_number = self.request.user.username
        if(registration_number=='admin'):
            return Student.objects.all()
        else:
        # Filter the queryset based on the registration number
            return Student.objects.filter(registration_number=registration_number)

    def get_object(self, queryset=None):
        # Get the object based on the filtered queryset
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs.get('pk'))
        return obj