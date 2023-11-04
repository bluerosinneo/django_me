# me/views.py
from django.views.generic import TemplateView


class AboutMeView(TemplateView):
    template_name = "about.html"


class InterestsMeView(TemplateView):
    template_name = "interests.html"
