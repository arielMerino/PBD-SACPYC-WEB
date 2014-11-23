# -*- encoding: utf-8 -*-
#controlador
from django.shortcuts import render #para llamar a los template
from django.views.generic import TemplateView
from django.template import RequestContext

class Cotizar(TemplateView):
	def __init__(self,valor): #cuando usas INIT, debes siempre inicializar todos tus objetos.
		self.valor = valor
		self.context = {'nombre':'','apellido':'','phone':'','email':'','comuna':'','calle':'','dir':'','block':'','dpto':'','fecha':'','duracion':'','invitados':''}
	def llamadaCotizar(self,request):
		print self.context['nombre']
		print self.context['apellido']
		print self.context['phone']
		print self.context['email']
		print self.context['comuna']
		print self.context['calle']
		print self.context['dir']
		print self.context['block']
		print self.context['dpto']
		return render(request,'Cotizar/cotizar.html',self.context)

	def llamadaCotizarEv(self,request):
		nombre = request.POST.get('nombre')
		apellido = request.POST.get('apellido')
		phone = request.POST.get('phone')
		email = request.POST.get('email')
		comuna = request.POST.get('comuna')
		calle = request.POST.get('calle')
		direc = request.POST.get('dir')
		blocke = request.POST.get('blocke')
		dpto = request.POST.get('dpto')

		self.context['nombre'] = nombre
		self.context['apellido'] = apellido
		self.context['phone'] = phone
		self.context['email'] = email
		self.context['comuna'] = comuna
		self.context['calle'] = calle
		self.context['dir'] = direc
		self.context['blocke'] = blocke
		self.context['dpto'] = dpto

		print self.context['nombre']
		print self.context['apellido']
		print self.context['phone']
		print self.context['email']
		print self.context['comuna']
		print self.context['calle']
		print self.context['dir']
		print self.context['blocke']
		print self.context['dpto']
		return render(request,'Cotizar/cotizarEv.html',self.context)

	def llamadaCotizarCat(self,request):
		nombre = request.POST.get('nombre')
		apellido = request.POST.get('apellido')
		phone = request.POST.get('phone')
		email = request.POST.get('email')
		comuna = request.POST.get('comuna')
		calle = request.POST.get('calle')
		direc = request.POST.get('dir')
		blocke = request.POST.get('blocke')
		dpto = request.POST.get('dpto')
		fecha = request.POST.get('fecha')
		hora = request.POST.get('hora')
		duracion = request.POST.get('duracion')
		invitados = request.POST.get('invitados')

		self.context['nombre'] = nombre
		self.context['apellido'] = apellido
		self.context['phone'] = phone
		self.context['email'] = email
		self.context['comuna'] = comuna
		self.context['calle'] = calle
		self.context['dir'] = direc
		self.context['blocke'] = blocke
		self.context['dpto'] = dpto
		self.context['fecha'] = fecha
		self.context['hora'] = hora
		self.context['duracion'] = duracion
		self.context['invitados'] = invitados

		print self.context['nombre']
		print self.context['apellido']
		print self.context['phone']
		print self.context['email']
		print self.context['comuna']
		print self.context['calle']
		print self.context['dir']
		print self.context['blocke']
		print self.context['dpto']
		print self.context['fecha']
		print self.context['hora']
		print self.context['duracion'] 
		print self.context['invitados']
		return render(request, 'Cotizar/cotizarCat.html', self.context)	
		
		
