from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from models import Pages


def mostrar_todo(request):
    #if request.method == "GET":
    lPages = Pages.objects.all()
    respuesta = "<ul> <h3> Los contenidos almacenados son:</h3><br>"
    for page in lPages:
        respuesta += '<li><a href="' + str(page.id) + '">'
        respuesta += page.Name + '</a></li>'
    respuesta += "</ul>"
    return HttpResponse(respuesta)


def mostrar_id(request, page_id):
    try:
        contenido = Pages.objects.get(id=int(page_id))
        return HttpResponse(contenido.Name + ' -> ' + contenido.Page)
    except Pages.DoesNotExist:
        return HttpResponse('Pagina no encontrada')


@csrf_exempt
def contenido(request, recurso):
    cuerpo = request.body
    if request.method == 'PUT':
        try:  # Actualiza el contenido de la pagina
            contenidoAlmac = Pages.objects.get(Name=recurso)
            contenidoAlmac.Page = cuerpo
            contenidoAlmac.save()
        except Pages.DoesNotExist:
            contenido = Pages(Name=recurso, Page=cuerpo)
            contenido.save()
    try:  # Hace el GET
        contenido = Pages.objects.get(Name=recurso)
        return HttpResponse(contenido.Page)
    except Pages.DoesNotExist:
        return HttpResponse('Pagina no encontrada')
