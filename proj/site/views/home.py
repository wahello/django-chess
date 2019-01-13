
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse


def home_view(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')

    return TemplateResponse(request, 'home.html')
