from django.shortcuts import render
from django.views.generic import TemplateView

class Contacto(TemplateView):
	def __init__(self,valor):
		self.valor=valor
	def llamada(self,request):
		return render(request, 'contactos/contactos.html',{})


# Create your views here.
