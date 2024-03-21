from django.shortcuts import render
import math

# Create your views here.
def index(request):
    context = {
        'titulo':"Formulario",
    }
    return render(request,'encuesta/formulario.html',context)   

def enviar(request):
    context={
        'titulo':"Respuesta",
        'nombre':request.POST['nombre'],
        'clave':request.POST['password'],
        'educacion':request.POST['educacion'],
        'nacionalidad':request.POST['nacionalidad'],
        'idiomas':request.POST.getlist('idiomas'),
        'correo':request.POST['email'],
        'website':request.POST['sitioweb'],
       

    }
    return render(request,'encuesta/respuesta.html',context)

#Operaciones   
def calcular(request):
    if request.method == 'POST':
        numero1 = int(request.POST.get('numero1', 0))
        numero2 = int(request.POST.get('numero2', 0))
        operacion = request.POST.get('operacion', '')

        if operacion == 'suma':
            resultado = numero1 + numero2
            operacion_texto = 'Suma'
        elif operacion == 'resta':
            resultado = numero1 - numero2
            operacion_texto = 'Resta'
        elif operacion == 'multiplicacion':
            resultado = numero1 * numero2
            operacion_texto = 'Multiplicación'

        context = {
            'titulo': "Resultado",
            'resultado': resultado,
            'numero1': numero1,
            'numero2': numero2,
            'operacion_texto': operacion_texto
        }
        return render(request, 'encuesta/resultado.html', context)
    else:
        # Manejar la solicitud GET devolviendo el formulario
        return render(request, 'encuesta/operaciones.html')
 
#Volumen del cilindro   
def calcular_cilindro(request):
    if request.method == 'POST':
        altura = float(request.POST['altura'])
        diametro = float(request.POST['diametro'])

        radio = diametro / 2
        volumen = math.pi * (radio ** 2) * altura

        context = {
            'titulo': "Resultado",
            'volumen': volumen
        }
        return render(request, 'encuesta/resultado_cilindro.html', context)
    else:
        # Manejar la solicitud GET devolviendo el formulario
        return render(request, 'encuesta/cilindro.html')