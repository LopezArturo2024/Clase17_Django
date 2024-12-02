from django.http import HttpResponse
from datetime import datetime
from django.template import Template,Context

def saludo(request):
    return HttpResponse("Prueba creando una vista en Django...")

def saludo_2(request):
    return HttpResponse("<h1>Segunda vista creada pero con HTML</h1>")

def fecha(request):
    dia=datetime.now()
    mensaje=f"<h1>La fecha de hoy es:</h1> {dia}"
    return HttpResponse(mensaje)

def nombre(request,nombre):
    mensaje_2=f"Aquí aparecerá el nombre de la URL: {nombre}"
    return HttpResponse(mensaje_2)

def probandotemplate(self):
    mihtml=open("./mysite/plantillas/template1.html")
    plantilla=Template(mihtml.read())
    mihtml.close()
    micontexto=Context()
    documento=plantilla.render(micontexto)
    return HttpResponse(documento)

