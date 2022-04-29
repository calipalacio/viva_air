from django import forms

class FormularioContacto(forms.Form):

    indice_i = forms.IntegerField()
    numero_n = forms.IntegerField()