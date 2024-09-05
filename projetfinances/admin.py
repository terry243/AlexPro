from django.contrib import admin
from .models import utilisateur, User , Lignebdgetaire, Produit

# Register your models here.
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('name','type','position','adresse','email','password')

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','first_name','last_name','email','password')

class LignebudgetaireAdmin(admin.ModelAdmin):
    list_display = ('name','origine','nomorigine','adresse','montant')

class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom','description','cathegorie','prix')


admin.site.register(Produit,ProduitAdmin)

admin.site.register(utilisateur,UtilisateurAdmin)
admin.site.register(Lignebdgetaire,LignebudgetaireAdmin)
admin.site.register(User,UserAdmin)
