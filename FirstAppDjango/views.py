from django.shortcuts import render


# Remplacer 'myapp/index.html par le bon chemin
def my_view(request):
    # View code here...
    return render(request, 'index.html')
