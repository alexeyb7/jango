from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class MainPageView(TemplateView):
    template_name = "mainapp/index.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Приветствую, путник!'
        return context_data

class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"

class CoursesPageView(TemplateView):
    template_name = "mainapp/courses_list.html"


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"

class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"

class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"
