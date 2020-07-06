from django.urls import path
from .views import HomeView


app_name = 'threads'


urlpatterns = [
    path('', HomeView.as_view(), name='index')
]
