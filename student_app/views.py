from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, TemplateView
from . import models

# Create your views here.
class SchoolListView(ListView):
    model = models.School
    
class SchoolDetailView(DetailView):
    model = models.School
    template_name = 'student_app/school_detail.html'