
from django.shortcuts import redirect, render
from abonnement.models import Abonnement
# from article.models import Article



def Home(request):
    # renvoyer la page index html
    return render(request, 'index.html')

def Contact(request):
    added = False
    # fonction reçois les données du formulaire
    
    if request.method == "POST":
        # récupère les donnée
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']

        abonnement = Abonnement()
        abonnement.name = name
        abonnement.phone = phone
        abonnement.address = address
        abonnement.email = email
        # les enregistre dans la bd
        abonnement.save()
        added = True

    return render(request, "contact.html", {'added':added})

def Practice(request):
    return render(request, "practice.html")

