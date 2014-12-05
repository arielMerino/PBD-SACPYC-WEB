# -*- encoding: utf-8 -*-
#controlador
from django.shortcuts import render #para llamar a los template
from django.views.generic import TemplateView
from django.template import RequestContext

class Menu(TemplateView):
	def __init__(self, valor):
		self.valor = valor
		self.context = {}
	def llamadaMenu(self,request):
		return render(request,'menu/menu.html',self.context)