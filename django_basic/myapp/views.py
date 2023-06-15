from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello")

class Home(TemplateView):
    Template_name="myapp/home.html"