from django.shortcuts import render


# Le chemin de index est définis dans settings.py (DIRS)
def my_view(request):
    # fonction qui me retourne ma page html
    return render(request, 'index.html')
