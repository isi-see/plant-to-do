from django.shortcuts import render
from django.views import View
from django.conf import settings

## create views

class HomeView(View):
    def get(self, request):
        host = request.get_host()
        islocal = host.find('localhost')>0 or host.find('127.0.0.1') >=0
        context = {
            'installed':settings.INSTALLED_APPS,
            'islocal':islocal
            }
        return render(request, 'home/main.html', context)
