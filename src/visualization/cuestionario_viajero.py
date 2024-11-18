from django.shortcuts import render

def travel_questionaire(request):
  return render(request, 'cuestionario_viajero.html')