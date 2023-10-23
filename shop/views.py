from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from shop.models import Blog, Categorie, Produit, SousCategorie, NewCommande

# Create your views here.


def home_page_view(request, category=None):
    produits = Produit.objects.all()
    categories = SousCategorie.objects.all()
    recherche = request.GET.get('recherche')
    if category:
        category = get_object_or_404(SousCategorie, slug=category)
        produits = produits.filter(sous_categorie=category)
    if recherche != '' and recherche is not None :
        produits = Produit.objects.filter(libelle__icontains=recherche)
        categories = SousCategorie.objects.filter(libelle__icontains=recherche)
    context =  {'produits': produits, 'categories': categories, 'category': category}
    return render(request, "base/hompage.html", context)

def shop_page_view(request, category=None):
    produits = Produit.objects.all()
    categories = SousCategorie.objects.all()
    recherche = request.GET.get('recherche')
    if category:
        category = get_object_or_404(SousCategorie, slug=category)
        produits = produits.filter(sous_categorie=category)
    if recherche != '' and recherche is not None :
        produits = Produit.objects.filter(libelle__icontains=recherche)
        categories = SousCategorie.objects.filter(libelle__icontains=recherche)
    #pagination 
    paginer = Paginator(produits, 2)
    print(paginer.num_pages)
    page_number = request.GET.get("page")
    produits = paginer.get_page(page_number)
    context =  {'produits': produits, 'categories': categories, 'category': category}
    return render(request, "base/shop-grid.html", context)


def shop_detail_view(request, pk=None):
    produits = Produit.objects.all()[:4]
    produit = Produit.objects.get(id=pk)
    context = {'produit':produit, 'produits':produits}
    return render(request, "base/shop-details.html", context)

def shop_cart_view(request):
    return render(request, "base/shoping-cart.html")

def contact_view(request):
    return render(request, "base/contact.html")

def checkout_view(request):
    if request.method == 'POST':
        items = request.POST.get('items')
        prenom = request.POST.get('prenom')
        nom = request.POST.get('nom')
        pays = request.POST.get('pays')
        ville = request.POST.get('ville')
        lieu = request.POST.get('lieu')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        codepostal = request.POST.get('codepostal')
        password = request.POST.get('password')
        mobile = request.POST.get('mobile')
        sommeTotal = request.POST.get('sommeTotal')

        commande = NewCommande(items=items, prenom=prenom,nom=nom,pays=pays,ville=ville,lieu=lieu,email=email,phone=phone,codepostal=codepostal, password=password,mobile=mobile, sommeTotal=sommeTotal)
        print(commande)
        commande.save()
    return render(request, "base/checkout.html")

#----------------------------------------------------------------
# Check blog

def blog_view(request, category=None):
    blogs  = Blog.objects.all()
    categories = Categorie.objects.all()
    if category:
        category = get_object_or_404(Categorie, slug=category)
        blogs = blogs.filter(categgorie=category)
    context = {'blogs': blogs, 'categories': categories}
    return render(request, "blog/blog.html", context)

def blog_detail_view(request, slug : str, category=None):
    blog = Blog.objects.get(slug=slug)
    categories = Categorie.objects.all()
    if category:
        category = get_object_or_404(Categorie, slug=category)
        blog = blog.filter(category=category)

    context = {'blog': blog, 'categories': categories}
    return render(request, "blog/blog-details.html", context)