from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406420772',
        'name': 'Kadek Ngurah Septyawan Chandra Diputra',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
