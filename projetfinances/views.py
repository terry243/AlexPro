from django.shortcuts import render, redirect
from .forms import UserForm,LignebudgetaireForm,ProduitForm
from .models import Produit

# Create your views here.

def index(request):
    produit = Produit.objects.all()
    context = {
        'produit':produit
    }
    return render(request,'index.html',context)

def ajouter(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listeproduit')
    else:
        form = ProduitForm()
    return render(request,'ajouterproduit.html',{'form':form})

def base(request):
    forms = UserForm()
    if request.method == 'POST':
        forms = UserForm(request.POST)
        if forms.is_valid():
            forms.save()
        forms = UserForm()
    return render(request,'base.html',{'forms':forms})

def entrer(request):
    forms = LignebudgetaireForm()
    if request.method == 'POST':
        forms = LignebudgetaireForm(request.POST)
        if forms.is_valid():
            forms.save()
        forms = LignebudgetaireForm()
    return render(request,'entrerdargent.html',{'forms':forms})