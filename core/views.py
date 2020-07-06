from django.shortcuts import render
from django.views import View


# Create your views here.


class IndexView(View):
    @staticmethod
    def get(request):
        return render(request, 'base.html')