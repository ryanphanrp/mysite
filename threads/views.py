from django.shortcuts import render, HttpResponse
from django.views import View


# Create your views here.

class HomeView(View):
    @staticmethod
    def get(request):
        return HttpResponse("<h1>blackpinkinyourarea</h1>")