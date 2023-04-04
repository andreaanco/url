from django.shortcuts import render


# Create your views here.


def cilindro(request):
    if request.method == 'POST':
      
        altura = float(request.POST['altura'])
        diametro = float(request.POST['diametro'])
   
        radio = diametro / 2
    
        volumen = 3.14159 * radio**2 * altura
        return render(request, 'cilindro/formulario.html', {'volumen': volumen})
    else:
        return render(request, 'cilindro/formulario.html')