from django.test import TestCase
from django.http import HttpResponse


# Create your tests here.
def home(request):
    return HttpResponse("<h1> Testing Django.......</h1>")
