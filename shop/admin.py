from django.contrib import admin

from shop.models import Blog, Categorie, NewCommande, Produit, Commande, ProduitCommande, SousCategorie

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'description',)

admin.site.register(Categorie, CategoryAdmin)

class SousCategoryAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'description',)

admin.site.register(SousCategorie, SousCategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'prix_unitaire', 'quantity', 'sous_categorie', 'image')

admin.site.register(Produit, ProductAdmin)

class CommandeAdmin(admin.ModelAdmin):
    list_display = ('client', 'code', 'montant', 'montant', 'mode_payement', 'is_valid', 'created_at', 'updated_at')

admin.site.register(Commande, CommandeAdmin)

class NewCommandeAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'phone', 'email','sommeTotal' ,'items')

admin.site.register(NewCommande, NewCommandeAdmin)

admin.site.register(ProduitCommande)
admin.site.register(Blog)