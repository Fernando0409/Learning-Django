from django.http import HttpResponse

def welcome(request): # Primera vista
	return HttpResponse("Hola, esta es mi primer pagina con Django")

def goodBye(request): # Vista de despedida
	return HttpResponse("Fue un placer, nos vemos luegos")
