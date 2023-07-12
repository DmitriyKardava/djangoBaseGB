from django.views.generic import TemplateView, ListView
from django.shortcuts import redirect
from requests.models import PreparedRequest

import json
from django.conf import settings
import os

class MainPageView(TemplateView):
    template_name = "mainapp/index.html"
    
class NewsPageView(ListView):
    template_name = "mainapp/news.html"
    paginate_by = 5

    def get_queryset(self):
        with open(os.path.join(settings.BASE_DIR, 'data/news.json')) as news_file:
            return json.load(news_file)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["news_title"] = "Тестовая новость для поиска"
        context["news_preview"] = "Предварительное описание, которое заинтересует каждого"
        context["search_str"] = "описание"
        context["search_str2"] = "заинтересует"
        return context            

class CoursesPageView(TemplateView):
    template_name = "mainapp/courses_list.html"

class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"

class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"

class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"

def SearchRedirect(request, search_str=''):
    req = PreparedRequest()
    url = "https://google.com/search"
    params = {'q':search_str}
    req.prepare_url(url, params)
    respose = redirect(req.url)
    return respose
