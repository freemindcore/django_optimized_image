from django.urls import path

from . import views


urlpatterns = [
    path(r'^optimized$', views.index, name='optimized_index'),
]
