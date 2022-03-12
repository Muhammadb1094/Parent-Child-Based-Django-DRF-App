from django.urls import path
from . import views as frontend_view

urlpatterns = [
    path('', frontend_view.home.as_view(), name='home'),
    path('update/', frontend_view.update_title.as_view(), name='update_title'),
    path('add/child/', frontend_view.add_child_title.as_view(), name='add_child_title'),
    path('delete/title/', frontend_view.delete_title.as_view(), name='delete_title'),
]
