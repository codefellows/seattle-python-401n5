from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "pages/things_home.html"