from django.urls import path

from . import views


urlpatterns = [
    path(r'^not_optimized$', views.index, name='not_optimized_index'),
]
