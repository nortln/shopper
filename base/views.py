from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator


from .models import Catalog, Brand, Product, Cart


def home(request):
    catalog = Catalog.objects.all()
    brands = Brand.objects.all()
    products = Product.objects.all()
    page = request.GET.get("page")
    paginator = Paginator(products, 8)
    page_obj = paginator.get_page(page)
    context = {
        "catalog": catalog,
        "brands": brands,
        "products": page_obj,
    }
    return render(request, "index.html", context)


def page(request, page=1):
    catalog = Catalog.objects.all()
    brands = Brand.objects.all()
    products = Product.objects.all()
    paginator = Paginator(products, 8)
    page_obj = paginator.get_page(page)

    context = {
        "catalog": catalog,
        "brands": brands,
        "products": page_obj,
    }

    return render(request, "index.html", context)


def product(request, pk):
    product = get_object_or_404(Product, id=pk)
    # product = Product.objects.get(id=pk)
    context = {
        "product": product,
    }
    return render(request, "product.html", context)


def add_cart(request, pk):
    if request.method == "POST":
        product = Product.objects.get(id=pk)
        cart_products = Cart.product.get_queryset()
        if product not in cart_products:
            cart = Cart(user=request.user,
                product=product,
                quantity=request.POST["quantity"])
            cart.user = request.user
            cart.save()
        else:
            cart_product = Cart.objects.get(product=product)
            cart_product.quantity += int(request.POST["quantity"])
            cart_product.save()
    
    return redirect("home")



def cart(request):
    cart = Cart.objects.all()
    context = {
        "cart": cart,
    }
    return render(request, "cart.html")



def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def faq(request):
    return render(request, "faq.html")


def personal_info(request):
    return render(request, "personal_info.html")

def payment_choose(request):
    return render(request, "payment-choose.html")

def address(request):
    return render(request, "address.html")

def address_edit(request):
    return render(request, "address-edit.html")


def auth(request):
    return render(request, "auth.html")


def login_user(request):
    if request.method == "POST":
         # email = request.POST["login_email"]
         username = request.POST["login_username"]
         password = request.POST["login_password"]
         
         user = authenticate(request, username=username.lower(), password=password)
         if user is not None:
             login(request, user)
             return redirect("home")
         else:
             return render(request, "auth.html", {"error_message": "Invalid Credentials"})
    return render(request, "auth.html")


def register_user(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["register_username"]
        email = request.POST["register_email"]
        password = request.POST["register_password"]
        confirm_password = request.POST["confirm_password"]
        
        user = User.objects.all()

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if confirm_password != password:
                    context = {
                    "register_error_message": "Password must match",
                    }
                    return render(request, "auth.html", context)
                else:
                    user = User()
                    user.username = username.lower()
                    user.first_name = first_name
                    user.last_name = last_name
                    user.email = email
                    user.set_password(password)
                    user.save()
                    login(request, user)
                    redirect("home")
            else:
                context = {
                    "register_error_message": "Email Already Exists",
                }
                return render(request, "auth.html", context)
        else:
            context = {
                "register_error_message": "Username Already Exists!!",
            }
            return render(request, "auth.html", context)
    
    return render(request, "auth.html")