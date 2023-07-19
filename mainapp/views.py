from mainapp.models import News, Courses
from django.views.generic import TemplateView, ListView


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"
    
class NewsPageView(ListView):
    model = News
    template_name = "mainapp/news.html"
    paginate_by = 5

class CoursesPageView(ListView):
    template_name = "mainapp/courses_list.html"
    model=Courses
    paginate_by = 5

class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"

class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"

class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"

