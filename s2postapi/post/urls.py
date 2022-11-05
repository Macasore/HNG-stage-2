from django.urls import path
from .views import view


urlpatterns = [
    #view path
    path('', view.as_view()),
]
