from django.urls import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from mainapp.models import News, Courses
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
import mainapp.forms as mainapp_forms
import mainapp.models as mainapp_models



class MainPageView(TemplateView):
    template_name = "mainapp/index.html"
    
class NewsListView(ListView):
    model = News
    paginate_by = 5
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)

class NewsCreateView(PermissionRequiredMixin, CreateView):
    model = News
    fields = "__all__"
    success_url = reverse_lazy("mainapp:news")
    permission_required = ("mainapp.add_news",)
    
class NewsDetailView(DetailView):
    model = News

class NewsUpdateView(PermissionRequiredMixin, UpdateView):
    model = News
    fields = "__all__"
    success_url = reverse_lazy("mainapp:news")
    permission_required = ("mainapp.change_news",)

class NewsDeleteView(PermissionRequiredMixin, DeleteView):
    model = News
    success_url = reverse_lazy("mainapp:news")
    permission_required = ("mainapp.delete_news",)

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


class CoursesListView(TemplateView): 
    template_name = "mainapp/courses_list.html"
    
    def get_context_data(self, **kwargs):
        context = super(CoursesListView, self).get_context_data(**kwargs) 
        context["objects"] = mainapp_models.Courses.objects.all()[:7] 
        return context

class CoursesDetailView(TemplateView): 
    template_name = "mainapp/courses_detail.html"
    
    def get_context_data(self, pk=None, **kwargs):
        context = super(CoursesDetailView, self).get_context_data(**kwargs) 
        context["course_object"] = get_object_or_404(mainapp_models.Courses, pk=pk)
        context["lessons"] = mainapp_models.Lessons.objects.filter(course=context["course_object"])
        context["teachers"] = mainapp_models.Teachers.objects.filter(course=context["course_object"])
        if not self.request.user.is_anonymous:
            if not mainapp_models.CourseFeedback.objects.filter(
                course=context["course_object"], user=self.request.user ).count():
                    context["feedback_form"] = mainapp_forms.CourseFeedbackForm(course=context["course_object"], user=self.request.user)
            context["feedback_list"] = mainapp_models.CourseFeedback.objects.filter(
                course=context["course_object"] ).order_by("-created", "-rating")[:5] 
        return context
    
class CourseFeedbackFormProcessView(LoginRequiredMixin, CreateView):
    model = mainapp_models.CourseFeedback
    form_class = mainapp_forms.CourseFeedbackForm

    def form_valid(self, form):
        self.object = form.save()
        rendered_card = render_to_string("mainapp/includes/feedback_card.html", context={"item": self.object})
        return JsonResponse({"card": rendered_card})
