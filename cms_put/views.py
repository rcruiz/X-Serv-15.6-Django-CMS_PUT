from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Page


def mostrar_todo(request):
    lPages = Page.objects.all()
    respuesta = "<ul> Los contenidos almacenados son:<br>"
    for page in lPages:
        respuesta += '<li><a href="' + str(page.id) + '">'
        respuesta += page.name + '</a></li>'
    respuesta += "</ul>"
    return HttpResponse(respuesta)


def mostrar_id(request, page_id):
    try:
        contenido = Page.objects.get(id=int(page_id))
        return HttpResponse(contenido.name + ' : ' + contenido.page)
    except Page.DoesNotExist:
        return HttpResponse('Pagina no encontrada')


@csrf_exempt
def contenido(request, recurso):
    cuerpo = request.body
    formulario = "<form method = POST action=''" + recurso + ">"
    formulario += "Nombre: <input type='text' name='name'><br>"
    formulario += "Página: <input type='text' name='page'><br>"
    formulario += "<input type='submit' value='Enviar'></form>"

    if request.method == 'GET':
        try:
            contenido = Page.objects.get(name=recurso)
            respuesta = '<a href="/' + contenido.name + '">/'
            respuesta += contenido.name + '</a>' + ' : ' + contenido.page
        except Page.DoesNotExist:
            respuesta = "Página no almacenada. Insértela" + formulario
    elif request.method == 'PUT':
        try:  # Actualiza el contenido de la pagina
            contenidoAlmac = Page.objects.get(name=recurso)
            contenidoAlmac.page = cuerpo
            contenidoAlmac.save()
        except Page.DoesNotExist:
            contenido = Page(name=recurso, page=cuerpo)
            contenido.save()
        respuesta = "La página ha sido actualizada"
    elif request.method == 'POST':
        nombre = request.POST['name']
        pag = request.POST['page']
        contenido = Page(name=nombre, page=pag)
        contenido.save()
        respuesta = "Página guardada"
    else:
        respuesta = "Metodo introducido no válido"
    return HttpResponse(respuesta)
