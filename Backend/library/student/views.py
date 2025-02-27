from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student
from .forms import StudentForm


# Create your views here.
class StudentListView(ListView):
    model = Student
    template_name = 'student/student_list.html'


class StudentDetailView(DetailView):
    model = Student
    template_name = 'student/student_detail.html'


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/student_create.html'
    success_url = reverse_lazy('student_list')


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/student_update.html'
    success_url = reverse_lazy('student_list')


class StudentDeleteView(View):
    def post(self, request, pk):
        author = get_object_or_404(Student, pk=pk)
        author.delete()
        return redirect('student_list')
