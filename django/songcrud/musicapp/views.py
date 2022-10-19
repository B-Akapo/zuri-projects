from django.http import HttpResponse


def index(request):
    return HttpResponse("I am creating a music app using Django")

# Create your views here.
