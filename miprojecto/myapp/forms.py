from django import forms


class FormularioCurso(forms.Form):

    nombre = forms.CharField(label="Nombre", max_length=128)
    inscriptos = forms.IntegerField(label="Inscriptos")
    solo_empresas = forms.BooleanField(label="Es empresa?", required=True)
    fecha_inicio = forms.DateField(label="Fecha de inicio", 
        widget=forms.DateInput(attrs={"type": "date"}, format='%d/%m/%Y'),
        input_formats=('%d/%m/%Y', ))

