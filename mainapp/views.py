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
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['contacts'] = [
            {
                'map': 'https://yandex.ru/map-widget/v1/-/CCUAZHcrhA',
                'city': 'Санкт-Петербург',
                'phone': '+7-999-11-11111',
                'email':'geeklab@spb.ru',
                'address':'территория Петропавловская крепость, 3Ж',
            },{
                'map': 'https://yandex.ru/map-widget/v1/-/CCUAZHX3xB',
                'city': 'Казань',
                'phone': '+7-999-22-22222',
                'email':'geeklab@kz.ru',
                'address':'территория Кремль, 11, Казань, Республика Татарстан, Россия',
            },{
                'map': 'https://yandex.ru/map-widget/v1/-/CCUAZHh9kD',
                'city': 'Москва',
                'phone': '+7-999-33-33333',
                'email':'geeklab@msk.ru',
                'address':'Красная площадь, 7, Москва, Россия',
            },
        ]
        return context_data

class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"

class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"
