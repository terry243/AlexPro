from django import forms
from .models import utilisateur,Lignebdgetaire, Produit

class UserForm(forms.ModelForm):
    
   class Meta:
      model = utilisateur
      fields= ('name','type','position','adresse','email','password')
        
   
class LignebudgetaireForm(forms.ModelForm):
    
   class Meta:
      model = Lignebdgetaire
      fields= ('name','origine','nomorigine','adresse','montant')
        
   
class ProduitForm(forms.ModelForm):
   class Meta:
      model = Produit
      fields = ('nom','description','cathegorie','prix')
    
    
    