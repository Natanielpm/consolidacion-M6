from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import Vehiculo
from .forms import VehiculoForm

def index(request):
    return render(request, 'index.html')

@login_required
def agregar_vehiculo(request):
    if request.method == 'POST':  # Este condicional verifica si se ha presionado el botón 'enviar' o 'submit' y su método es 'POST'
        AddForm = VehiculoForm(request.POST)  # Carga los datos del form una vez se ha presionado 'enviar' o 'submit'
        if AddForm.is_valid():
            AddForm.save()  # .save guardará los datos en la BD
            messages.success(request, 'El vehículo se ha guardado exitosamente.')
            return redirect('agregar_vehiculo')  # Redirige a la página principal
        else:
            messages.error(request, 'Error! No se han guardado los datos. Por favor, verifique los datos ingresados e inténtelo nuevamente.')

    AddForm = VehiculoForm()  # Carga el form en la variable de contexto
    return render(request, 'vehiculo_form.html', {'AddForm': AddForm})

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('index')  # Redirige al index después de registrarse
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

@login_required
def vehiculo_catalogo(request):
    # Variables de filtros por costo
    CostoBajo = Vehiculo.objects.filter(precio__lt=10000)
    CostoMedio = Vehiculo.objects.filter(precio__gte=10000, precio__lte=30000)
    CostoAlto = Vehiculo.objects.filter(precio__gt=30000)
    # Variable que captura los datos de la BD en un listado de vehículos definiendo sus atributos
    vehiculos = list(Vehiculo.objects.all().values('marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio', 'fecha_creacion', 'fecha_modificado'))
    # Renderiza la plantilla y le entrega las variables antes definidas
    return render(request, 'vehiculo_Catalogo.html', {
        'vehiculos': vehiculos,
        'costo_bajo': CostoBajo,
        'costo_medio': CostoMedio,
        'costo_alto': CostoAlto,
    })
