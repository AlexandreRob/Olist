from django.http import HttpResponse
from django.template import loader

def connexion(request):
  template = loader.get_template('accueil.html')
  return HttpResponse(template.render())