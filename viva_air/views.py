import requests

from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from viva_air.forms import FormularioContacto
from viva_air.getinfo import get_info

def hello(request):

    return HttpResponse("Hello, world")

def contacto(request):

    if request.method == "POST":

        miFormulario = FormularioContacto(request.POST)

        if miFormulario.is_valid():

            infForm = miFormulario.cleaned_data
            # print(infForm)
            indice_i = infForm.get('indice_i')
            numero_n = infForm.get('numero_n')
            print(indice_i)
            print(numero_n)

            top_stories, info_items = get_info(indice_i, numero_n)
            print(top_stories)
            print(info_items)

            context = {
                'top_stories': top_stories,
                'info_items': info_items,
            }

            # print(type(infForm))

            # return render(request, "gracias.html", {"top_stories":top_stories}, {"info_items":info_items})
            return render(request, "gracias.html", context)



    else:

        miFormulario = FormularioContacto()

    return render(request, "formulario_contacto.html", {"form":miFormulario})