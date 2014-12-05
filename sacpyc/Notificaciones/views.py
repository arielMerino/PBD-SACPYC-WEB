# -*- encoding: utf-8 -*-
#controlador
from django.shortcuts import render #para llamar a los template
from django.views.generic import TemplateView
from django.template import RequestContext

class Notificaciones(TemplateView):
	def __init__(self, valor):
		self.valor = valor
		self.context = {}
	def llamadaNotificaciones(self,request):
		return render(request,'notificaciones/notificaciones.html',self.context)