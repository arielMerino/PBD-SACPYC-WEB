# -*- encoding: utf-8 -*-
#controlador
from django.shortcuts import render #para llamar a los template
from django.views.generic import TemplateView
from django.template import RequestContext

class CotizarAd(TemplateView):
	def __init__(self, valor):
		self.valor = valor
		self.context = {}
	def llamadaCotizarAd(self,request):
		return render(request,'cotizarad/cotizarad.html',self.context)