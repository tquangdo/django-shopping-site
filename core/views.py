from django.shortcuts import render
from django.views import View


class onHomeView(View):
    def get(self, request):
        return render(request, 'homepage/index.html')
