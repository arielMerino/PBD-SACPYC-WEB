# -*- encoding: utf-8 -*-
#controlador
from django.shortcuts import render #para llamar a los template
from django.views.generic import TemplateView
from django.template import RequestContext

class Contacto(TemplateView):
	def __init__(self,valor): #cuando usas INIT, debes siempre inicializar todos tus objetos.
		self.valor = valor
	def llamadaContacto(self,request):
		return render(request,'contacto/contacto.html',{})