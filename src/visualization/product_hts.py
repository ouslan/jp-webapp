from django.shortcuts import render

def products_hts(request):
    return render(request, 'product_hts.html')