from django.shortcuts import render
from django.views.generic import View


class IndexView(View):
    @staticmethod
    def get(request, params=None):
        return render(request, 'my_app/index.html')
