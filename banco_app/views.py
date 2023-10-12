from django.shortcuts import render, redirect
from .models import Voluntario  
from .models import Asistencia
from .forms import AsistenciaForm
from .forms import VoluntarioForm
from django.http import JsonResponse
from django.http import HttpResponse
from io import BytesIO
from django.template.loader import get_template
import weasyprint


def registro_voluntario(request):
    if request.method == 'POST':
        form = VoluntarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pag_exito')  # Redirigir a una página de registro exitoso
    else:
        form = VoluntarioForm()
    
    return render(request, 'registro_voluntario.html', {'form': form})

#===========================================================================

def pagina_exito(request):
    return render(request, 'pag_exito.html')


#===========================================================================


def registro_asistencia(request):
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exito')  # Redirigir a una página de registro exitoso
    else:
        form = AsistenciaForm()
    
    return render(request, 'registrar_asistencia.html', {'form': form})

#================================================================================

def exito (request):
    return render (request, 'exito.html')


def ver_voluntario(request):
    return render (request, 'ver_voluntario.html')
#================================================================================

def ver_asistencia(request):
    asistencias = Asistencia.objects.all()
    return render(request, 'ver_asistencia.html', {'asistencias': asistencias})

#==================================================================================
def inicio_web(request):
    return render(request,"inicio.html")

#=================================================================================



from django.http import HttpResponse
from django.template.loader import get_template
import weasyprint
from .models import Asistencia

def generar_pdf(request):
    # Obtén los datos de asistencia de tu aplicación
    asistencias = Asistencia.objects.all()  # Reemplaza con la forma en que obtienes tus datos

    # Creamos un contexto con los datos necesarios para la plantilla
    context = {
        'asistencias': asistencias,
    }

    # Renderizamos la plantilla con solo la tabla y el título
    template = get_template('ver_asistencia.html')
    html = template.render(context)

    # Configuramos la respuesta para generar el PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="registro_asistencias.pdf"'

    # Generamos el PDF con weasyprint
    weasyprint.HTML(string=html).write_pdf(response)

    return response

from django.shortcuts import render
from .models import Voluntario
#==========================================================================================


def seleccionar_voluntarios(request):
    voluntarios = Voluntario.objects.all()
    return render(request, 'registrar_asistencia.html', {'voluntarios': voluntarios})
