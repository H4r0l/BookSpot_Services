from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
# Create your views here.

method_decorator(csrf_exempt, name='dispatch')
class authAPI(View):
    def get(self, request):
        return HttpResponse(200, 'Alright')