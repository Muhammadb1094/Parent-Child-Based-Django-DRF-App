from django.urls import path
from . import views as api_view

urlpatterns = [
    path('topics/', api_view.topics, name='topics'),
    path('one/topic/<int:id>/', api_view.one_topic, name='one_topic'),
]
