from django.views.generic import TemplateView
from api.models import Topic


class home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = {
            'base_url': 'http://127.0.0.1:8000'
        }

        return context


class update_title(TemplateView):

    template_name = "update.html"

    def get_context_data(self, **kwargs):
        context = {
            'topics': Topic.objects.all(),
            'base_url': 'http://127.0.0.1:8000'
        }

        return context


class add_child_title(TemplateView):

    template_name = "child.html"

    def get_context_data(self, **kwargs):
        context = {
            'topics': Topic.objects.all(),
            'base_url': 'http://127.0.0.1:8000'
        }

        return context


class delete_title(TemplateView):

    template_name = "delete.html"

    def get_context_data(self, **kwargs):
        context = {
            'topics': Topic.objects.all(),
            'base_url': 'http://127.0.0.1:8000'
        }

        return context

