from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, TemplateView
from . import models

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'


class SchoolListView(ListView):
    #ListView provides context as *modelnameinlowercase*_list 
    context_object_name = 'schools' #for custom context name
    model = models.School
    
    
class SchoolDetailView(DetailView):
    #DetailView provides *modelnameinlowercase* as the context name
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'student_app/school_detail.html'