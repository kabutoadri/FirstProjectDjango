from django.shortcuts import render
from time import strftime


# Le chemin de index est définis dans settings.py (DIRS)
def my_view(request):
    time = strftime("%H:%M:%S")
    # fonction qui me retourne ma page html et les variables se trouvant dans la vue
    return render(request, 'index.html', locals())
